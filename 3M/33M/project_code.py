import json
import numpy as np
import pandas as pd
import spotipy 
import os
import sys


username = os.environ['SPOTIPY_CLIENT_ID']
api_key = os.environ['SPOTIPY_CLIENT_SECRET']

mood=sys.argv[1]

if mood=='angry':
    dataset_data = pd.read_csv('angry.csv')
elif mood=='happy':
    dataset_data=pd.read_csv('happy.csv')
elif mood=='sad':
    dataset_data=pd.read_csv('sad.csv')
else:
    dataset_data=pd.read_csv('happy.csv')



from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
song_cluster_pipeline = Pipeline([('scaler', StandardScaler()), 
                                  ('kmeans', KMeans(n_clusters=20, 
                                   verbose=0, n_jobs=4))],verbose=False)
X = dataset_data.select_dtypes(np.number)
number_cols = list(X.columns)
song_cluster_pipeline.fit(X)
song_cluster_labels = song_cluster_pipeline.predict(X)
dataset_data['cluster_label'] = song_cluster_labels




from collections import defaultdict
from scipy.spatial.distance import cdist
import difflib

number_cols = ['valence', 'year', 'acousticness', 'danceability', 'duration_ms', 'energy', 'explicit',
 'instrumentalness', 'key', 'liveness', 'loudness', 'mode', 'popularity', 'speechiness', 'tempo']


from spotipy.oauth2 import SpotifyClientCredentials
from collections import defaultdict

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=os.environ["SPOTIPY_CLIENT_ID"],
                                                           client_secret=os.environ["SPOTIPY_CLIENT_SECRET"]))




def find_song(name, year):
    
    song_data = defaultdict()
    results = sp.search(q= 'track: {} year: {}'.format(name,
                                                       year), limit=1)
    if results['tracks']['items'] == []:
        return None
    
    results = results['tracks']['items'][0]

    track_id = results['id']
    audio_features = sp.audio_features(track_id)[0]
    
    song_data['name'] = [name]
    song_data['year'] = [year]
    song_data['explicit'] = [int(results['explicit'])]
    song_data['duration_ms'] = [results['duration_ms']]
    song_data['popularity'] = [results['popularity']]
   
    
    for key, value in audio_features.items():
        song_data[key] = value
    
    return pd.DataFrame(song_data)




def get_song_data(song, dataset_data):
    
    """
    Gets the song data for a specific song. The song argument takes the form of a dictionary with 
    key-value pairs for the name and release year of the song.
    """
    
    try:
        song_data = dataset_data[(dataset_data['name'] == song['name']) 
                                & (dataset_data['year'] == song['year'])].iloc[0]
        return song_data
    
    except IndexError:
        return find_song(song['name'], song['year'])

        



def get_mean_vector(song_list, dataset_data):
  
    """
    Gets the mean vector for a list of songs.
    """
    
    song_vectors = []
    
    for song in song_list:
        song_data = get_song_data(song, dataset_data)
        if song_data is None:
            print('Warning: {} does not exist in Spotify or in database'.format(song['name']))
            continue
        song_vector = song_data[number_cols].values
        song_vectors.append(song_vector)  
    
    song_matrix = np.array(list(song_vectors))
    return np.mean(song_matrix, axis=0)






def flatten_dict_list(dict_list):
   
    """
    Utility function for flattening a list of dictionaries.
    """
    
    flattened_dict = defaultdict()
    for key in dict_list[0].keys():
        flattened_dict[key] = []
    
    for dictionary in dict_list:
        for key, value in dictionary.items():
            flattened_dict[key].append(value)
            
    return flattened_dict
        




def recommend_songs(song_list, dataset_data, n_songs=5):
  
    """
    Recommends songs based on a list of previous songs that a user has listened to.
    """
    
    metadata_cols = ['name', 'year', 'artists','id']
    song_dict = flatten_dict_list(song_list)
    
    song_center = get_mean_vector(song_list, dataset_data)
    scaler = song_cluster_pipeline.steps[0][1]
    scaled_data = scaler.transform(dataset_data[number_cols])
    scaled_song_center = scaler.transform(song_center.reshape(1, -1))
    distances = cdist(scaled_song_center, scaled_data, 'cosine')
    index = list(np.argsort(distances)[:, :n_songs][0])
    rec_songs = dataset_data.iloc[index]
    rec_songs = rec_songs[~rec_songs['name'].isin(song_dict['name'])]
    return rec_songs[metadata_cols].to_dict(orient='records')
recomnd_list=(recommend_songs([{'name': 'Come As You Are', 'year':1991}],  dataset_data))

recomnd_list_songs=[]
for i in range(5):
    track_id=recomnd_list[i]['id']
    track_info=sp.track(track_id)
    recomnd_list_song=(recomnd_list[i]['name'],recomnd_list[i]['year'],recomnd_list[i]['artists'],track_info['external_urls']['spotify'])
    recomnd_list_songs.append(recomnd_list_song)
print(json.dumps(recomnd_list_songs))












