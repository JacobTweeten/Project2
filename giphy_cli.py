import unittest
from giphy_api import GiphyAPI 

class GiphyCLI:
    def __init__(self, api_key):
        self.api = GiphyAPI(api_key)

    def trending(self, count=5):
        gifs = self.api.get_trending_gifs(count)
        return gifs

