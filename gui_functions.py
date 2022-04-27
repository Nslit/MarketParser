from constants import *
from parser_books import labirint_search, book24_search, bookvoed_search
from labirint import parser_labirint
from book24 import parser_book24


def onSearch(instance, value):
    global SEARCH_QUERY
    SEARCH_QUERY = value
    print(value)



def startSearching(instance):
    global SEARCH_QUERY
    global MARKETS
    global FILTER_VALUE
    global ALL_BOOKS
    print(MARKETS)
    print(SEARCH_QUERY)
    if "labirint" in MARKETS:
        print(labirint_search(SEARCH_QUERY, FILTER_VALUE))
        ALL_BOOKS += parser_labirint(SEARCH_QUERY)
    if "book24" in MARKETS:
        print(book24_search(SEARCH_QUERY, FILTER_VALUE))
        ALL_BOOKS += parser_book24(SEARCH_QUERY)
    if "bookvoed" in MARKETS:
        print(bookvoed_search(SEARCH_QUERY, FILTER_VALUE))
    print(*ALL_BOOKS, sep="\n")


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
        MARKETS.add("book24")
        print('The checkbox Book24 is active')
    else:
        MARKETS.discard("book24")
        print('The checkbox Book24 is inactive')


def onBookvoedActive(checkbox, value):
    global MARKETS
    if value:
        MARKETS.add("bookvoed")
        print('The checkbox bookvoed is active')
    else:
        MARKETS.discard("bookvoed")
        print('The checkbox bookvoed is inactive')


if __name__ == '__main__':
    pass
