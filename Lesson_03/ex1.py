# Импорт из produkt
from produkt import Product
# Создаем продуктовый набор класса продукт
my_pohmele = Product('Водка Столичная', 2.87)
# Вот теперь и тут выводим на  печать
print(my_pohmele.sayName())
print(my_pohmele.sayPrice())
print(my_pohmele.sayMix())