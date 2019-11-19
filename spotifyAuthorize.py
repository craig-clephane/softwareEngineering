import requests
import spotipy
import spotipy.util as util

params = (
        ('client_id', '432ad931cf3e427084e9447c79a57835'),
        ('response_type', 'code'),
        ('scope', ['user-read-email', 'user-follow-read']),
        ('redirect_uri', 'https://127.0.0.1:5000/spotify/callback'),
    )

def accessKey(): 
    username = '7wxlddrk3temavvzzao5qidyu'
    scope = 'user-library-read'
    client_id = '432ad931cf3e427084e9447c79a57835'
    client_secret = '9d07660464dd49fa84ce468bb51132d7'
    redirect_uri = 'http://localhost:8888/callback'
    token = util.prompt_for_user_token(username, scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
    print(token)
    return token