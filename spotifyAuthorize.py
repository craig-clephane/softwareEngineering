import requests
import spotipy
import spotipy.util as util


def access_key(user_id='7wxlddrk3temavvzzao5qidyu'):
    username = user_id
    scope = 'user-library-read playlist-modify-private playlist-modify-public playlist-read-private playlist-read-collaborative'
    client_id = '432ad931cf3e427084e9447c79a57835'
    client_secret = '9d07660464dd49fa84ce468bb51132d7'
    redirect_uri = 'http://localhost:8888/callback'
    token = util.prompt_for_user_token(username, scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
    print(token)
    return token
