from labirint import parser_labirint
from book24 import parser_book24
from parser_books import labirint_search, book24_search, bookvoed_search

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout


class MarketParser(App):

    def startSearching(self, instance):
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

    def book_list(self):
        self.layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))
        for i in self.ALL_BOOKS:
            btn = Button(text=str(i), size_hint_y=None, height=50)
            self.layout.add_widget(btn)
        self.bottomLayout = ScrollView(size_hint=(1, None), size=(0, 450))
        self.bottomLayout.add_widget(self.layout)
        return self.bottomLayout

    def build(self):
        self.FILTER_VALUE = 0
        self.SEARCH_QUERY = ""
        self.MARKETS = set()
        self.ALL_BOOKS = []

        self.mainLayout = BoxLayout(orientation='vertical')
        self.headLayout = BoxLayout(orientation='vertical', size_hint=(1, 0.3), padding=(0, 0, 0, 5))
        self.menuLayout = BoxLayout(orientation='horizontal')

        self.textInput = TextInput(text='', multiline=False, size_hint=(1, 0.4))
        self.textInput.bind(text=self.onSearch)
        self.search = Button(text='search')
        self.search.bind(on_press=self.startSearching)

        self.filtersLayout = BoxLayout(orientation='vertical')
        self.scoreToggle = ToggleButton(text='score', group='filters')
        self.scoreToggle.bind(on_press=self.onSoreToggle)
        self.newToggle = ToggleButton(text='new', group='filters')
        self.newToggle.bind(on_press=self.onNewToggle)
        self.priceToggle = ToggleButton(text='price', group='filters')
        self.priceToggle.bind(on_press=self.onPriceToggle)
        self.ratingToggle = ToggleButton(text='rating', group='filters')
        self.ratingToggle.bind(on_press=self.onRatingToggle)
        self.discountToggle = ToggleButton(text='discount', group='filters')
        self.discountToggle.bind(on_press=self.onDiscountToggle)
        self.filtersLayout.add_widget(self.scoreToggle)
        self.filtersLayout.add_widget(self.newToggle)
        self.filtersLayout.add_widget(self.priceToggle)
        self.filtersLayout.add_widget(self.ratingToggle)
        self.filtersLayout.add_widget(self.discountToggle)

        self.shopsLayout = BoxLayout(orientation='horizontal')
        self.shopsCheckBoxLayout = BoxLayout(orientation='vertical')
        self.shopsCheckBoxNamesLayout = BoxLayout(orientation='vertical')
        self.labirintCheckBox = CheckBox()
        self.labirintCheckBox.bind(active=self.onLabirintActive)
        self.book24CheckBox = CheckBox()
        self.book24CheckBox.bind(active=self.onBook24Active)
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

    def onSearch(self, instance, value):
        self.SEARCH_QUERY = value
        print(self.SEARCH_QUERY)

    def onSoreToggle(self, instance):
        self.FILTER_VALUE = 0
        print(self.FILTER_VALUE)

    def onNewToggle(self, instance):
        self.FILTER_VALUE = 1
        print(self.FILTER_VALUE)

    def onPriceToggle(self, instance):
        self.FILTER_VALUE = 2
        print(self.FILTER_VALUE)

    def onRatingToggle(self, instance):
        self.FILTER_VALUE = 3
        print(self.FILTER_VALUE)

    def onDiscountToggle(self, instance):
        self.FILTER_VALUE = 4
        print(self.FILTER_VALUE)

    def onLabirintActive(self, checkbox, value):
        if value:
            self.MARKETS.add("labirint")
            print('The checkbox labirint is active')
        else:
            self.MARKETS.discard("labirint")
            print('The checkbox labirint is inactive')

    def onBook24Active(self, checkbox, value):
        if value:
            self.MARKETS.add("book24")
            print('The checkbox Book24 is active')
        else:
            self.MARKETS.discard("book24")
            print('The checkbox Book24 is inactive')

    def onBookvoedActive(self, checkbox, value):
        if value:
            self.MARKETS.add("bookvoed")
            print('The checkbox bookvoed is active')
        else:
            self.MARKETS.discard("bookvoed")
            print('The checkbox bookvoed is inactive')


if __name__ == '__main__':
    MarketParser().run()
