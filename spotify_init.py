# Created 29/10/2019
# Last Edited: 29/10/2019
# Author(s): Will Woodruff
# Collaborator(s): -

import requests

headers = {
    'Authorization': 'Bearer {your access token for each individual account}',
}

params = (
    ('q', 'world'),
    ('type', 'song'),
)

response = requests.get('https://api.spotify.com/v1/search', headers, params)

if response.status_code == 200:
    print('Success! We are generating your songs!')
elif response.status_code == 404:
    print('Not Found. Sorry, there wern\'t any results for that article')
else:
    print('An error occurred')