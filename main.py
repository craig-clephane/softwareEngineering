# Using Python 3 syntax as version 2 is being deprecated at the beginning of 2020
import news_init
import spotify_init

newsHeadlines = news_init.accessNewsAPI()

for row in newsHeadlines:
    for i in row:
        spotify_init.runRequest(i)
    
