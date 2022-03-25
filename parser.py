from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote

ozon_sort_list = ('score', 'new', 'price', 'rating', 'discount')
sber_sort_list = (0, 4, 1, 3, 6)
wild_sort_list = ('popular', 'newly', 'priceup', 'rate', 'sale')


def ozon_search(product, sorter=0):
    return f"https://www.ozon.ru/search/?from_global=true&sorting={ozon_sort_list[sorter]}&text={quote(product)}"


def sber_search(product, sorter=0):
    return f'https://sbermegamarket.ru/catalog/?q={quote(product)}#?sort={sber_sort_list[sorter]}'


def wild_search(product, sorter=0):
    return f'https://www.wildberries.ru/catalog/0/search.aspx?page=1&sort={wild_sort_list[sorter]}&search={quote(product)}'


def test(product, sorter=0):
    print(ozon_search(product, sorter))
    print(sber_search(product, sorter))
    print(wild_search(product, sorter))


def soup_creation(url):
    html = urlopen(url).read().decode('utf-8')  # Получение html по url
    soup = BeautifulSoup(html, 'html.parser')  # Создание соупа из html
    return soup


if __name__ == "__main__":
    # print(soup_creation(ozon_search('губка')))
    test("xiaomi", 1)
