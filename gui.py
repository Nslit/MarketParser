from labirint import parser_labirint
from book24 import parser_book24
from bookvoed import parser_bookvoed
from parser_books import labirint_search, book24_search, bookvoed_search, joining_lists

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

Window.size = (400, 600)


class MarketParser(App):

    def build(self):
        self.FILTER_VALUE = "default"
        self.SEARCH_QUERY = ""
        self.MARKETS = set()
        self.ALL_BOOKS = []

        self.mainLayout = BoxLayout(orientation='vertical', padding=(5, 0, 5, 5))
        self.headLayout = BoxLayout(orientation='vertical', size_hint=(1, 0.3), padding=(0, 0, 0, 5))
        self.menuLayout = BoxLayout(orientation='horizontal', spacing=10)

        self.textInput = TextInput(text='', multiline=False, size_hint=(1, 0.4))
        self.textInput.bind(text=self.on_search)
        self.search = Button(text='Поиск')
        self.search.bind(on_press=self.start_searching)

        self.filtersLayout = BoxLayout(orientation='vertical', size_hint=(0.7, 1))
        self.defaultToggle = ToggleButton(text='Стандартные', group='filters')
        self.defaultToggle.bind(on_press=self.on_default_toggle)
        self.popularToggle = ToggleButton(text='Популярные', group='filters')
        self.popularToggle.bind(on_press=self.on_popular_toggle)
        self.newToggle = ToggleButton(text='Новые', group='filters')
        self.newToggle.bind(on_press=self.on_new_toggle)
        self.price_upToggle = ToggleButton(text='Дешевые', group='filters')
        self.price_upToggle.bind(on_press=self.on_price_up_toggle)
        self.price_downToggle = ToggleButton(text='Дорогие', group='filters')
        self.price_downToggle.bind(on_press=self.on_price_down_toggle)
        self.filtersLayout.add_widget(self.defaultToggle)
        self.filtersLayout.add_widget(self.popularToggle)
        self.filtersLayout.add_widget(self.newToggle)
        self.filtersLayout.add_widget(self.price_upToggle)
        self.filtersLayout.add_widget(self.price_downToggle)

        self.shopsLayout = BoxLayout(orientation='horizontal')
        self.shopsCheckBoxLayout = BoxLayout(orientation='vertical')
        self.shopsCheckBoxNamesLayout = BoxLayout(orientation='vertical')
        self.labirintCheckBox = CheckBox()
        self.labirintCheckBox.bind(active=self.on_labirint_active)
        self.book24CheckBox = CheckBox()
        self.book24CheckBox.bind(active=self.on_book24_active)
        self.bookvoedCheckBox = CheckBox()
        self.bookvoedCheckBox.bind(active=self.on_bookvoed_active)
        self.shopsCheckBoxLayout.add_widget(self.labirintCheckBox)
        self.shopsCheckBoxLayout.add_widget(self.book24CheckBox)
        self.shopsCheckBoxLayout.add_widget(self.bookvoedCheckBox)
        self.shopsLayout.add_widget(self.shopsCheckBoxLayout)
        self.labirintCheckBoxName = Label(text='labirint')
        self.book24CheckBoxName = Label(text='book24')
        self.bookvoedCheckBoxName = Label(text='bookvoed')
        self.shopsCheckBoxNamesLayout.add_widget(self.labirintCheckBoxName)
        self.shopsCheckBoxNamesLayout.add_widget(self.book24CheckBoxName)
        self.shopsCheckBoxNamesLayout.add_widget(self.bookvoedCheckBoxName)
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
        self.labirint_books = []
        self.book24_books = []
        self.bookvoed_books = []
        if "labirint" in self.MARKETS:
            print(labirint_search(self.SEARCH_QUERY, self.FILTER_VALUE))
            self.labirint_books = parser_labirint(self.SEARCH_QUERY, self.FILTER_VALUE)
        if "book24" in self.MARKETS:
            print(book24_search(self.SEARCH_QUERY, self.FILTER_VALUE))
            self.book24_books = parser_book24(self.SEARCH_QUERY, self.FILTER_VALUE)
        if "bookvoed" in self.MARKETS:
            print(bookvoed_search(self.SEARCH_QUERY, self.FILTER_VALUE))
            self.bookvoed_books = parser_bookvoed(self.SEARCH_QUERY, self.FILTER_VALUE)

        self.ALL_BOOKS = joining_lists(self.labirint_books, self.book24_books, self.bookvoed_books)
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

        if  self.ALL_BOOKS:
            kniga = ''
            count = len(self.ALL_BOOKS)
            if count % 10 in (0, 5, 6, 7, 8, 9):
                kniga = "книг"
            elif count % 10 == 1:
                kniga = "книга"
            elif count % 10 in (2, 3, 4):
                kniga = "книги"

            self.countBooks = Label(text=f"По вашему запросу нашлось {count} {kniga}!", size_hint_y=None, \
                                       height=20, halign="left", valign="middle")
            self.countBooks.bind(size=self.countBooks.setter('text_size'))
            self.layout.add_widget(self.countBooks)

        for book in self.ALL_BOOKS:
            good = Book(book)
            good.run(self.layout)

        if not self.ALL_BOOKS and not self.SEARCH_QUERY:
            self.info = """Это приложение для поиска книг на нескольких платформах одновременно.
Для того, чтобы начать, напишите свой запрос в строку поиска, галочками выберите нужные магазины, если нужно отсортировать результаты поиска, нажмите на нужный фильтр и нажмите на кнопку 'Поиск'."""
            self.infoLabel = Label(text=self.info, size_hint_y=None, \
                                   height=200, halign="left", valign="middle")
            self.infoLabel.bind(size=self.infoLabel.setter('text_size'))
            self.layout.add_widget(self.infoLabel)

        elif not self.ALL_BOOKS:
            self.info = "К сожалению ничего не нашлось :("
            self.infoLabel = Label(text=self.info, size_hint_y=None, \
                                   height=200, halign="left", valign="middle")
            self.infoLabel.bind(size=self.infoLabel.setter('text_size'))
            self.layout.add_widget(self.infoLabel)

        self.bottomLayout.add_widget(self.layout)
        return self.bottomLayout

    def on_search(self, instance, value):
        self.SEARCH_QUERY = value
        print(self.SEARCH_QUERY)

    def on_default_toggle(self, instance):
        self.FILTER_VALUE = "default"
        print(self.FILTER_VALUE)

    def on_popular_toggle(self, instance):
        self.FILTER_VALUE = "popular"
        print(self.FILTER_VALUE)

    def on_new_toggle(self, instance):
        self.FILTER_VALUE = "new"
        print(self.FILTER_VALUE)

    def on_price_up_toggle(self, instance):
        self.FILTER_VALUE = "price_up"
        print(self.FILTER_VALUE)

    def on_price_down_toggle(self, instance):
        self.FILTER_VALUE = "price_down"
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
            print('The checkbox book24 is active')
        else:
            self.MARKETS.discard("book24")
            print('The checkbox book24 is inactive')

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
