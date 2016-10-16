import urlparse
import urllib2
from BeautifulSoup import BeautifulSoup


class Hyperlinks:

    def __init__(self, url):
        self.links = list()
        self.parse_url(url)

    def is_absolute(self, url):
        return bool(urlparse.urlparse(url).netloc)

    def parse_url(self, url):
        html_page = None
        try:
            html_page = urllib2.urlopen(url)
        except:
            pass
        try:
            soup = BeautifulSoup(html_page)

            for link in soup.findAll('a'):
                hyperlink = link.get('href')
                try:
                    if self.is_absolute(hyperlink):
                        self.links.append(hyperlink)
                    else:
                        constructed_hyperlink = urlparse.urljoin(url, hyperlink)
                        # double check url is valid after construction
                        if self.is_absolute(constructed_hyperlink):
                            self.links.append(constructed_hyperlink)
                except:
                    pass
        except:
            pass

