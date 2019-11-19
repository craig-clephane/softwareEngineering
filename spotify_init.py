# Created 29/10/2019
# Last Edited: 29/10/2019
# Author(s): Will Woodruff
# Collaborator(s): Craig Clephane
import datetime

import requests
import json

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer BQCFJ-e4SRAsThNu0mjSbQnwnNu_Uu63bEK3eK-yJXquRsQrqqKb-Ia-3HM4Iknq0470HADLvUcnzU-16JEO_Le1VPI0PwA9aHWTKRHHiwo-2UwZD7u6sBHYoc0wK8Ug4q4T85aUSkcwnl-T47hu52EpHQAk-aQ9aeNNOV6C59iEPyHNE-fInTNZRsOKb66PilSIq37869YJ2IhbBhpKscL4eDvPk5Ke0GB0m82c1hIgjrDRry1xIyphehhzntVCEkghxSsjxLYHOSF1nWdy_HLabnBGsA',
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
