from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote

ozon_sort_list = ("score", "new", "price", "rating", "discount")
sber_sort_list = (0, 4, 1, 3, 6)
wild_sort_list = ("popular", "newly", "priceup", "rate", "sale")


def ozon_search(product, sorter=0):
    return f"https://www.ozon.ru/search/?from_global=true&sorting={ozon_sort_list[sorter]}&text={quote(product)}"


def sber_search(product, sorter=0):
    return f"https://sbermegamarket.ru/catalog/?q={quote(product)}#?sort={sber_sort_list[sorter]}"


def wild_search(product, sorter=0):
    return f"https://www.wildberries.ru/catalog/0/search.aspx?page=1&sort={wild_sort_list[sorter]}&search={quote(product)}"


def test(product, sorter=0):
    print(ozon_search(product, sorter))
    print(sber_search(product, sorter))
    print(wild_search(product, sorter))


def soup_creation(url):
    html = urlopen(url).read().decode("utf-8")  # Получение html по url
    soup = BeautifulSoup(html, "html.parser")  # Создание соупа из html
    return soup


if __name__ == "__main__":
    product = "xiaomi"
    link = ozon_search(product)
    soup = soup_creation(link)

    quotes = soup.find_all("div", class_="l4i li5")  # получение карточек всех товаров со страницы
    for i in quotes:
        link = "https://www.ozon.ru" + str(i.find("a", class_="tile-hover-target ji9").get("href"))
        title = str(i.find("a", class_="tile-hover-target ji9").text)
        price = i.find("span", class_="ui-n9 ui-o1 ui-o4")
        if price:
            price = price.text  # цена со скидкой
        else:
            price = i.find("span", class_="ui-n9 ui-o1").text  # цена без скидки
        img = i.find("img", class_="ui-i8").get("src")
        score = str(i.find("div", class_="ui-b2a").get("style"))[6: -2]
        if not score:
            score = 0
        score = round(float(score), 2)
        print(title)
        print(link)
        print(price)
        print(img)
        print(score)
        print()
