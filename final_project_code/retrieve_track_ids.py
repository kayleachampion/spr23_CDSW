import spotipy 

from spotify_authentication import SPOTIPY_CLIENT_ID
from spotify_authentication import SPOTIPY_CLIENT_SECRET

from spotipy.oauth2 import SpotifyClientCredentials 

def retrieve_track_ids(spotify_playlist_id, track_id_file_name)

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET))

#retrieving track id's for current playlist
results = spotify.playlist_tracks(spotify_playlist_id)

items = results['items']

track_list = track_id_file_name

with open(track_list, 'w') as output_file:

    for item in items:
        track_data = item['track']
        track_id = track_data['id']
    
        print(track_id, file=output_file)