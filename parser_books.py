from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from urllib.parse import quote

labirint_filters = {"default": "relevance&way=back",
                    "popular": "popularity&way=forward",
                    "new": "date&way=back",
                    "price_up": "price&way=forward",
                    "price_down": "price&way=back",
                    }
book24_filters = {"default": "desc&sort=date",
                  "popular": "desc&sort=sort",
                  "new": "desc&sort=date",
                  "price_up": "asc&sort=price_discount",
                  "price_down": "desc&sort=price_discount",
                  }
bookvoed_filters = {"default": "relevancy&desc=1",
                    "popular": "sales&desc=1",
                    "new": "time&desc=1",
                    "price_up": "price&desc=0",
                    "price_down": "price&desc=1",
                    }


def labirint_search(product, sorter=labirint_filters["default"]):
    return f"https://www.labirint.ru/search/{quote(product)}/?stype=0&order={sorter}"


def book24_search(product, sorter=book24_filters["default"]):
    return f"https://book24.ru/search/?q={quote(product)}&by={sorter}"


def bookvoed_search(product, sorter=bookvoed_filters["default"]):
    return f"https://www.bookvoed.ru/books?q={quote(product)}&order={sorter}&ishop=true"


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


def joining_lists(*lists):
    answer = []
    max_len = 0
    for i in lists:
        if len(i) > max_len:
            max_len = len(i)
    for i in range(max_len):
        for l in lists:
            try:
                answer.append(l[i])
            except:
                pass
    return answer


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

        # self.parser_test()

        return {
            "shop": str(type(self).__name__),
            "title": self.title,
            "author": self.author,
            "link": self.link,
            "price": self.price
        }


if __name__ == '__main__':
    pass
