# Created 29/10/2019
# Last Edited: 29/10/2019
# Author(s): Will Woodruff
# Collaborator(s): Craig Clephane

import requests
import json

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer BQBz0dl-5IUhuX9GBiqSkY4PBw_feRjYox3s8uimXPwkUbrtifLmAy1yIyZGI3bBKxI32OZxjASxizegJdGcF38XLx9fJ_GvIGXoXjKqOsJyMv5mNV6kbTjxJvqb7x9eMA0GIg3BPXRjWDTuIXZr9_hTcUlAv6l1johypMxaPGI5D8vi1FmWhbqBU9cPr4C9RBbQheQpg_bzBSJI3Gy9GiZbaPz7miHRLHU56iLS-jhp7Nqw2RXygd1hxdaaWjYXOorqqbLWfm3TljYAvPjp_g4voP1aAA',
}


def run_request(value):
    params = (
        ('q', value),
        ('type', 'track'),
    )

    response = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params)
    json_data = json.loads(response.text)

    if response.status_code == 200:
        print('Success! We are generating your songs!')
        print(json_data)

    elif response.status_code == 404:
        print('Not Found. Sorry, there wern\'t any results for that article')
    else:
        print('An error occurred -', response.status_code)

    print(len(json_data["tracks"]["items"]))
    if len(json_data["tracks"]["items"]) is not 0:
        song = json_data["tracks"]["items"][0]["id"]
        print(song)
        return song


def create_playlist():
    data = '{"name":"A New Playlist", "public":false}'
    response = requests.post('https://api.spotify.com/v1/users/7wxlddrk3temavvzzao5qidyu/playlists', headers=headers,
                             data=data)
    print(response)


def add_track(track):
    params = (
        ('uris', 'spotify:track:' + track),
    )

    response = requests.post('https://api.spotify.com/v1/playlists/1HsXvdPOcUvIsamfEMxuaM/tracks', headers=headers,
                             params=params)
    print(response)
