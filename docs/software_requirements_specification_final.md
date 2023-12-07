# Overview
The purpose of this software requirements document is to outline the requirements that our program must adhere to. These include functionality features and backend features. The main requirments outlined include login requirments, dashboard requirements, and analysis requirements.    

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

# Non-Functional Requirements
4. User-Friendly Interface   
   UI1: The dashboard shall load using any type of web brower.  
   UI2: The dashboard shall reformat to fit the screen size of any device.  
   UI3: The website shall allow unlimited attempts to correctly input user credentials.  
   UI4: The website shall allow unlimited attempts to correctly input user playlist link.  

5. User Security  
   US1: The website shall prompt the user and ask if they are still there after 55 minutes of being logged in.  
   US2: The website shall display the analysis for 1 hour, or until the website is closed.  
   US3: Closing the website deletes the user's access token.  
   
7. User Permissions  
   UP1: The dashboard shall collect user permissions by prompting for cookies.  

8. User Availability  
   UA1: The website shall be usable all hours and everyday.  

9. API Functionality  
   AP1: The website shall grab the user's data in realtime every login instance.  
   AP2: The website shall grab the user's playlist data in realtime every playlist link analysis.  
