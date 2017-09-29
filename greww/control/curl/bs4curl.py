import bs4
import urllib.request


def curl_url(url):
    return urllib.request.urlopen(url).read().decode('utf-8')

def soup_url(url):
    soup = bs4.BeautifulSoup(curl_p(url), 'html.parser')
    return soup
