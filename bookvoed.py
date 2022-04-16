from parser_books import Shop

class Bookvoed(Shop):

    def parser_title(self):
        try:
            title = self.card.find("a", class_="ASb ls").text
            self.title = str(title)
        except Exception:
            self.title = None
            print("Error in parse_title")

    def run(self):
        self.parser_title()
        print(self.title, self.link, self.price)


if __name__ == "__main__":
    from parser_books import bookvoed_search, soup_creation, product_cards


    def test(product):
        url = bookvoed_search(product)
        soup = soup_creation(url)
        class_name = "Ph"
        cards = product_cards(soup, class_name)
        for card in cards:
            Bookvoed(card).run()

    test("Ремарк")