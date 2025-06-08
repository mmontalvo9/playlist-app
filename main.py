from flask import Flask, request, jsonify, render_template, send_file
from playlist import Playlist
import os

app = Flask(__name__)
playlist = Playlist()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/songs', methods=['GET'])
def get_songs():
    current = playlist.head
    songs = []
    while current:
        songs.append({
            'title': current.title,
            'artist': current.artist,
            'duration': current.duration,
            'youtube_url': current.youtube_url
        })
        current = current.next
    return jsonify(songs)

@app.route('/add', methods=['POST'])
def add_song():
    data = request.get_json()
    playlist.add_song_at_end(
        data['title'],
        data['artist'],
        data['duration'],
        data.get('youtube_url')
    )
    return jsonify({'message': 'Song added!'})

@app.route('/download', methods=['GET'])
def download_csv():
    filename = "playlist.csv"
    playlist.save_to_file(filename)
    return send_file(filename, as_attachment=True)

# ✅ Updated for Render compatibility
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

