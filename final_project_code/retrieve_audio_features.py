import json
import spotipy 

from spotify_authentication import SPOTIPY_CLIENT_ID
from spotify_authentication import SPOTIPY_CLIENT_SECRET

from spotipy.oauth2 import SpotifyClientCredentials 


def retrieve_audio_features(track_id_file_name, track_audio_features_file_name):

    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID,       client_secret=SPOTIPY_CLIENT_SECRET))

    with open(track_audio_features_file_name, 'w') as output_file:
    
        with open(track_id_file_name, 'r') as f:

            for id in f:
                id = id.replace('\n', '')   #taking off the appended new line in the list of id's

                #retrieve audio features of current track
                results_features = spotify.audio_features(id)
            
                print(json.dumps(results_features), file = output_file)
                
    return