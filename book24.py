from parser_books import Shop


class Book24(Shop):

    def parser_title(self):
        try:
            title = self.card.find("a", class_="product-card__name smartLink").get("title")
            self.title = str(title)
        except Exception:
            self.title = None
            print("Error in parse_title")

    def parser_link(self):
        try:
            link = self.card.find("a", class_="product-card__name smartLink").get("href")
            self.link = "https://book24.ru" + str(link)
        except Exception:
            self.link = None
            print("Error in parser_link")

    def parser_price(self):
        try:
            price = self.card.find("div", class_="product-card-price__current").get("span")
            self.price = str(price)
        except Exception:
            self.price = None
            print("Error in parser_price")

    def parser_author(self):
        try:
            author = self.card.find("div", class_="author-list product-card__authors-holder").text
            self.author = str(author)
        except Exception:
            self.author = None
            print("Error in parser_author")


def parser_book24(product):
    url = book24_search(product)
    soup = soup_creation_agent(url)
    class_name = "product-list__item"
    cards = product_cards(soup, class_name)
    for card in cards:
        Book24(card).pars()


if __name__ == "__main__":
    from parser_books import book24_search, soup_creation_agent, product_cards

    parser_book24("Ремарк")
