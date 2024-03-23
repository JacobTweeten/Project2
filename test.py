import unittest
import requests
from giphy_api import GiphyAPI
from giphy_cli import GiphyCLI

class testing(unittest.TestCase):
    def setUp(self):
        self.api_key = "***REMOVED***"
        self.cli = GiphyCLI(self.api_key)

    #Testing Trending functionality
    def test_trending_default_count(self):
        gifs = self.cli.trending()
        self.assertEqual(len(gifs), 5)

    def test_trending_custom_count(self):
        count = 10
        gifs = self.cli.trending(count)
        self.assertEqual(len(gifs), count)

    #Testing search functionality
    def test_search_default_count(self):
        query = "hello"
        count=5
        gifs = self.cli.search(count, query)
        self.assertEqual(len(gifs), 5)

    def test_search_custom_count(self):
        query = "hello"
        count = 10
        gifs = self.cli.search(count, query)
        self.assertEqual(len(gifs), count)



    #Testing search
    



if __name__ == "__main__":
    unittest.main()
