# AIzaSyBn6SBnBd1Ru36L1lKLSW7WD9gCEt8vqRk

from lyrics_extractor import SongLyrics

extract_lyrics = SongLyrics("AIzaSyBn6SBnBd1Ru36L1lKLSW7WD9gCEt8vqRk","ac7f664d971914e3f")

song = extract_lyrics.get_lyrics("I swear there was lightning coming from your eyes Starting a fire in a hotel room")


print(song['title'])