from parser_books import Shop


class Book24(Shop):

    def parser_title(self):
        try:
            title = self.card.find("a", class_="product-card__name smartLink").text
            self.title = str(title)
        except Exception:
            self.title = None
            print("Error in parse_title")

    def run(self):
        self.parser_title()
        print(self.title, self.link, self.price)


if __name__ == "__main__":
    from parser_books import book24_search, soup_creation_agent, product_cards

    def test(product):
        url = book24_search(product)
        soup = soup_creation_agent(url)
        class_name = "product-list__item"
        cards = product_cards(soup, class_name)
        for card in cards:
            Book24(card).run()


    test("Ремарк")
