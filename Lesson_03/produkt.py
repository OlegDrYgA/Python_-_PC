# создание класса
class Product:
    # Описание класса
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def sayName(self):
        return f'в наличии {self.name}'

    def sayPrice(self):
        return f'по цене  {self.price}'

    def sayMix(self):
        return f'В наличии есть {self.name} по цене {self.price}'