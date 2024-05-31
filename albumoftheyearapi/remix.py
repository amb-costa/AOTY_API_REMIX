"""
json : REST API integration
Request, urlopen : URL handling
BeautifulSoup : HTML parsing 
"""
import json
import html
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


class Remix:
    """Initializes all methods that are used to get user data"""

    # comment 4 amber : does api need related artists?
    # considering deleting it in favor of other features
    # only artist features that should be implemented : albums, mixtapes, ep, singles
    # plus every result should have related data like critics + user score
    # should artist have score? keep code just in case
    # should artist show followers?

    # () : initializing artist + needed attributes
    def __init__(self, class_ = None):
        if class_ is None:
            raise NotImplementedError()
        self.artist = ""
        self.url = ""
        self.req = ""
        self.artist_page = ""
        self.artist_url = ""

    # method works as a remix for an API update, that won't rely on mainpage
    # instead, will recollect info from different URLs and process only what's needed
    
    # then, it's possible to catch the required HTML
    def remix_albums(self, artist):
        url = self.artist_url + artist + "/?type=lp"
        album_request = Request(url, headers={"User-Agent": "Mozilla/6.0"})

        # bs4 will parse the decoded request into HTML
        # then it's possible to perform queries and searches
        # every piece of data is contained in a "albumBlock" class div
        # find_all is a bs4 tool, not native to python!
        # for every lp iteration -> title, year, rating are retrieved
        # then ratings should be retrieved to get proper ratings
        with urlopen(album_request, data = None) as open_album:
            ugly_page = open_album.read().decode("UTF-8")
            better_page = BeautifulSoup(ugly_page, "html.parser")
            project_block = better_page.find_all(attrs={"class":"albumBlock"})
            title = better_page.find_all(attrs={"class":"albumTitle"})
            year = better_page.find_all(attrs={"class":"type"})
            rates = better_page.find_all(attrs={"class":"rating"})
            typerate = better_page.find_all(attrs={"class":"ratingText"})
            # every two "ratingtext" corresponds at the number of ratings
            # this is useless for API purposes but can be overriden here 
            # ratings should be worked on, since not all records will have both critics
            print(project_block[4])



        
        el_p = len(title)
        rating = len(rates)

        remix_albums = []
        for i in range(0,el_p):
            album = title[i].getText()
            date = year[i].getText()
            remix_albums.append({"album_title" : album, "release_year" : date})

        return remix_albums
