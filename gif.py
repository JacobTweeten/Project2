#GIPHY_API_KEY=gtTp4Z8gedifHYvlsv2V5ciQWO08jO3s poetry run python gif.py trending --count 3

import os
import click
from giphy_cli import GiphyCLI

# call GiphyCLI with API key
api_key = os.environ.get("GIPHY_API_KEY")
giphy_cli = GiphyCLI(api_key)

@click.group()
def gif():
    print("hello from giphy cli!")


@gif.command()
@click.option('--count', default=5, help='Number of trending GIFs to retrieve.') #option to request certain number of gifs, and added a help message
def trending(count):
    # Calling on GiphyCLI's trending method
    gifs = giphy_cli.trending(count)
    for x in range(count):
        gif = gifs[x]
        gif_url = f"{gif['title']} ({gif['bitly_gif_url']})"
        print(f"{x+1}) {gif_url}")

@gif.command()
@click.option('--count', default=5, help='Number of search results to retrieve')
@click.argument('query', required=False, type=str)
def search(count, query):
    if query is None: #Could not find a better way to check for a query with click, so I use this statement
        print("Please provide a search query.")
        return

    #print("search subcommand called!")
    gifs = giphy_cli.search(count, query)
    
    if gifs is None:
        print("No GIFs found for the provided query.")
        return

    for x in range(count):
        gif = gifs[x]
        gif_url = f"{gif['title']} ({gif['bitly_gif_url']})"
        print(f"{x+1}) {gif_url}")

if __name__ == "__main__":
    gif()