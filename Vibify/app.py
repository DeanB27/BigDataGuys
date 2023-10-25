import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import re
import urllib.request


def id_from_url(url):
    try:
        url_regex = re.search(r"^https?:\/\/(?:open\.)?spotify.com\/(user|episode|playlist|track|album)\/(?:spotify\/playlist\/)?(\w*)", url)

        return url_regex.group(1), url_regex.group(2)

    except AttributeError:
        return 'invalid URL'


client_id = '8cfa81fbc4074f3aad32716a36044864'
client_secret = 'a64ec813eaa24d19a42c694dbc61ba35'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

st.title("Spotify Playlist Analyzer")

image = Image.open('Vibify.png')
st.sidebar.image(image)

playlist_name = st.sidebar.text_input("Enter the URL of the Spotify playlist:")
#playlist = sp.current_user_playlists(limit=20, offset=0)


if playlist_name:
    #playlists = sp.search(playlist_name, type="playlist")["playlists"]["items"]
    url_type, playlist_id = id_from_url(playlist_name)
else:
    playlist_id = None


if playlist_id:
    st.balloons()
    st.snow()
    playlist = sp.playlist(playlist_id)
    # playlist_cover = sp.playlist_cover_image(playlist_id=playlist_id)
    tracks = playlist["tracks"]["items"]
    track_names = [track["track"]["name"] for track in tracks]
    track_artists = [", ".join([artist["name"] for artist in track["track"]["artists"]]) for track in tracks]
    track_popularity = [track["track"]["popularity"] for track in tracks]
    # track_valence = [sp.audio_features(tracks=tracks).get("Valence") for track in tracks]
    track_duration = [track["track"]["duration_ms"] for track in tracks]
    track_album = [track["track"]["album"]["name"] for track in tracks]
    track_release_date = [track["track"]["album"]["release_date"] for track in tracks]
    # track_image = [track['album']['images'][0]['url'] for track in tracks]

# display the playlist data in a table

    st.write(f"## {playlist['name']}")
    # st.image({sp.playlist_cover_image(playlist)})
    st.write(f"**Description:** {playlist['description']}")
    st.write(f"**Number of tracks:** {len(tracks)}")
    st.write("")
    st.write("### Tracklist")
    st.write("| Name | Artist | Album | Release Date | Popularity | Duration (ms) | Mood")
    # st.write("| ---- | ------ | ----- | ------------ | ---------- | -------------- |")
    for i in range(len(tracks)):
        st.write(f"| {track_names[i]} | {track_artists[i]} | {track_album[i]} | {track_release_date[i]} |"
                 f" {track_popularity[i]} | {track_duration[i]} |")

    # create a dataframe from the playlist data
    data = {"Name": track_names, "Artist": track_artists, "Album": track_album, "Release Date": track_release_date, "Popularity": track_popularity, "Duration (ms)": track_duration}
    df = pd.DataFrame(data)

# display a histogram of track popularity
    fig_popularity = px.histogram(df, x="Popularity", nbins=20, title="Track Popularity Distribution")
    st.plotly_chart(fig_popularity)

# add a dropdown menu for bivariate analysis
    st.write("#### Bivariate Analysis")
    x_axis = st.selectbox("Select a variable for the x-axis:", ["Popularity", "Duration (ms)"])
    y_axis = st.selectbox("Select a variable for the y-axis:", ["Popularity", "Duration (ms)"])
    fig_bivariate = px.scatter(df, x=x_axis, y=y_axis, title=f"{x_axis} vs. {y_axis}")
    st.plotly_chart(fig_bivariate)

# add a dropdown menu for multivariate analysis
    st.write("#### Multivariate Analysis")
    color_by = st.selectbox("Select a variable to color by:", ["Artist", "Album", "Release Date"])
    size_by = st.selectbox("Select a variable to size by:", ["Popularity", "Duration (ms)"])
    fig_multivariate = px.scatter(df, x="Duration (ms)", y="Popularity", color=color_by, size=size_by, hover_name="Name", title="Duration vs. Popularity Colored by Artist")
    st.plotly_chart(fig_multivariate)

# add a summary of the playlist data
    st.write("")
    st.write("### Playlist Summary")
    st.write(f"**Most popular track:** {df.iloc[df['Popularity'].idxmax()]['Name']} by {df.iloc[df['Popularity'].idxmax()]['Artist']} ({df['Popularity'].max()} popularity)")
    st.write(f"**Least popular track:** {df.iloc[df['Popularity'].idxmin()]['Name']} by {df.iloc[df['Popularity'].idxmin()]['Artist']} ({df['Popularity'].min()} popularity)")

# display a bar chart of the top 10 most popular artists in the playlist
    st.write("#### Top 10 Artists")
    st.write("The bar chart below shows the top 10 most popular artists in the playlist.")
    top_artists = df.groupby("Artists").mean().sort_values("Popularity", ascending=False).head(10)
    fig_top_artists = px.bar(top_artists, x=top_artists.index, y="Popularity", title="Top 10 Artists")
    st.plotly_chart(fig_top_artists)

# display a bar chart of the top 10 most popular songs in the playlist
    st.write("#### Top 10 Songs")
    st.write("The bar chart below shows the top 10 most popular songs in the playlist.")
    top_artistss = df.groupby("Name").mean().sort_values("Popularity", ascending=False).head(10)
    fig_top_artistss = px.bar(top_artistss, x=top_artistss.index, y="Popularity", title="Top 10 Songs")
    st.plotly_chart(fig_top_artistss)
