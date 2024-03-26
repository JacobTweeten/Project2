import os

import click

from giphy_cli import GiphyCLI

# call GiphyCLI with API key
api_key = os.environ.get("GIPHY_API_KEY")
giphy_cli = GiphyCLI(api_key)


@click.group(help="CLI for requesting GIFs from Giphy.")
def gif():
    pass


@gif.command()
@click.option(
    "--count", default=5, help="Number of trending GIFs to retrieve."
)  # option to request certain number of gifs, and added a help message
@click.option(
    "--markdown",
    is_flag=True,
    default=False,
    help="Returns GIFs in markdown image format.",
)
@click.option("--lucky", is_flag=True, default=False, help="Returns a single GIF")
def trending(count, markdown, lucky):
    # Calling on GiphyCLI's trending method
    gifs = giphy_cli.trending(count)

    if lucky:
        gif = gifs[1]
        gif_url = f"{gif['title']} ({gif['bitly_gif_url']})"
        if markdown:
            gif_url = f"![{gif['title']}]({gif['images']['original']['url']})"

        print(gif_url)
        exit()

    for x in range(count):
        gif = gifs[x]

        if markdown:
            gif_url = f"![{gif['title']}]({gif['images']['original']['url']})"
        else:
            gif_url = f"{gif['title']} ({gif['bitly_gif_url']})"
        print(f"{x+1}) {gif_url}")


@gif.command()
@click.option("--count", default=5, help="Number of search results to retrieve")
@click.argument("query", required=False, type=str)
@click.option(
    "--markdown",
    is_flag=True,
    default=False,
    help="Returns GIFs in markdown image format.",
)
@click.option("--lucky", is_flag=True, default=False, help="Returns a single GIF")
def search(count, query, markdown, lucky):
    if query is None:
        # Could not find a better way to check for a query with click, so I use this statement
        print("Please provide a search query.")
        return

    # print("search subcommand called!")
    gifs = giphy_cli.search(count, query)

    if gifs is None:
        print("No GIFs found for the provided query.")
        return

    if lucky:
        gif = gifs[1]
        gif_url = f"{gif['title']} ({gif['bitly_gif_url']})"
        if markdown:
            gif_url = f"![{gif['title']}]({gif['images']['original']['url']})"

        print(gif_url)
        exit()

    for x in range(count):
        gif = gifs[x]

        if markdown:
            gif_url = f"![{gif['title']}]({gif['images']['original']['url']})"
        else:
            gif_url = f"{gif['title']} ({gif['bitly_gif_url']})"
        print(f"{x+1}) {gif_url}")


if __name__ == "__main__":
    gif()
