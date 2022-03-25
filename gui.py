from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from kivy.uix.boxlayout import BoxLayout


class TestApp(App):

    def build(self):

        mainLayout = BoxLayout(orientation='vertical')
        headLayout = BoxLayout(orientation='vertical', size_hint=(1, 0.2), padding=(0,0,0,5))
        bottomLayout = BoxLayout(orientation='vertical')
        filtersLayout = BoxLayout(orientation='horizontal')

        textinput = TextInput(text='Enter a request')

        search = Button(text='search')
        def startSearching(instance):
            print(f"{instance.text}")
        search.bind(on_press=startSearching)

        filters = Button(text='filters')
        shops = Button(text='shops')
        filtersLayout.add_widget(search)
        filtersLayout.add_widget(filters)
        filtersLayout.add_widget(shops)

        headLayout.add_widget(textinput)
        headLayout.add_widget(filtersLayout)

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