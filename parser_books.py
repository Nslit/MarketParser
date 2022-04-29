from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from urllib.parse import quote


def labirint_search(product, sorter="relevance"):
    return f"https://www.labirint.ru/search/{quote(product)}/?stype=0&order={sorter}"


def book24_search(product, sorter="sort"):
    return f"https://book24.ru/search/?q={quote(product)}&by=desc&sort={sorter}"


def bookvoed_search(product, sorter="relevancy"):
    return f"https://www.bookvoed.ru/books?q={quote(product)}&order={sorter}&desc=1&ishop=true"


def soup_creation(url):
    html = urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    return soup


def soup_creation_agent(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    return soup


def product_cards(soup, class_name):
    quotes = soup.find_all("div", class_=class_name)
    return quotes


class Shop:
    def __init__(self, card):
        self.card = card
        self.title = None
        self.author = None
        self.link = None
        self.price = None
        self.img = None

    def parser_test(self):
        print("#" * 30)
        print(type(self).__name__)
        print(self.title)
        print(self.author)
        print(self.price)
        print(self.link)
        print()

    def pars(self):
        self.parser_title()
        self.parser_link()
        self.parser_price()
        self.parser_author()

        #self.parser_test()

        return {
            "shop": str(type(self).__name__),
            "title": self.title,
            "author": self.author,
            "link": self.link,
            "price": self.price
        }
