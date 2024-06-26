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
    artist_albums = pytest.client.artist_albums(artist)
    assert artist_albums != null


def test_get_artist_albums_json(artist):
    artist_albums_json = pytest.client.artist_albums_json(artist)
    assert artist_albums_json != null


def test_get_artist_mixtapes(artist):
    artist_mixtapes = pytest.client.artist_mixtapes(artist)
    assert artist_mixtapes != null


def test_get_artist_mixtapes_json(artist):
    artist_mixtapes_json = pytest.client.artist_mixtapes_json(artist)
    assert artist_mixtapes_json != null


def test_get_artist_eps(artist):
    artist_eps = pytest.client.artist_eps(artist)
    assert artist_eps != null


def test_get_artist_eps_json(artist):
    artist_eps_json = pytest.client.artist_eps_json(artist)
    assert artist_eps_json != null


def test_get_artist_singles(artist):
    artist_singles = pytest.client.artist_singles(artist)
    assert artist_singles != null


def test_get_artist_singles_json(artist):
    artist_singles_json = pytest.client.artist_singles_json(artist)
    assert artist_singles_json != null


def test_get_artist_name(artist):
    artist_name = pytest.client.artist_name(artist)
    assert artist_name != null


def test_get_artist_name_json(artist):
    artist_name_json = pytest.client.artist_name_json(artist)
    assert artist_name_json != null


def test_get_artist_critic_score(artist):
    artist_critic_score = pytest.client.artist_critic_score(artist)
    assert artist_critic_score != null


def test_get_artist_critic_score_json(artist):
    artist_critic_score_json = pytest.client.artist_critic_score_json(artist)
    assert artist_critic_score_json != null


def test_get_artist_user_score(artist):
    artist_user_score = pytest.client.artist_user_score(artist)
    assert artist_user_score != null


def test_get_artist_user_score_json(artist):
    artist_user_score_json = pytest.client.artist_user_score_json(artist)
    assert artist_user_score_json != null


def test_get_artist_total_score(artist):
    artist_total_score = pytest.client.artist_total_score(artist)
    assert artist_total_score != null


def test_get_artist_total_score_json(artist):
    artist_total_score_json = pytest.client.artist_total_score_json(artist)
    assert artist_total_score_json != null


def test_get_artist_follower_count(artist):
    artist_follower_count = pytest.client.artist_follower_count(artist)
    assert artist_follower_count != null


def test_get_artist_follower_count_json(artist):
    artist_follower_count_json = pytest.client.artist_follower_count_json(artist)
    assert artist_follower_count_json != null


def test_get_artist_details(artist):
    artist_details = pytest.client.artist_details(artist)
    assert artist_details != null


def test_get_artist_details_json(artist):
    artist_details_json = pytest.client.artist_details_json(artist)
    assert artist_details_json != null


# def test_get_artist_top_songs(artist):
#     artist_top_songs = pytest.client.artist_top_songs(artist)
#     assert artist_top_songs != null


# def test_get_artist_top_songs_json(artist):
#     artist_top_songs_json = pytest.client.artist_top_songs(artist)
#     assert artist_top_songs_json != null


# def test_get_similar_artists(artist):
#     similar_artists = pytest.client.similar_artists(artist)
#     assert similar_artists != null


# def test_get_similar_artists_json(artist):
#     similar_artists_json = pytest.client.similar_artists_json(artist)
#     assert similar_artists_json != null


if __name__ == "__main__":
    ARTIST = "183-kanye-west"
    AlbumWrapper = AOTY()

    ye_data = {
        "albums" : AlbumWrapper.artist_albums(ARTIST),
        "mixtapes" : AlbumWrapper.artist_mixtapes(ARTIST),
        "eps" : AlbumWrapper.artist_eps(ARTIST),
        "singles" : AlbumWrapper.artist_singles(ARTIST),
        "artist_name" : AlbumWrapper.artist_name(ARTIST),
        "critic_score" :  AlbumWrapper.artist_critic_score(ARTIST),
        "user_score" : AlbumWrapper.artist_user_score(ARTIST),
        "total_score" : AlbumWrapper.artist_total_score(ARTIST),
        "follower_count" : AlbumWrapper.artist_follower_count(ARTIST),
        "artist_details" : AlbumWrapper.artist_details(ARTIST),
        # "top_songs" : AlbumWrapper.artist_top_songs(ARTIST),
        # "similar_artists" : AlbumWrapper.similar_artists(ARTIST)
    }

    print (ye_data)
    print("test was successful")
