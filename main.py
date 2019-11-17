# Using Python 3 syntax as version 2 is being deprecated at the beginning of 2020
import news_init
import spotify_init

newsHeadlines = news_init.access_news_api()

for row in newsHeadlines:
    for i in row:
        song = spotify_init.run_request(i)
        if song is not None: 
            spotify_init.add_track(song)
