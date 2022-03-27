from gui_functions import *
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton

from kivy.uix.boxlayout import BoxLayout


class TestApp(App):

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
        ozonCheckBox = CheckBox()
        ozonCheckBox.bind(active=onOzonActive)
        sberCheckBox = CheckBox()
        sberCheckBox.bind(active=onSberActive)
        wildberriesCheckBox = CheckBox()
        wildberriesCheckBox.bind(active=onWildberriesActive)
        shopsCheckBoxLayout.add_widget(ozonCheckBox)
        shopsCheckBoxLayout.add_widget(sberCheckBox)
        shopsCheckBoxLayout.add_widget(wildberriesCheckBox)
        shopsLayout.add_widget(shopsCheckBoxLayout)
        ozonCheckBoxName = Label(text='ozon')
        sberCheckBoxName = Label(text='sber')
        wildberriesCheckBoxName = Label(text='wildberries')
        shopsCheckBoxNamesLayout.add_widget(ozonCheckBoxName)
        shopsCheckBoxNamesLayout.add_widget(sberCheckBoxName)
        shopsCheckBoxNamesLayout.add_widget(wildberriesCheckBoxName)
        shopsLayout.add_widget(shopsCheckBoxNamesLayout)

        menuLayout.add_widget(search)
        menuLayout.add_widget(filtersLayout)
        menuLayout.add_widget(shopsLayout)

        headLayout.add_widget(textInput)
        headLayout.add_widget(menuLayout)

        goods1 = Button(text='goods1')
        goods2 = Button(text='goods2')
        goods3 = Button(text='goods3')
        bottomLayout.add_widget(goods1)
        bottomLayout.add_widget(goods2)
        bottomLayout.add_widget(goods3)

        mainLayout.add_widget(headLayout)
        mainLayout.add_widget(bottomLayout)
        return mainLayout


if __name__ == '__main__':
    TestApp().run()
