# Created 29/10/2019
# Last Edited: 29/10/2019
# Author(s): Will Woodruff
# Collaborator(s): Craig Clephane
import datetime

import requests
import json
import spotifyAuthorize as spotauth

bearer = spotauth.accessKey()

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + bearer,
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
    data = '{"name":"' + str(datetime.date.today()) + '", "public":false}'
    response = requests.post('https://api.spotify.com/v1/users/7wxlddrk3temavvzzao5qidyu/playlists', headers=headers,
                             data=data)
    json_data = json.loads(response.text)
    playlist_id = json_data['external_urls']['spotify'].split('/')[-1]
    return playlist_id


def add_track(track, playlist):
    params = (
        ('uris', 'spotify:track:' + track),
    )

    response = requests.post(f'https://api.spotify.com/v1/playlists/{playlist}/tracks', headers=headers,
                             params=params)
    print(response)
