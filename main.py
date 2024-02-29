import config
import os 
import base64
from requests import post, get
import json

client_id = config.CLIENT_ID
client_secret = config.CLIENT_SECRET

def getToken():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"

    headers = {
        "Authorization": "Basic " + auth_base64, 
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "grant_type": "client_credentials"
    }

    result = post(url, headers = headers, data = data)

    json_results = json.loads(result.content)

    token = json_results['access_token']

    return token

def getHeader(token):
    return {"Authorization": "Bearer" + token}

def searchArtists(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = getHeader(token)

    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query
    result = get(query_url, headers = headers)
    json_result = json.loads(result.content)["artists"]["items"]

    if len(json_result) == 0:
        print('No artist with that name!')
        return None

    return json_result[0]

def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = getHeader(token)
    result = get(url, headers = headers)
    json_result = json.loads(result.content)["artists"]["items"]

    return json_result[0]

def get_genre(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/genre?country=US"
    headers = getHeader(token)
    result = get(url, headers = headers)
    json_result = json.loads(result.content)["artists"]["items"]

    return json_result[0]