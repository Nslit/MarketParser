from parser_books import Shop

class ChitaiGorod(Shop):

    def parser_title(self):
        try:
            title = self.card.find("a", class_="product-card__link js-watch-productlink").text
            self.title = str(title)
        except Exception:
            self.title = None
            print("Error in parse_title")

    def run(self):
        self.parser_title()
        print(self.title, self.link, self.price)


if __name__ == "__main__":
    from parser_books import chitai_gorod_search, soup_creation_agent, product_cards


    def test(product):
        url = chitai_gorod_search(product)
        soup = soup_creation_agent(url)
        class_name = "product-card js_product js__product_card"
        cards = product_cards(soup, class_name)
        for card in cards:
            print(card)
            ChitaiGorod(card).run()

    test("Ремарк")