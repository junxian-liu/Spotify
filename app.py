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
    return render_template('index.html', song = song)

if __name__ == '__main__':
    app.run(debug=True)