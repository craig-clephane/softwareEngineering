# Created 29/10/2019
# Last Edited: 29/10/2019
# Author(s): Will Woodruff
# Collaborator(s): Craig Clephane

import requests
import json

headers = {
    #'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer BQA7KQzRzrqzEGDLSYR2nMdQR_MKMxnCSJVS80M9lxy5nNofgm8FASq5QQilk_fl3Mx3wWYRnYkjbNsI-1AJe0BNVUWy0VlJVSHu6OBqi-zWVc4KOdfhyRF_sJPwbvQQMO54he5aWULguPthJtbvO28MO7U0HPpQksPaUUm9olXOUZuwul_irqd3Y2m5Hyg',
}


def runRequest(value):

    params = (
        ('q', value),
        ('type', 'track'),
    )

    response = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params)
    json_data = json.loads(response.text)

    if response.status_code == 200:
        print('Success! We are generating your songs!')
        #print(json_data)
    elif response.status_code == 404:
        print('Not Found. Sorry, there wern\'t any results for that article')
    else:
        print('An error occurred -', response.status_code)

    song = json_data["tracks"]["items"][0]["album"]['id']
    #print(song)
    return song


def createplaylist():
    data = '{"name":"A New Playlist", "public":false}'
    response = requests.post('https://api.spotify.com/v1/users/7wxlddrk3temavvzzao5qidyu/playlists', headers=headers, data=data)
    print(response)


def addtrack(track):
    params = (
    ('uris', 'spotify:track:',track )
)

    response = requests.post('https://api.spotify.com/v1/playlists/7aEjvDQ1eCifCjOrHoqQNi/tracks', headers=headers, params=params)
    print(response)

    
song = runRequest("hi")
print(song)
addtrack(song)
