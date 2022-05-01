from parser_books import Shop
from parser_books import bookvoed_search, soup_creation, product_cards


class Bookvoed(Shop):

    def parser_title(self):
        try:
            title = self.card.find("a", class_="OTb ls").text
            self.title = str(title)
            self.title = self.title.replace("\r", "")
            self.title = self.title.replace("\n", "")
        except Exception:
            self.title = None
            print("Error in parse_title")

    def parser_link(self):
        try:
            link = self.card.find("a", class_="fs gs").get("href")
            self.link = str(link)
        except Exception:
            self.link = None
            print("Error in parser_link")

    def parser_price(self):
        try:
            price = self.card.find("div", class_="zg").text
            self.price = str(price)
            self.price = self.price.replace("\r", "")
            self.price = self.price.replace("\n", "")
            self.price = self.price.replace("₽", "")
        except Exception:
            self.price = None
            print("Error in parser_price")

    def parser_author(self):
        try:
            author = self.card.find("div", class_="ms").text
            self.author = str(author)
            self.author = self.author.replace("\r", "")
            self.author = self.author.replace("\n", "")
        except Exception:
            self.author = None
            print("Error in parser_author")


def parser_bookvoed(product):
    books = []
    url = bookvoed_search(product)
    soup = soup_creation(url)
    class_name = "Ph"
    cards = product_cards(soup, class_name)
    for card in cards:
        books.append(Bookvoed(card).pars())
    #print(books)
    return books


if __name__ == "__main__":

    parser_bookvoed("Ремарк")