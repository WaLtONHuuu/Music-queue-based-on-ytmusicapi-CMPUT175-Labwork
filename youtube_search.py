

# Import time format change function from utils.py, import Song class from song.py, import ytmusicapi from YTMusic;
# using ytmusicapi search song information and adjust
# Author: Chen Hu
# When: May 22, 2026


from song import Song
from utils import time_to_seconds
from ytmusicapi import YTMusic

def extract_artists(song_info):
    """
    Input: information of the song as originally retrieved in dictionary
    Returns: all artists involved in the song as a string; or "NA" if there is no artist info
    Working: makes sure that all artists involved in a song show up in the final representation
    """
    if song_info["artists"] != None:
        artists=song_info["artists"]
    else:
        artists=None
    names=[]
    if artists != None:
        for name in artists:
            names.append(name["name"])
        return ", ".join(names)
    else:
        return "NA"

def song_search(query):
    """
    Input: search query
    Returns: top 5 results
    Working: use search method from YTMusic, returns the top 5 results
    """
    ytmusic = YTMusic()
    results = ytmusic.search(query, filter="songs")
    return results[0:5]


def filter_info(results):
    """
    Input: search results in a JSON like format
    Returns: list of Song Objects
    Working: extract information from JSON, create Song objects, append into a list; raise exception as error occur
    """
    songs=[]
    try:
        for result in results:
            title=result["title"]
            artists=extract_artists(result)
            duration_seconds=time_to_seconds(result["duration"])
            song = Song(title, artists, duration_seconds)
            songs.append(song)
    except Exception:
        raise Exception("Invalid song info")
    return songs