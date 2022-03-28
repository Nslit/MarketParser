from parser import ozon_search, soup_creation


def get_goods_from_ozon(soup):
    quotes = soup.find_all("div", class_="l4i li5")
    return quotes


class OzonGoods:

    def __init__(self, goods):
        self.name = goods
        self.title = None
        self.link = None

    def title_parse(self):
        try:
            title = self.name.find("a", class_="tile-hover-target ji9").text
            self.title = str(title)
        except Exception:
            pass

    def link_parse(self):
        try:
            link = self.name.find("a", class_="tile-hover-target ji9").get("href")
            self.link = "https://www.ozon.ru" + str(link)
        except Exception:
            pass

    def test(self):
        print(self.title)
        print(self.link)

    def run(self):
        self.title_parse()
        self.link_parse()
        self.test()


if __name__ == "__main__":
    soup = soup_creation(ozon_search("xiaomi"))
    for goods in get_goods_from_ozon(soup):
        OzonGoods(goods).run()
