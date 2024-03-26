# I got the tutorial for this setup file from this medium article -
# https://medium.com/nerd-for-tech/how-to-build-and-distribute-a-cli-tool-with-python-537ae41d9d78
from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="giphy-cli",
    version="0.0.1",
    author="Jacob Tweeten",
    author_email="jtweeten@unca.edu",
    license="Freeeeeee Pubilc Domain",
    description="Used to search, and find gifs using a Giphy api key",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JacobTweeten/Project2",
    packages=find_packages(),
    install_requires=[
        "click",
        "requests",
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    entry_points="""
        [console_scripts]
        gif=gif:gif
    """,
)
