from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote
from ozon import OzonGoods

ozon_sort_list = ("score", "new", "price", "rating", "discount")
sber_sort_list = (0, 4, 1, 3, 6)
wild_sort_list = ("popular", "newly", "priceup", "rate", "sale")


def ozon_search(product, sorter=0):
    return f"https://www.ozon.ru/search/?from_global=true&sorting={ozon_sort_list[sorter]}&text={quote(product)}"


def sber_search(product, sorter=0):
    return f"https://sbermegamarket.ru/catalog/?q={quote(product)}#?sort={sber_sort_list[sorter]}"


def wild_search(product, sorter=0):
    return f"https://www.wildberries.ru/catalog/0/search.aspx?page=1&sort={wild_sort_list[sorter]}&search={quote(product)}"


def get_goods_from_ozon(soup):
    quotes = soup.find_all("div", class_="l4i li5")
    return quotes


def get_goods_from_wildberries(soup):
    quotes = soup.find_all(class_="price")
    return quotes


def soup_creation(url):
    html = urlopen(url).read().decode("utf-8")  # Получение html по url
    soup = BeautifulSoup(html, "html.parser")  # Создание соупа из html
    return soup


if __name__ == "__main__":
    product = "xiaomi"
    """
    print(f"Парсинг Озона по запросу{product}")
    print(ozon_search(product))
    soup = soup_creation(ozon_search("xiaomi"))
    for goods in get_goods_from_ozon(soup):
       OzonGoods(goods).run()
    print()
    """
    print(sber_search(product))
    print(wild_search(product))
    soup = soup_creation(wild_search("xiaomi"))
    print(get_goods_from_wildberries(soup))
