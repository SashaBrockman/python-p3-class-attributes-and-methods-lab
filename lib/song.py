class Song:
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.add_song_to_count()
        if not self.has_genre(genre):
            self.add_genre(genre)
        if not self.has_artist(artist):
            self.add_artist(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)
        self.name = name
        self.artist = artist
        self.genre = genre
    
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_genre(cls, genre):
        cls.genres.append(genre)

    @classmethod
    def has_genre(cls, genre):
        return genre in cls.genres

    @classmethod
    def add_artist(cls, artist):
        cls.artists.append(artist)

    @classmethod
    def has_artist(cls, artist):
        return artist in cls.artists

    @classmethod
    def add_to_genre_count(cls, genre):
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artist_count(cls, artist):
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1