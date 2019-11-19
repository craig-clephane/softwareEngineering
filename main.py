# Using Python 3 syntax as version 2 is being deprecated at the beginning of 2020
import news_init
import spotify_init
from tkinter import *
from tkmacosx import Button
import webbrowser
import spotifyAuthorize as spotauth


def open_url(url):
    webbrowser.open("https://open.spotify.com/playlist/" + url)


def run_program():
    lbl.configure(text="Your playlist is being generated...")
    user_id = e1.get()
    playlist_name = e2.get()
    print(user_id)
    bearer = spotauth.access_key(user_id)
    news_headlines = news_init.access_news_api()
    playlist_id = spotify_init.create_playlist(bearer, user_id, playlist_name)
    for row in news_headlines:
        for keyword in row:
            song = spotify_init.run_request(bearer, keyword)
            if song is not None:
                spotify_init.add_track(bearer, song, playlist_id)
    lbl.configure(text="Your playlist has been generated! :)")
    btn.configure(text="Click to Open", command=lambda: open_url(playlist_id))


window = Tk()

window.geometry("480x250")
window.configure(background='#2B2722')
# Creates the size of the window
window.title("Spotify News Playlist Generator")
# Adds a title to the Windows GUI for the window

heading = Label(window, text=" Hello, welcome to the Spotify Playlist generator. \n", font=("Arial Bold", 20),
                fg='#fff', bg='#2B2722')

Label(window, text="Spotify Username", fg='#fff', bg='#2B2722').grid(row=1)
Label(window, text="Playlist Name (Optional)", fg='#fff', bg='#2B2722').grid(row=3)

e1 = Entry(window)
e2 = Entry(window)


e1.grid(row=2, column=0)
e2.grid(row=4, column=0)

lbl = Label(window,
            text="We will get the latest news and match them to the Spotify library \n to generate you the songs of the day!\n",
            fg='#fff', bg='#2B2722')

heading.grid(column=0, row=0)
lbl.grid(column=0, row=5)

btn = Button(window, text="Click Me to Generate", bg="#68DA8F", fg="#fff", command=run_program)

btn.grid(column=0, row=6)

window.mainloop()
