import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://ws.audioscrobbler.com/2.0/"


def request_lastfm(method):
    params={
        'method': method,
        'api_key': API_KEY,
        'format': 'json'
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code != 200:
        raise Exception(f"ERROR: {response.status_code}")
    
    return response.json()

def request_geo_lastfm(method, country):
    params={
        'method': method,
        'country': country,
        'api_key': API_KEY,
        'format': 'json'
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code != 200:
        raise Exception(f"ERROR: {response.status_code}")
    
    return response.json()
    

def get_chart_top_artists():
    return request_lastfm("chart.gettopartists")

def get_chart_top_tracks():
    return request_lastfm("chart.getTopTracks")

def get_geo_top_artists():
    return request_geo_lastfm("geo.getTopArtists", 'brazil')

def get_geo_top_tracks():
    return request_geo_lastfm("geo.getTopTracks", 'brazil')

# test:
# print(get_geo_top_tracks())
