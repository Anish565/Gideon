import requests
import spotipy
from spotipy import util
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import time
import gspread
import datetime
import json
SPOTIFY_CLIENT_ID = "b9b3a98399714684b74d8b7112c7f461"
SPOTIFY_CLIENT_SECRET = "97b459bf5ab148e0aaac6efcbeb8dde7"
SPOTIFY_REDIRECT_URI = "http://127.0.0.1:9090"
SCOPE = "user-top-read user-read-playback-state user-read-currently-playing"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,client_secret=SPOTIFY_CLIENT_SECRET,redirect_uri=SPOTIFY_REDIRECT_URI,scope=SCOPE))
# token = util.prompt_for_user_token("Anizz@565",SCOPE)
# if token:
    
#     devices = sp.devices()
#     print(devices)
# else:
#     print("can't get token for Anizz@565")
#     exit()
devices = sp.devices()

print(devices)

print(json.dumps(devices, sort_keys=True, indent=4))
deviceID = devices['devices'][0]['id']

print(deviceID)


top_tracks_shorts = sp.current_user_top_tracks(limit=20, offset=0,time_range="short_term")
# print(type(top_tracks_shorts))

# The song ids are retrieved 
def getTrackIds(time_frame):
    track_ids = []
    for song in time_frame['items']:
        track_ids.append(song['id'])
    return track_ids

track_ids = getTrackIds(top_tracks_shorts)
# print(track_ids)

T1 = track_ids[1]

searchResults = sp.search("BB ki vines",5,0,"artist")
# print(searchResults)
print(searchResults['artists']['items'][-1]['uri'])

# Info about the Song 
def getTrackFeatures(id):
    meta = sp.track(id)
    name = meta['name']
    album = meta['album']['name']
    artist = meta['album']['artists'][0]['name']
    spotify_url = meta['external_urls']['spotify']
    album_cover = meta['album']['images'][0]['url']
    uri = meta['uri']
    track_info = [name,album,artist,spotify_url,album_cover]
    return track_info

# print(getTrackFeatures(T1))

# sp.start_playback(deviceID,None,searchResults['artists']['items'][-1]['uri'])

# get the list of the Songs details
def getAllData(trackIds):
    tracks = []
    for i in range(len(trackIds)):
        time.sleep(.5)
        track = getTrackFeatures(trackIds[i])
        tracks.append(track)
    return tracks

tracksData = getAllData(track_ids)


dataFrame = pd.DataFrame(tracksData, columns=['name','albums','artist','spotify_url','album_cover'])
# print(dataFrame.head(5))


# gc = gspread.service_account(filename='')