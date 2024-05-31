"""
sqlalchemy : REST API integration
pytest : testing
AOTY : API module
"""

from sqlalchemy import null
import pytest
from albumoftheyearapi import AOTY

# establishing Kanye West as test subject
@pytest.fixture(name="artist")
def artist_fixture():
    return "183-kanye-west"

# initializing AOTY class by establishing client
@pytest.mark.first
def test_initialize():
    c = AOTY()
    pytest.client = c
    assert pytest.client != null

# testing for artist_albums(name = "fixture") result
def test_get_artist_albums(artist):
    artist_albums = pytest.remix.artist_albums(artist)
    assert artist_albums != null

if __name__ == "__main__":
    ARTIST = "183-kanye-west"
    AlbumWrapper = AOTY()

    ye_data = {
        "albums-remix" : AlbumWrapper.remix_albums(ARTIST),
    }
    print(ye_data)
    print("test was successful")

