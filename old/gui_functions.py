from constants import *
from parser_books import labirint_search, book24_search, bookvoed_search
from labirint import parser_labirint
from book24 import parser_book24


class GuiFunction:

    def onSearch(self, instance, value):
        global SEARCH_QUERY
        SEARCH_QUERY = value
        print(value)




    def onSoreToggle(self, instance):
        global FILTER_VALUE
        FILTER_VALUE = 0
        print(FILTER_VALUE)


    def onNewToggle(self, instance):
        global FILTER_VALUE
        FILTER_VALUE = 1
        print(FILTER_VALUE)


    def onPriceToggle(self, instance):
        global FILTER_VALUE
        FILTER_VALUE = 2
        print(FILTER_VALUE)


    def onRatingToggle(self, instance):
        global FILTER_VALUE
        FILTER_VALUE = 3
        print(FILTER_VALUE)


    def onDiscountToggle(self, instance):
        global FILTER_VALUE
        FILTER_VALUE = 4
        print(FILTER_VALUE)


    def onLabirintActive(self, checkbox, value):
        global MARKETS
        if value:
            MARKETS.add("labirint")
            print('The checkbox labirint is active')
        else:
            MARKETS.discard("labirint")
            print('The checkbox labirint is inactive')


    def onBook24Active(self, checkbox, value):
        global MARKETS
        if value:
            MARKETS.add("book24")
            print('The checkbox Book24 is active')
        else:
            MARKETS.discard("book24")
            print('The checkbox Book24 is inactive')


    def onBookvoedActive(self, checkbox, value):
        global MARKETS
        if value:
            MARKETS.add("bookvoed")
            print('The checkbox bookvoed is active')
        else:
            MARKETS.discard("bookvoed")
            print('The checkbox bookvoed is inactive')


if __name__ == '__main__':
    pass
