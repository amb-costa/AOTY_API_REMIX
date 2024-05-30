"""
json : REST API integration
Request, urlopen : URL handling
BeautifulSoup : HTML parsing 
"""
import json
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


class ArtistMethods:
    """Initializes all methods that are used to get user data"""

    # comment 4 amber : does api need related artists?
    # considering deleting it in favor of other features

    # () : initializing artist + needed attributes
    def __init__(self, class_ = None):
        if class_ is None:
            raise NotImplementedError()
        self.artist = ""
        self.url = ""
        self.req = ""
        self.artist_page = ""
        self.artist_url = ""

    # () : assigning artist + url, request + decoding to html
    def __set_artist_page(self, artist, url):
        self.artist = artist
        self.url = url
        self.req = Request(self.url, headers={"User-Agent": "Mozilla/6.0"})
        with urlopen(self.req, data = None) as open_req:
            ugly_page = open_req.read().decode("UTF-8")
        soup_page = BeautifulSoup(ugly_page, "html.parser")
        with open("output.html", "w", encoding = 'utf-8') as file : 
            file.write(str(soup_page.prettify()))
        self.artist_page = soup_page

    def __class_text(self, artist, class_name, url):
        if self.url != url:
            self.__set_artist_page(artist, url)
        return self.artist_page.find(class_=class_name).getText()

    def artist_albums(self, artist):
        url = self.artist_url + artist + "/"
        if self.url != url:
            self.__set_artist_page(artist, url)

        albums = self.artist_page.find_all(attrs={"data-type": "lp"})

        artist_albums = []
        for x in albums:
            album = x.getText().encode("ascii", "ignore").decode()[4:]
            album_name = album.split("LP")[0]
            artist_albums.append(album_name)

        return artist_albums

    def artist_albums_json(self, artist):
        albums_json = {"albums": self.artist_albums(artist)}
        return json.dumps(albums_json)

    def artist_mixtapes(self, artist):
        url = self.artist_url + artist + "/"
        if self.url != url:
            self.__set_artist_page(artist, url)

        mixtapes = self.artist_page.find_all(attrs={"data-type": "mixtape"})

        artist_mixtapes = []
        for x in mixtapes:
            mixtape = x.getText().encode("ascii", "ignore").decode()[4:]
            mixtape_name = mixtape.split("Mixtape")[0]
            artist_mixtapes.append(mixtape_name)

        return artist_mixtapes

    def artist_mixtapes_json(self, artist):
        mixtapes_json = {"mixtapes": self.artist_mixtapes(artist)}
        return json.dumps(mixtapes_json)

    def artist_eps(self, artist):
        url = self.artist_url + artist + "/"
        if self.url != url:
            self.__set_artist_page(artist, url)

        eps = self.artist_page.find_all(attrs={"data-type": "ep"})

        artist_eps = []
        for x in eps:
            ep = x.getText().encode("ascii", "ignore").decode()[4:]
            ep_name = ep.split("EP")[0]
            artist_eps.append(ep_name)

        return artist_eps

    def artist_eps_json(self, artist):
        eps_json = {"eps": self.artist_eps(artist)}
        return json.dumps(eps_json)

    def artist_singles(self, artist):
        url = self.artist_url + artist + "/"
        if self.url != url:
            self.__set_artist_page(artist, url)
        singles = self.artist_page.find_all(attrs={"data-type": "single"})

        artist_singles = []
        for x in singles:
            single = x.getText().encode("ascii", "ignore").decode()[4:]
            single_name = single.split("Single")[0]
            artist_singles.append(single_name)

        return artist_singles

    def artist_singles_json(self, artist):
        singles_json = {"singles": self.artist_singles(artist)}
        return json.dumps(singles_json)

    def artist_name(self, artist):
        return self.__class_text(
            artist, "artistHeadline", self.artist_url + artist + "/"
        )

    def artist_name_json(self, artist):
        name_json = {"name": self.artist_name(artist)}
        return json.dumps(name_json)

    def artist_critic_score(self, artist):
        return self.__class_text(
            artist, "artistCriticScore", self.artist_url + artist + "/"
        )

    def artist_critic_score_json(self, artist):
        critic_score_json = {"critic score": self.artist_critic_score(artist)}
        return json.dumps(critic_score_json)

    def artist_user_score(self, artist):
        return self.__class_text(
            artist, "artistUserScore", self.artist_url + artist + "/"
        )

    def artist_user_score_json(self, artist):
        user_score_json = {"user score": self.artist_user_score(artist)}
        return json.dumps(user_score_json)

    def artist_total_score(self, artist):
        return (
            int(self.artist_critic_score(artist)) + int(self.artist_user_score(artist))
        ) / 2

    def artist_total_score_json(self, artist):
        total_score_json = {"total score": self.artist_total_score(artist)}
        return json.dumps(total_score_json)

    def artist_follower_count(self, artist):
        return self.__class_text(artist, "followCount", self.artist_url + artist + "/")

    def artist_follower_count_json(self, artist):
        follower_count_json = {"follower count": self.artist_follower_count(artist)}
        return json.dumps(follower_count_json)

    def artist_details(self, artist):
        return self.__class_text(
            artist, "artistTopBox info", self.artist_url + artist + "/"
        )

    def artist_details_json(self, artist):
        artist_details_json = {"artist details": self.artist_details(artist)}
        return json.dumps(artist_details_json)

    def artist_top_songs(self, artist):
        return self.__class_text(
            artist, "trackListTable", self.artist_url + artist + "/"
        )

    def artist_top_songs_json(self, artist):
        artist_top_songs_json = {"top songs": self.artist_top_songs(artist)}
        return json.dumps(artist_top_songs_json)

    def similar_artists(self, artist):
        return self.__class_text(
            artist, "section relatedArtists", self.artist_url + artist + "/"
        )

    def similar_artists_json(self, artist):
        similar_artists_json = {"similar artists": self.similar_artists(artist)}
        return json.dumps(similar_artists_json)
