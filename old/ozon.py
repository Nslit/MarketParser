class OzonGoods:

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
            title = self.name.find("a", class_="tile-hover-target ji9").text
            self.title = str(title)
        except Exception:
            self.title = None
            print("Error in title_parse")

    def link_parse(self):
        try:
            link = self.name.find("a", class_="tile-hover-target ji9").get("href")
            self.link = "https://www.ozon.ru" + str(link)
        except Exception:
            self.link = None
            print("Error in link_parse")

    def price_parse(self):
        try:
            price = self.name.find("span", class_="ui-n9 ui-o1 ui-o4").text
            if not price:
                price = self.name.find("span", class_="ui-n9 ui-o1").text
            self.price = str(price)
        except Exception:
            self.price = None
            print("Error in price_parse")

    def img_parser(self):
        try:
            img = self.name.find("img", class_="ui-i8").get("src")
            self.img = str(img)
        except Exception:
            self.img = None
            print("Error in img_parser")

    def score_parser(self):
        try:
            score = str(self.name.find("div", class_="ui-b2a").get("style"))[6: -2]
            score = round(float(score), 2)
            self.score = str(score)
        except Exception:
            self.score = None
            print("Error in score_parser")

    def reviews_parser(self):
        try:
            reviews = self.name.find("span", class_="cx8").text
            reviews = reviews.split(" ")[0]
            self.reviews = str(reviews)
        except Exception:
            self.reviews = None
            print("Error in reviews_parser")

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
    from parser import ozon_search, soup_creation, get_goods_from_ozon
    soup = soup_creation(ozon_search("xiaomi"))
    for goods in get_goods_from_ozon(soup):
        OzonGoods(goods).run()
