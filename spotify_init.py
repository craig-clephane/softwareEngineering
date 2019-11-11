# Created 29/10/2019
# Last Edited: 29/10/2019
# Author(s): Will Woodruff
# Collaborator(s): Craig Clephane

import requests
import json

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer BQC9m22cm2mOFnfBYTrewC8xAsq2I0l0OsViJW6cxXa-iWZoWS2mBov4iXoLZVyolwzVzjslqNqS_Kyi6YMuFCRQB3aLZ8Wssj4342cUmUsZ_CVrqy_EOHianO5qLsDSwKF_oDC3Z_ydXITGGv-V08wcFi35yJo',
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
        print(json_data)
    elif response.status_code == 404:
        print('Not Found. Sorry, there wern\'t any results for that article')
    else:
        print('An error occurred -', response.status_code)


def createplaylist():
    data = '{"name":"Test", "public":false}'
    requests.post('https://api.spotify.com/v1/users/7wxlddrk3temavvzzao5qidyu/playlists', headers=headers, data=data)

createplaylist()
