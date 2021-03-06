from parser_books import Shop
from parser_books import labirint_search, soup_creation, product_cards, labirint_filters


class Labirint(Shop):
    def parser_title(self):
        try:
            title = self.card.find("a", class_="product-title-link").text
            self.title = str(title).replace("\n", "")
        except Exception:
            self.title = None
            print("Error in parser_title")

    def parser_link(self):
        try:
            link = self.card.find("a", class_="product-title-link").get("href")
            self.link = "https://www.labirint.ru" + str(link).replace("\n", "")
        except Exception:
            self.link = None
            print("Error in parser_link")

    def parser_price(self):
        try:
            price = self.card.find("span", class_="price-val").text
            self.price = str("".join(price.split()[0:-1]))
        except Exception:
            self.price = None
            print("Error in parser_price")

    def parser_author(self):
        try:
            author = self.card.find("div", class_="product-author").text
            self.author = str(author).replace("\n", "")
        except Exception:
            self.author = None
            print("Error in parser_author")


def parser_labirint(product, filter):
    books = []
    url = labirint_search(product, labirint_filters[filter])
    soup = soup_creation(url)
    class_name = "card-column card-column_gutter col-xs-6 col-sm-3 col-md-1-5 col-xl-2"

    for i in soup.find_all("a", class_="pagination-number__text"):
        print(i.text)

    cards = product_cards(soup, class_name)
    for card in cards:
        books.append(Labirint(card).pars())
    #print(books)
    return books


if __name__ == "__main__":
    parser_labirint("Пушкин", "default")
