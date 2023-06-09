import json
import pandas as pd

#building our function
def build_songs_dataframe(audio_features_filename):

    songs = []
    with open(audio_features_filename, "r") as input_file:
        for line in input_file.readlines():
            song_features = json.loads(line)[0]
            songs.append(song_features)
        
    return pd.DataFrame(songs)