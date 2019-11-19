# Created 23/10/2019
# Last Edited: 04/11/2019
# Author(s): Craig Clephane
# Collaborator(s): - Will Woodruff

from newsapi.newsapi_client import NewsApiClient
import requests
from rake_nltk import rake

stop_dir = "SmartStoplist.txt"

articleTitles = []
keywordsArray = []


def access_news_api():
    # Contains API key for project
    # newsapi = NewsApiClient(api_key='96113538df2a451caefde995afc26143')

    # Makes a HTTP Request for content within gb
    url = ('https://newsapi.org/v2/top-headlines?'
           'country=gb&'
           'apiKey=96113538df2a451caefde995afc26143')

    # Stores content inside variable
    response = requests.get(url).json()
    prints_content(response)
    return keywordsArray


def prints_content(response):
    i = 0
    while i < 20:
        res = response['articles'][i]['title'].split("-")[0]
        print(res)
        store_array(res)
        i = i + 1


def store_array(response):
    global articleTitles
    if response not in articleTitles:
        articleTitles.append(response)
    phrases(response)


def phrases(response):
    global keywordsArray
    rake_object = rake.Rake(stop_dir)
    rake_object.extract_keywords_from_text(response)
    # print(rake_object.get_ranked_phrases())
    keywords = rake_object.get_ranked_phrases()
    # print(keywords)
    keywordsArray.append(keywords)


# access_news_api()
# print(keywordsArray)
