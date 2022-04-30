from labirint import parser_labirint
from book24 import parser_book24
from parser_books import labirint_search, book24_search, bookvoed_search

import webbrowser

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.size = (300, 600)


class MarketParser(App):

    def build(self):
        self.FILTER_VALUE = 0
        self.SEARCH_QUERY = ""
        self.MARKETS = set()
        self.ALL_BOOKS = []

        self.mainLayout = BoxLayout(orientation='vertical', padding=(5, 0, 5, 5))
        self.headLayout = BoxLayout(orientation='vertical', size_hint=(1, 0.3), padding=(0, 0, 0, 5))
        self.menuLayout = BoxLayout(orientation='horizontal', spacing=10)

        self.textInput = TextInput(text='', multiline=False, size_hint=(1, 0.4))
        self.textInput.bind(text=self.on_search)
        self.search = Button(text='search')
        self.search.bind(on_press=self.start_searching)

        self.filtersLayout = BoxLayout(orientation='vertical')
        self.scoreToggle = ToggleButton(text='score', group='filters')
        self.scoreToggle.bind(on_press=self.on_sore_toggle)
        self.newToggle = ToggleButton(text='new', group='filters')
        self.newToggle.bind(on_press=self.on_new_toggle)
        self.priceToggle = ToggleButton(text='price', group='filters')
        self.priceToggle.bind(on_press=self.on_price_toggle)
        self.ratingToggle = ToggleButton(text='rating', group='filters')
        self.ratingToggle.bind(on_press=self.on_rating_toggle)
        self.discountToggle = ToggleButton(text='discount', group='filters')
        self.discountToggle.bind(on_press=self.on_discount_toggle)
        self.filtersLayout.add_widget(self.scoreToggle)
        self.filtersLayout.add_widget(self.newToggle)
        self.filtersLayout.add_widget(self.priceToggle)
        self.filtersLayout.add_widget(self.ratingToggle)
        self.filtersLayout.add_widget(self.discountToggle)

        self.shopsLayout = BoxLayout(orientation='horizontal')
        self.shopsCheckBoxLayout = BoxLayout(orientation='vertical')
        self.shopsCheckBoxNamesLayout = BoxLayout(orientation='vertical')
        self.labirintCheckBox = CheckBox()
        self.labirintCheckBox.bind(active=self.on_labirint_active)
        self.book24CheckBox = CheckBox()
        self.book24CheckBox.bind(active=self.on_book24_active)
        # self.bookvoedCheckBox = CheckBox()
        # self.bookvoedCheckBox.bind(active=self.onBookvoedActive)
        self.shopsCheckBoxLayout.add_widget(self.labirintCheckBox)
        self.shopsCheckBoxLayout.add_widget(self.book24CheckBox)
        # self.shopsCheckBoxLayout.add_widget(self.bookvoedCheckBox)
        self.shopsLayout.add_widget(self.shopsCheckBoxLayout)
        self.labirintCheckBoxName = Label(text='labirint')
        self.book24CheckBoxName = Label(text='book24')
        # self.bookvoedCheckBoxName = Label(text='bookvoed')
        self.shopsCheckBoxNamesLayout.add_widget(self.labirintCheckBoxName)
        self.shopsCheckBoxNamesLayout.add_widget(self.book24CheckBoxName)
        # self.shopsCheckBoxNamesLayout.add_widget(self.bookvoedCheckBoxName)
        self.shopsLayout.add_widget(self.shopsCheckBoxNamesLayout)

        self.menuLayout.add_widget(self.search)
        self.menuLayout.add_widget(self.filtersLayout)
        self.menuLayout.add_widget(self.shopsLayout)

        self.headLayout.add_widget(self.textInput)
        self.headLayout.add_widget(self.menuLayout)

        self.mainLayout.add_widget(self.headLayout)
        self.bottomLayout = self.book_list()
        self.mainLayout.add_widget(self.bottomLayout)

        return self.mainLayout

    def start_searching(self, instance):
        print(self.MARKETS)
        print(self.SEARCH_QUERY)
        if "labirint" in self.MARKETS:
            print(labirint_search(self.SEARCH_QUERY, self.FILTER_VALUE))
            self.ALL_BOOKS += parser_labirint(self.SEARCH_QUERY)
        if "book24" in self.MARKETS:
            print(book24_search(self.SEARCH_QUERY, self.FILTER_VALUE))
            self.ALL_BOOKS += parser_book24(self.SEARCH_QUERY)
        if "bookvoed" in self.MARKETS:
            print(bookvoed_search(self.SEARCH_QUERY, self.FILTER_VALUE))

        print(*self.ALL_BOOKS, sep="\n")

        self.mainLayout.clear_widgets()
        self.bottomLayout = self.book_list()
        self.mainLayout.add_widget(self.headLayout)
        self.mainLayout.add_widget(self.bottomLayout)
        self.ALL_BOOKS = []

    def book_list(self):
        self.layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))
        self.bottomLayout = ScrollView(size_hint=(1, None), size=(0, 450))
        for book in self.ALL_BOOKS:
            good = Book(book)
            good.run(self.layout)

        self.bottomLayout.add_widget(self.layout)
        return self.bottomLayout

    def on_search(self, instance, value):
        self.SEARCH_QUERY = value
        print(self.SEARCH_QUERY)

    def on_sore_toggle(self, instance):
        self.FILTER_VALUE = 0
        print(self.FILTER_VALUE)

    def on_new_toggle(self, instance):
        self.FILTER_VALUE = 1
        print(self.FILTER_VALUE)

    def on_price_toggle(self, instance):
        self.FILTER_VALUE = 2
        print(self.FILTER_VALUE)

    def on_rating_toggle(self, instance):
        self.FILTER_VALUE = 3
        print(self.FILTER_VALUE)

    def on_discount_toggle(self, instance):
        self.FILTER_VALUE = 4
        print(self.FILTER_VALUE)

    def on_labirint_active(self, checkbox, value):
        if value:
            self.MARKETS.add("labirint")
            print('The checkbox labirint is active')
        else:
            self.MARKETS.discard("labirint")
            print('The checkbox labirint is inactive')

    def on_book24_active(self, checkbox, value):
        if value:
            self.MARKETS.add("book24")
            print('The checkbox Book24 is active')
        else:
            self.MARKETS.discard("book24")
            print('The checkbox Book24 is inactive')

    def on_bookvoed_active(self, checkbox, value):
        if value:
            self.MARKETS.add("bookvoed")
            print('The checkbox bookvoed is active')
        else:
            self.MARKETS.discard("bookvoed")
            print('The checkbox bookvoed is inactive')


class Book:

    def __init__(self, book_info):
        self.shop = book_info["shop"]
        self.title = book_info["title"]
        self.author = book_info["author"]
        self.link = book_info["link"]
        self.price = book_info["price"]

    def run(self, layout):
        self.layout = layout
        self.book_text = f'Магазин:{self.shop}\nНазвание:{self.title}\nАвтор:{self.author}\nЦена:{self.price}'
        self.bookLabel = Label(text=self.book_text, size_hint_y=None, \
                               height=200, halign="left", valign="middle")
        self.bookLabel.bind(size=self.bookLabel.setter('text_size'))

        self.btn = Label(text=f"[ref=]Купить[/ref]", markup=True, \
                         on_ref_press=lambda instance, link: webbrowser.open(self.link, new=2))

        self.layout.add_widget(self.bookLabel)
        self.layout.add_widget(self.btn)


if __name__ == '__main__':
    MarketParser().run()
