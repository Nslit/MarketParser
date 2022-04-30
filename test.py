import webbrowser
from kivy.app import App
from kivy.uix.button import Button


class Test(App):
    def build(self):
        url = "https://habr.com/ru/post/470938/"
        btn = Button(text="поиск")
        btn.bind(on_press=lambda instance : webbrowser.open(url, new=2))
        return btn

Test().run()

class book:

    def __init__(self, book_info):
        self.shop = book_info["shop"]
        self.title = book_info["title"]
        self.author = book_info["author"]
        self.link = book_info["link"]
        self.price = book_info["price"]

    def run(self, layout):
        self.layout = layout
        self.book_text = f' Магазин:{self.shop}\n Название:{self.title}\n Автор:{self.author}\n Цена:{self.price}'
        self.bookLabel = Label(text=book_text, size_hint_y=None, height=200, halign="left", valign="middle")
        self.bookLabel.bind(size=self.bookLabel.setter('text_size'))

        self.btn = Button(text="Купить")
        self.btn.bind(on_press=lambda instance: webbrowser.open(self.link, new=2))

        self.layout.add_widget(self.bookLabel)
        self.layout.add_widget(self.btn)



