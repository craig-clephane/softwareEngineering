#Created 23/10/2019
#Last Edited: 04/11/2019
#Author(s): Craig Clephane
#Collaborator(s): -

from newsapi import NewsApiClient
import requests

articleTitles = []

def accessNewsAPI():
       ## Contains API key for project 
       # newsapi = NewsApiClient(api_key='96113538df2a451caefde995afc26143')

       ## Makes a HTTP Request for content within the US
       url = ('https://newsapi.org/v2/top-headlines?'
              'country=gb&'
              'apiKey=96113538df2a451caefde995afc26143')
       
       ## Stores content inside variable 
       response = requests.get(url).json()
       printsContent(response)

def printsContent(response): 
       i = 0
       while i < 20:
              print (response['articles'][i]['title'])
              storeArray(response['articles'][i]['title'])
              i = i+1

def storeArray(response):
       articleTitles.append(response)
       
def returnTitles():
       return articleTitles


accessNewsAPI()
