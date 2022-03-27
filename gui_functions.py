FILTER_VALUE = 0

def startSearching(instance):
    print(f"{instance.text}")


def onSoreToggle(instance):
    FILTER_VALUE = 0
    print(FILTER_VALUE)


def onNewToggle(instance):
    FILTER_VALUE = 1
    print(FILTER_VALUE)


def onPriceToggle(instance):
    FILTER_VALUE = 2
    print(FILTER_VALUE)


def onRatingToggle(instance):
    FILTER_VALUE = 3
    print(FILTER_VALUE)


def onDiscountToggle(instance):
    FILTER_VALUE = 4
    print(FILTER_VALUE)

def onOzonActive(checkbox, value):
    if value:
        print('The checkbox Ozon is active')
    else:
        print('The checkbox Ozon is inactive')

def onSberActive(checkbox, value):
    if value:
        print('The checkbox Sber is active')
    else:
        print('The checkbox Sber is inactive')

def onWildberriesActive(checkbox, value):
    if value:
        print('The checkbox Wildberries is active')
    else:
        print('The checkbox Wildberries is inactive')

def on_text(instance, value):
    print(value)