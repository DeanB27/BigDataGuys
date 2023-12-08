# Big Data Guys

This Github repo contains our Spotify playlist analyzer (Vibify). In this analyzer we implemented a way to link 
your Spotify playlist to our analyzer, which returns an analysis of the songs in your playlist by genre, mood, and popularity. We also 
gave a style rating to the user's playlist such as "happy" or "sad" depending on the vibe of the 
playlist. In addition to this, we implemented a system that creates a list of recommendations with similar songs to the inputted 
playlist. We hosted this program via a Streamlit website where people can copy and paste their spotify 
playlist links directly into the website. 

## Team Members

* [Dean Berg](https://github.com/DeanB27/CIS350-HW2-Berg)
* [Clay Beal](https://github.com/clayster4004/CIS350-HW2-Beal)
* [Ian McCourt](https://github.com/ianmccourt/CIS350-HW2-McCourt)
* [Aaron Dies](https://github.com/diesat/CIS350-HW2-Dies)

## Prerequisites
### FOR PUBLIC VERSION:
* You will need a stable internet connection.
* You will need a link to a public Spotify playlist.

### FOR LOCAL VERSION:
* You will need a python IDE of your choosing.
* You will need Python 3 installed.
* You will need to install the Streamlit, Plotly, Pandas, and Spotipy python libraries.
* You will need both the main and class python files, and the vibify logo in the same directory.

## Run Instructions
### FOR PUBLIC VERSION:
* Go to the website link. [Vibify](https://vibify.streamlit.app/)
* You then need to copy and paste your Spotify link into the side bar and hit enter.

### FOR LOCAL VERSION:
* Put the vibify png, the localmain, and localclass python files in the same directory in your IDE.
* Download the Streamlit, Plotly, Pandas, and Spotipy python libraries, using "pip install "library-name"".
* In the directory terminal, type streamlit run localmain.py" and hit enter.
