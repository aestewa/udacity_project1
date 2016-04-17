"""

This module provides the Movie class that is used in the
entertainment_center.py module.

"""

import webbrowser


class Movie():
    def __init__(self, movie_title, poster_image, trailer):
        """
    Args:
        movie_title: The official movie title.
        poster_image: The full url for the official box art image.
        trailer: The full url for the official trailer.
            Please only use YouTube videos.

"""
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        """
    This allows the movie trailer to play after the movie's poster
    image has been clicked.

"""
        webbrowser.open(self.trailer_youtube_url)
