from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

SPOT_CLIENT_ID = 'cea71293f3e749f698ed6c1357f86540'
SPOT_CLIENT_SECRET = "a1327b853ff34754941cfd4e47c3bd6b"

# auth_manager = SpotifyClientCredentials(client_id=SPOT_CLIENT_ID, client_secret=SPOT_CLIENT_SECRET)

spotify_oauth = SpotifyOAuth(client_id=SPOT_CLIENT_ID, client_secret=SPOT_CLIENT_SECRET, redirect_uri='https://youtube.com', scope="playlist-modify-private")
# spotify = spotipy.Spotify(client_credentials_manager=spotify_oauth)

# user_id = spotify.current_user()['id']
# playlits = spotify.user_playlists(user_id)

# print(user_id)
# print(playlits)


urn = 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'
sp = spotipy.Spotify(auth_manager=spotify_oauth)

artist = sp.artist(urn)
print(artist)

user = sp.user('plamere')
print(user)
