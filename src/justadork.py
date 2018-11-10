import requests
import urllib
import time
from lxml.html import document_fromstring

class DorkScanner:

    def __init__(self, config):
        self.config = config

    def get_search_url(self, dork):
        return self.config['search-engine'].format(urllib.parse.quote_plus(dork))

    def search_urls(self, dork):
        res = []
        r = requests.get(self.get_search_url(dork))
        if r.status_code == 200:
            for u in document_fromstring(r.text).cssselect(self.config['css-selector']):
                href = u.attrib['href']
                if href.startswith(self.config['url-startswith']):
                    if self.config['url-is-query']:
                        url = urllib.parse.parse_qs(urllib.parse.urlparse(href).query)[self.config['url-query']][0]
                        res.append(url)
                    else:
                        res.append(href)
        else:
            return None
        return res

    def save(self, urls):
        self.save_as(urls, "output/{}.txt".format(str(time.time())))

    def save_as(self, urls, filename):
        file = open(filename, 'w+')
        for url in urls:
            file.write("{}\n".format(str(url)))
