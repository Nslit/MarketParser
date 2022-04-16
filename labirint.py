from parser_books import Shop


class Labirint(Shop):
    def parse_title_link(self):
        try:
            title = self.card.find("a", class_="product-title-link").text
            link = self.card.find("a", class_="product-title-link").get("href")
            self.title = str(title)
            self.link = "https://www.labirint.ru" + str(link)
        except Exception:
            self.title = None
            self.link = None
            print("Error in parse_title_link")

    def parser_price(self):
        try:
            price = self.card.find("span", class_="price-val").text
            self.price = str(price)
        except Exception:
            self.price = None
            print("Error in parser_price")

    def run(self):
        self.parse_title_link()
        self.parser_price()
        print(self.title, self.link, self.price)


if __name__ == "__main__":
    from parser_books import labirint_search, soup_creation, product_cards


    def test(product):
        url = labirint_search(product)
        soup = soup_creation(url)
        class_name = "card-column card-column_gutter col-xs-6 col-sm-3 col-md-1-5 col-xl-2"
        cards = product_cards(soup, class_name)
        for card in cards:
            Labirint(card).run()

    test("Ремарк")
