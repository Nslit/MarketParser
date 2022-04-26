from gui_functions import *
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

    def book_list(self):
        layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        for i in range(100):
            btn = Button(text=str(i), size_hint_y=None, height=50)
            layout.add_widget(btn)
        bottomLayout = ScrollView(size_hint=(1, None), size=(0, 450))
        bottomLayout.add_widget(layout)
        return bottomLayout

    def build(self):
        mainLayout = BoxLayout(orientation='vertical')
        headLayout = BoxLayout(orientation='vertical', size_hint=(1, 0.4), padding=(0, 0, 0, 5))
        bottomLayout = BoxLayout(orientation='vertical')
        menuLayout = BoxLayout(orientation='horizontal')

        textInput = TextInput(text='Enter a request', multiline=False)
        textInput.bind(text=onSearch)
        search = Button(text='search')
        search.bind(on_press=startSearching)

        filtersLayout = BoxLayout(orientation='vertical')
        scoreToggle = ToggleButton(text='score', group='filters')
        scoreToggle.bind(on_press=onSoreToggle)
        newToggle = ToggleButton(text='new', group='filters')
        newToggle.bind(on_press=onNewToggle)
        priceToggle = ToggleButton(text='price', group='filters')
        priceToggle.bind(on_press=onPriceToggle)
        ratingToggle = ToggleButton(text='rating', group='filters')
        ratingToggle.bind(on_press=onRatingToggle)
        discountToggle = ToggleButton(text='discount', group='filters')
        discountToggle.bind(on_press=onDiscountToggle)
        filtersLayout.add_widget(scoreToggle)
        filtersLayout.add_widget(newToggle)
        filtersLayout.add_widget(priceToggle)
        filtersLayout.add_widget(ratingToggle)
        filtersLayout.add_widget(discountToggle)

        shopsLayout = BoxLayout(orientation='horizontal')
        shopsCheckBoxLayout = BoxLayout(orientation='vertical')
        shopsCheckBoxNamesLayout = BoxLayout(orientation='vertical')
        labirintCheckBox = CheckBox()
        labirintCheckBox.bind(active=onLabirintActive)
        book24CheckBox = CheckBox()
        book24CheckBox.bind(active=onBook24Active)
        # wildberriesCheckBox = CheckBox()
        # wildberriesCheckBox.bind(active=onWildberriesActive)
        shopsCheckBoxLayout.add_widget(labirintCheckBox)
        shopsCheckBoxLayout.add_widget(book24CheckBox)
        # shopsCheckBoxLayout.add_widget(wildberriesCheckBox)
        shopsLayout.add_widget(shopsCheckBoxLayout)
        labirintCheckBoxName = Label(text='labirint')
        book24CheckBoxName = Label(text='sber')
        # wildberriesCheckBoxName = Label(text='wildberries')
        shopsCheckBoxNamesLayout.add_widget(labirintCheckBoxName)
        shopsCheckBoxNamesLayout.add_widget(book24CheckBoxName)
        # shopsCheckBoxNamesLayout.add_widget(wildberriesCheckBoxName)
        shopsLayout.add_widget(shopsCheckBoxNamesLayout)

        menuLayout.add_widget(search)
        menuLayout.add_widget(filtersLayout)
        menuLayout.add_widget(shopsLayout)

        headLayout.add_widget(textInput)
        headLayout.add_widget(menuLayout)

        mainLayout.add_widget(headLayout)
        # mainLayout.add_widget(bottomLayout)
        mainLayout.add_widget(self.book_list())

        return mainLayout


if __name__ == '__main__':
    MarketParser().run()
