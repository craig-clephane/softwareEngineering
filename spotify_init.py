# Created 29/10/2019
# Last Edited: 29/10/2019
# Author(s): Will Woodruff
# Collaborator(s): Craig Clephane

import requests
import json

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer BQC9TAewts1UyNAasOuHx9QSuNUYPHafL_Nomai9ViZar9PbNlmvnsPaOUMIym8gIYKOav96ZEGpQUWZE4FgqkPgHCJ0sGW3XCvomScpA3j7wsUycAzBiJbAZ4YtO3BXRUd5iZ9KL3NiMqrE0KChNfOB5793YRuuyg',
}

params = (
    ('q', 'winner'),
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