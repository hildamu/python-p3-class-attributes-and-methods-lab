class Song:
    count = 0
    genre_count = {}
    artist_count = {}
    genres = set()
    artists = set()

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        Song.genre_count.setdefault(self.genre, 0)
        Song.genre_count[self.genre] += 1
        Song.artist_count.setdefault(self.artist, 0)
        Song.artist_count[self.artist] += 1
        Song.genres.add(self.genre)
        Song.artists.add(self.artist)
