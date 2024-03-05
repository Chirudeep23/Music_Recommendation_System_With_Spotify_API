#Importing Necessary Modules
import pickle #For Retrieving The Dumped Data
import streamlit as st #For Making Web Application
import pandas as pd #For Data Preprocessing
import spotipy #For Using Spotify WebAPI
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = "29791f64a313460cb86847cebe657fdb"
CLIENT_SECRET = "65ba145aad86400d8cc4f2b42801a672"

# Initializing the Spotify client ID & client Secret
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#Definig a function which searches for a song's album cover URL using the Spotify API
def get_song_album_cover_url(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=search_query, type="track")
    if results and results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        album_cover_url = track["album"]["images"][0]["url"]
        print(album_cover_url)
        return album_cover_url
    else:
        return "https://i.postimg.cc/XNC7tmCT/Designer.png"
#Defining function which recommends similar songs to the input song based on the calculated similarity scores
def recommend(song):
    index = music[music['song'] == song].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_music_names = []
    recommended_music_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        artist = music.iloc[i[0]].artist
        print(artist)
        print(music.iloc[i[0]].song)
        recommended_music_posters.append(get_song_album_cover_url(music.iloc[i[0]].song, artist))
        recommended_music_names.append(music.iloc[i[0]].song)

    return recommended_music_names,recommended_music_posters

st.header('Music Recommendation System')
#Loading The Dumped Pickle File into Webapp
music = pickle.load(open('df.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

#Creating a dropdown menu for selecting songs from the dataset
music_list = music['song'].values
selected_movie = st.selectbox("Select Music From The Dropdown Menu",music_list)
#Creating a button for showing the output of recommended songs
if st.button('Recommend Me The Music'):
    recommended_music_names,recommended_music_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5= st.columns(5)
    with col1:
        st.text(recommended_music_names[0])
        st.image(recommended_music_posters[0])
    with col2:
        st.text(recommended_music_names[1])
        st.image(recommended_music_posters[1])
    with col3:
        st.text(recommended_music_names[2])
        st.image(recommended_music_posters[2])
    with col4:
        st.text(recommended_music_names[3])
        st.image(recommended_music_posters[3])
    with col5:
        st.text(recommended_music_names[4])
        st.image(recommended_music_posters[4])
        
#Customization of Webpage

# Define the background image URL
background_image = "https://i.postimg.cc/mgqh9K0h/Music-recommendation-system.jpg"

# Adding a style block with the background image
st.markdown(f"""
<style>
.stApp {{
    background-image: url("{background_image}");
    background-size: cover;
}}
</style>
""", unsafe_allow_html=True)

st.caption('_Developed By Chirudeep Amaraju_')
st.subheader('Contact', divider='grey')
#Customisation of Contact icons
col1, col2, col3, col4 = st.columns(4)
with col1:
        st.link_button("GitHub", "https://github.com/Chirudeep23")
with col2:
        st.link_button("LinkedIn", "https://www.linkedin.com/in/chirudeep-amaraju-74aa6b259/")
with col3:
        st.link_button("Instagram","https://www.instagram.com/chirudeep_23/")
with col4:
        st.link_button("Download Dataset","https://www.kaggle.com/datasets/notshrirang/spotify-million-song-dataset")
