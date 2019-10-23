#Created 23/10/2019
#Last Edited: 23/10/2019
#Author(s): Craig Clephane
#Collaborator(s): -

from newsapi import NewsApiClient
import requests

## Contains API key for project 
newsapi = NewsApiClient(api_key='96113538df2a451caefde995afc26143')

## Makes a HTTP Request for content within the US
url = ('https://newsapi.org/v2/top-headlines?'
       'country=us&'
       'apiKey=96113538df2a451caefde995afc26143')
       
## Stores content inside variable 
response = requests.get(url)

## Prints Latest news in the form for a json string 
print (response.json())
