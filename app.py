from flask import Flask, request, render_template
import main

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def getValue():
    artist = request.form["artist"].upper()
    token = main.getToken()
    artist_id = main.searchArtists(token, artist)
    song = main.get_songs_by_artist(token, artist_id)
    similar_artists = main.get_genre(artist_id)
    link = main.generate_spotify_link(artist)
    statement = "Your artist top song is {song}, and similar artists to your artist is {similar_artisits[0]}, {similar_artisits[1]}, and {similar_artisits[2]}. Their spotify link is {link}"
    return render_template('index.html', song = statement)

if __name__ == '__main__':
    app.run(debug=True)