import webbrowser
import spotipy
import requests
from spotipy import client
from spotipy.oauth2 import SpotifyOAuth
import pandas

SPOTIPY_CLIENT_ID="b9b3a98399714684b74d8b7112c7f461"
SPOTIPY_CLIENT_SECRET="97b459bf5ab148e0aaac6efcbeb8dde7"
SPOTIPY_REDIRECT_URI="http://127.0.0.1:9090"
SCOPE = "user-top-read "
artist_name = []
track_name = []
popularity = []
track_id = []
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET,redirect_uri=SPOTIPY_REDIRECT_URI,scope=SCOPE))

def getTracks(timeF):
    for i,t in enumerate(timeF['tracks']['items']):
        artist_name.append(t['artists'][0]['name'])
        track_name.append(t['name'])
        track_id.append(t['id'])
        popularity.append(t['popularity'])
        # return tracks

name = []
album = []
artist = []
spotify_url = []
# album_cover = []
# track_info = []
def get_track_features(id):
    meta = sp.track(id)
    # meta
    name.append(meta["name"])
    album.append(meta["album"]["name"])
    artist.append(meta["album"]["artists"][0]["name"])
    spotify_url.append(meta["external_urls"]["spotify"])
    # album_cover.append(meta["album"]["images"][0]["url"])
    # track_info.append([name, album, artist, spotify_url, album_cover])
    # return track_info

def topCharts():
    top_tracks_short = sp.current_user_top_tracks(limit=10, offset=0, time_range="short_term")
    # print(top_tracks_short)
    track_ids = []
    for song in top_tracks_short["items"]:
        track_ids.append(song["id"])
    return track_ids


def searchSong(name):
    search = sp.search(name,type="track")
    # print(search)
    getTracks(search)
    data_set = {'Artist':artist_name,'Song':track_name,'id':track_id,'Popularity':popularity}
    df = pandas.DataFrame(data_set)
    # print(df)

query = 'darde disco'
searchSong(query)
print(sp.track(track_id[0]))
for id in track_id:
    get_track_features(id)

# dataSet = {'name':name,'album':album,'artist':artist,'URL':spotify_url,'cover':album_cover}
dataSet = {'name':name,'album':album,'artist':artist,'URL':spotify_url}

# sp.start_playback()

dtable = pandas.DataFrame(dataSet)
# for i in spotify_url:
#     webbrowser.open(i)
# print(dtable)
# print(artist_name)
# print(track_name)
# print(track_id)
# print(popularity)

