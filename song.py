

# Import time format change function from utils.py, create Song class
# Author: Chen Hu
# When: May 22, 2026


from utils import seconds_to_time_format

class Song:
    def __init__(self, name, artist, dur):
        """
        Input: Name of the song, Artist of the song, Duration of the song
        Returns: None
        Working:
        This function initializes the Song object with the name, artist, and duration
        """
        assert type(name) == str
        assert type(artist) == str
        assert type(dur) == int

        self.name = name
        self.artist = artist
        self.duration = dur

    def get_name(self):
        """
        Input: None
        Returns: Name of the song
        """
        return self.name

    def get_artist(self):
        """
        Input: None
        Returns: Artist of the song
        """
        return self.artist

    def get_duration(self):
        """
        Input: None
        Returns: Duration of the song
        """
        return self.duration

    def __str__(self):
        """
        Input: None
        Returns: String representation of the song
        """
        return f"{self.name}\n   Artists: {self.artist}\n   Duration: {seconds_to_time_format(self.duration)}"