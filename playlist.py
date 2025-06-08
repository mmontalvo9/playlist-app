class Song:
    def __init__(self, title, artist, duration, youtube_url=None):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.youtube_url = youtube_url
        self.next = None
        self.prev = None

    def __str__(self):
        return f"'{self.title}' by {self.artist}"

import csv
import os
import random

class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current_song = None

    def is_empty(self):
        return self.head is None

    def add_song_at_end(self, title, artist, duration, youtube_url=None):
        song = Song(title, artist, duration, youtube_url)
        if self.is_empty():
            self.head = self.tail = song
        else:
            self.tail.next = song
            song.prev = self.tail
            self.tail = song

    def save_to_file(self, filename):
        try:
            with open(filename, mode='w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Title", "Artist", "Duration", "YouTube URL"])
                current = self.head
                while current:
                    writer.writerow([current.title, current.artist, current.duration, current.youtube_url or ""])
                    current = current.next
        except Exception as e:
            print(f"Error saving playlist: {e}")


