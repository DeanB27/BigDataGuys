"""
Spotify Playlist Analyzer
"""
# Importing Libraries
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import re
import VibifyLocalClass as c
import time
from spotipy.oauth2 import SpotifyOAuth
import os

# Spotify app credentials from your Spotify Developer Dashboard
SPOTIPY_CLIENT_ID = '2bdfeb8580304b9fb343ff8cc8744e76'
SPOTIPY_CLIENT_SECRET = '73cbcc49de99490f821c2925c2b41419'
SPOTIPY_REDIRECT_URI = 'http://localhost:8080/'


# Real Main
def main():
    # Spotify app credentials from the Spotify Developer Dashboard
    SPOTIPY_CLIENT_ID = '2bdfeb8580304b9fb343ff8cc8744e76'
    SPOTIPY_CLIENT_SECRET = '73cbcc49de99490f821c2925c2b41419'
    SPOTIPY_REDIRECT_URI = 'http://localhost:8080/'

    st.title("Spotify Playlist Analyzer")

    # Loads the Vibify logo and displays it in the Streamlit sidebar
    image = Image.open('Vibify.png')
    st.sidebar.image(image)


    # Creates the green border style on the login and playlist buttons
    button_style = f"""
    <style>
        /* Button style */
        .stButton button {{
            background-color: transparent !important;
            color: #1DB954 !important;
            border: 2px solid #1DB954 !important; /* Green border all the time */
            transition: background-color 0.3s, border-color 0.3s, color 0.3s;
        }}

        /* Button hover style */
        .stButton button:hover {{
            background-color: #1DB954 !important; /* Green background on hover */
            color: white !important; /* White text on hover */
        }}
    </style>
    """

    # Display the custom CSS style
    st.markdown(button_style, unsafe_allow_html=True)


    try:
        playlist_name
    except NameError:
        playlist_name = st.sidebar.text_input("Enter the URL of the Spotify playlist:")



    # NEW
    playlists_dict = {}
    if st.sidebar.button("Manage Spotify Account"):
        # Spotify API credentials
        CLIENT_ID = '2bdfeb8580304b9fb343ff8cc8744e76'
        CLIENT_SECRET = '73cbcc49de99490f821c2925c2b41419'
        
        # Authenticate the user with Spotify
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(CLIENT_ID,
                CLIENT_SECRET,
                redirect_uri="http://localhost:8080/",
                scope="playlist-read-private",  # Scope for reading playlists
                show_dialog=True))

        user = sp.current_user()
        st.sidebar.success(f"Logged in as {user['display_name']}")

        # Get the playlists of the authenticated user
        playlists = sp.current_user_playlists()

        st.session_state.spotify_playlists = playlists['items']

        playlist_name = None


    # Method to pull the playlist
    def generate_analysis(playlist):
        playlist_name = playlist['external_urls']['spotify']
        return playlist_name

    # Print the contents of the session state variable and add a button for each playlist
    if 'spotify_playlists' in st.session_state:
        playlists = st.session_state.spotify_playlists
        for idx, playlist in enumerate(playlists):
            st.sidebar.write(f"{idx + 1}. {playlist['name']}")
            #st.sidebar.write(f"   External URL: {playlist['external_urls']['spotify']}")
            generate_button = st.sidebar.button(f"Generate Analysis for {playlist['name']}", key=f"generate_{idx}")
            st.sidebar.markdown("<hr style='margin: 0px;'>", unsafe_allow_html=True)
            if generate_button:
                # Call a function to generate the analysis for the selected playlist
                playlist_name = generate_analysis(playlist)
    else:
        pass

    flag = False

    # Define the desired loading bar color (Spotify green)
    loading_bar_color = "#1DB954"

    # Define the custom CSS style for the loading bar with the chosen color
    loading_bar_style = f"""
    <style>
    @keyframes loading {{
        0% {{
            width: 0%;
        }}
        100% {{
            width: 100%;
        }}
    }}

    .loading-bar {{
        width: 100%;
        background-color: #ddd;
        position: relative;
    }}

    .loading-bar div {{
        height: 4px;
        background-color: {loading_bar_color};  # Set the color here
        width: 0;
        position: absolute;
        animation: loading 2s linear infinite;
    }}
    </style>
    """

    # Display the custom CSS style
    st.markdown(loading_bar_style, unsafe_allow_html=True)
    loading_container = st.empty()


    # Instantiate the Playlist class
    if playlist_name:
        loading_container.markdown('<div class="loading-bar"><div></div></div>', unsafe_allow_html=True)
        p = c.Playlist(playlist_name)
        flag = True
        loading_container.empty()


    # If we have a valid playlist ID, proceed to fetch and display playlist data
    if flag:
        st.balloons()  # Show celebration balloons in the app
        c.run(p)
    cache_file = ".cache"
    if os.path.exists(cache_file):
        os.remove(cache_file)

if __name__ == '__main__':
    main()
