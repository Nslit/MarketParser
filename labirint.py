from parser_books import Shop


class Labirint(Shop):
    def parse_title_link(self):
        try:
            title = self.card.find("a", class_="product-title-link").text
            link = self.card.find("a", class_="product-title-link").get("href")
            self.title = str(title).replace("\n", "")
            self.link = "https://www.labirint.ru" + str(link).replace("\n", "")
        except Exception:
            self.title = None
            self.link = None
            print("Error in parse_title_link")

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

    def pars(self):
        self.parse_title_link()
        self.parser_price()
        self.parser_author()

        self.parser_test()


if __name__ == "__main__":
    from parser_books import labirint_search, soup_creation, product_cards


    def test(product):
        url = labirint_search(product)
        soup = soup_creation(url)
        class_name = "card-column card-column_gutter col-xs-6 col-sm-3 col-md-1-5 col-xl-2"
        cards = product_cards(soup, class_name)
        for card in cards:
            Labirint(card).pars()


    test("Ремарк")
