import webbrowser

class Movie():
	
"""A constructor is defined. This constructor is called whenever a new instace of the class is created.
Attributes:
        title: Title of the movie
        storyline: Story Line of the movie
        poster_image_url: Pointer to the movie poster.
        trailer_youtube_url: Pointer to the official movie trailer on YouTube."""
   
def __init__(self, movie_title , movie_storyline, poster_image, trailer_youtube):
    self.title = movie_title
    self.storyline = movie_storyline
    self.poster_image_url = poster_image
    self.trailer_youtube_url = trailer_youtube

def show_trailer(self):
    webbrowser.open(self.trailer_youtube_url)
    """Plays the embedded YouTube video."""

def show_poster(self):
    webbrowser.open(self.poster_image_url)
    """ Shows the embedded poster image. """
                 
        
