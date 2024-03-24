import requests


class GiphyAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.giphy.com/v1"

    def get_trending_gifs(self, limit=5):

        # response = requests.get(api_key)
        link = f"https://api.giphy.com/v1/gifs/trending?api_key={self.api_key}&limit={limit}&offset=0&rating=g"
        data = requests.get(link)
        data = data.json()
        # print(data)
        return data.get("data", [])

    def get_search_results(self, count, query):
        link = f"https://api.giphy.com/v1/gifs/search?api_key={self.api_key}&q={count}&limit={query}&offset=0&rating=g"
        # print(link)
        data = requests.get(link)
        data = data.json()
        # print(data)

        return data.get("data", [])
