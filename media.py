import webbrowser as web


class Movie():
    '''Contains Instance Variable : title, storyline, poster_image_url, trailer_youtube_url '''
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        web.open(self.trailer_youtube_url)
