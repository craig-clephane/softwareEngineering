#Created 23/10/2019
#Last Edited: 04/11/2019
#Author(s): Craig Clephane
#Collaborator(s): -

from newsapi.newsapi_client import NewsApiClient
import requests
stop_dir = "SmartStoplist.txt"
from rake_nltk import rake
import operator

articleTitles = []
keywordsArray = []

def accessNewsAPI():
       ## Contains API key for project 
       # newsapi = NewsApiClient(api_key='96113538df2a451caefde995afc26143')

       ## Makes a HTTP Request for content within gb
       url = ('https://newsapi.org/v2/top-headlines?'
              'country=gb&'
              'apiKey=96113538df2a451caefde995afc26143')
       
       ## Stores content inside variable 
       response = requests.get(url).json()
       printsContent(response)
       return keywordsArray

def printsContent(response): 
       i = 0
       while i < 20:
              print (response['articles'][i]['title'])
              storeArray(response['articles'][i]['title'])
              i = i+1

def storeArray(response):
       global articleTitles
       articleTitles.append(response)
       phrases(response)
       
       
def returnTitles():
       return articleTitles

def phrases(response):
       global keywordsArray
       rake_object = rake.Rake(stop_dir)
       rake_object.extract_keywords_from_text(response)
       #print(rake_object.get_ranked_phrases()) 
       keywords = rake_object.get_ranked_phrases()
       #print(keywords)
       keywordsArray.append(keywords)

#accessNewsAPI()
#print(keywordsArray)







