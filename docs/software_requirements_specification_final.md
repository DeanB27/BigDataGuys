# Overview
The purpose of this software requirements document is to outline the requirements that our program must adhere to. These include functionality features and backend features. The main requirments outlined include the dashboard requirements, analysis requirements, accessibility requirements, as well as API connectivity requirements.  

# Functional Requirements
1. Spotify API Connectivity  
   SA1: Upon inputting a public playlist link, the program shall pull the user's playlist name.  
   SA2: Upon inputting a public playlist link, the program shall pull the user's playlist cover.  
   SA3: Upon inputting a public playlist link, the program shall pull the user's playlist description.  
   SA4: Upon inputting a public playlist link, the program shall pull the user's playlist track count.   
   SA5: Upon inputting a public playlist link, the program shall pull the user's playlist duration.   
   SA6: Upon inputting a public playlist link, the program shall pull the user's playlist tracks.   
   SA7: Upon inputting a public playlist link, the program shall pull the user's playlist track artists.   
   SA8: Upon inputting a public playlist link, the program shall pull the user's playlist track popularities.
   SA9: Upon inputting a public playlist link, the program shall pull song recommendations based on songs in the user's inputted playlist.    

3. Genre and Mood Metric Analysis  
   G1: The program shall list the percentages of each genre in the given playlist.  
   G2: The program shall use a plotly pie chart to show the percentages of each genre in the given playlist.  
   G3: The program shall filter for the genres: country, rock, rap, pop, hip-hop, jazz, soul, metal, funk, indie, techno, dubstep, alternative, folk, and consider all other        genres as "other."  
   G4: The program shall list a mood metric of your playlist, showing the percentage of each mood.  
   G5: The program shall use a plotly pie chart to show the percentages of each mood in the given playlist.  

5. Streamlit Dashboard User Interface  
   D1: The dashboard shall have a text box to paste a link to a specific Spotify playlist.    
   D2: Upon inputting a public playlist link, the dashboard shall display the user's playlist duration.    
   D3: Upon inputting a public playlist link, the dashboard shall display the user's playlist name.    
   D4: Upon inputting a public playlist link, the dashboard shall display the user's playlist cover.  
   D5: Upon inputting a public playlist link, the dashboard will display a small window that contains the songs, artists, release dates, popularities, and durations of             every song in the playlist.  
   D6: Upon inputting a public playlist link, the dashboard shall display recommended songs.  
   D7: The recommended songs will be clickable, and shall navigate the user to that song on Spotify.  

# Non-Functional Requirements
4. User-Friendly Interface   
   UI1: The dashboard shall load using any and all type's of web brower.    
   UI2: The dashboard shall reformat to fit any screen size.   
   UI3: The website shall allow unlimited attempts to correctly input user playlist link.  
   UI4: The website shall redirect the user to the Spotify website when clicking a recommended song on a computer.  
   UI5: The website shall redirect the user to the Spotify app when clicking a recommended song on a mobile device.   

5. User Availability  
   UA1: The website shall be usable all hours of everyday.  
   UA2: The website shall work with any public Spotify playlist with 1000 songs or less.  
   UA3: The website shall clear the cache after being closed.  
   UA4: The website shall reformat when loaded on a mobile device.  
   UA5: The website shall have a short domain name with the title "vibify" in it.  
    
6. API Functionality  
   AP1: The website shall grab the user's data in realtime every login instance.  
   AP2: The website shall grab the user's playlist data in realtime every playlist link analysis.  
   AP3: The website shall only have one page with a top-down view of the analysis.  
   AP4: The website shall seamlessly switch between playlists as they are inputted, without reloading the webpage.    
   AP5: The website shall take no longer than 15 seconds to load the analysis per one hundred songs in the playlist.  
