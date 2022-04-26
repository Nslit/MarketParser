class SberGoods:

    def __init__(self, goods):
        self.name = goods
        self.title = None
        self.link = None
        self.price = None
        self.img = None
        self.score = None
        self.reviews = None

    def title_parse(self):
        try:
            pass
        except Exception:
            pass

    def link_parse(self):
        try:
            pass
        except Exception:
            pass

    def price_parse(self):
        try:
            pass
        except Exception:
            pass

    def img_parser(self):
        try:
            pass
        except Exception:
            pass

    def score_parser(self):
        try:
            pass
        except Exception:
            pass

    def reviews_parser(self):
        try:
            pass
        except Exception:
            pass

    def test(self):
        print(self.title)
        print(self.link)
        print(self.price)
        print(self.img)
        print(self.score)
        print(self.reviews)

    def run(self):
        self.title_parse()
        self.link_parse()
        self.price_parse()
        self.img_parser()
        self.score_parser()
        self.reviews_parser()
        self.test()


if __name__ == "__main__":
    from old.parser import sber_search, soup_creation, get_goods_from_sber

    soup = soup_creation(sber_search("xiaomi"))
    for goods in get_goods_from_sber(soup):
        SberGoods(goods).run()