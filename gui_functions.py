from constants import *
from parser import ozon_search, sber_search, wild_search


def onSearch(instance, value):
    global SEARCH_QUERY
    SEARCH_QUERY = value
    print(value)


def startSearching(instance):
    global SEARCH_QUERY
    global MARKETS
    global FILTER_VALUE
    print(MARKETS)
    print(SEARCH_QUERY)
    if "ozon" in MARKETS:
        print(ozon_search(SEARCH_QUERY, FILTER_VALUE))
    if "sber" in MARKETS:
        print(sber_search(SEARCH_QUERY, FILTER_VALUE))
    if "wieldberries" in MARKETS:
        print(wild_search(SEARCH_QUERY, FILTER_VALUE))


def onSoreToggle(instance):
    global FILTER_VALUE
    FILTER_VALUE = 0
    print(FILTER_VALUE)


def onNewToggle(instance):
    global FILTER_VALUE
    FILTER_VALUE = 1
    print(FILTER_VALUE)


def onPriceToggle(instance):
    global FILTER_VALUE
    FILTER_VALUE = 2
    print(FILTER_VALUE)


def onRatingToggle(instance):
    global FILTER_VALUE
    FILTER_VALUE = 3
    print(FILTER_VALUE)


def onDiscountToggle(instance):
    global FILTER_VALUE
    FILTER_VALUE = 4
    print(FILTER_VALUE)


def onLabirintActive(checkbox, value):
    global MARKETS
    if value:
        MARKETS.add("labirint")
        print('The checkbox labirint is active')
    else:
        MARKETS.discard("labirint")
        print('The checkbox labirint is inactive')


def onBook24Active(checkbox, value):
    global MARKETS
    if value:
        MARKETS.add("Book24")
        print('The checkbox Book24 is active')
    else:
        MARKETS.discard("Book24")
        print('The checkbox Book24 is inactive')


def onWildberriesActive(checkbox, value):
    global MARKETS
    if value:
        MARKETS.add("wieldberries")
        print('The checkbox Wildberries is active')
    else:
        MARKETS.discard("wieldberries")
        print('The checkbox Wildberries is inactive')


if __name__ == '__main__':
    pass
