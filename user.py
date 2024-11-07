# Функции:
# Классы: Товар, Заказ, Пользователь, Корзина.
# Товар содержит название, описание, цену и количество на складе.
# Корзина позволяет добавлять и удалять товары, а также вычислять итоговую сумму.
# Пользователь может создавать заказ, добавлять товары в корзину, оплачивать.
# Дополнительно: Реализуйте скидки для VIP-пользователей, историю покупок
# а также уведомления о доступности товара

class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Cart:
    def __init__(self):
        self.total_price = 0
        self.all_products = []

    def add_to_cart(self, product, quantity=1):
        self.all_products.append({'product': product, 'quantity': quantity})
        for item in self.all_products:
            print(f"add Product: {item['product'].name}, Quantity: {item['quantity']}")

    def del_to_cart(self, product):
        self.all_products = [i for i in self.all_products if i['product'] != product]
        for item in self.all_products:
            print(f"del Product: {item['product'].name}, Quantity: {item['quantity']}")

    def calculate_total(self):
        return sum(item['product'].price * item['quantity'] for item in self.all_products)

class Order:
    def __init__(self, user, total, date, items):
         self.user = user
         self.total = total
         self.date = date
         self.items = items
         self.status = 'not pay'

    def pay(self):
        self.status = 'pay'



# Пользователь может создавать заказ, добавлять товары в корзину, оплачивать.
class User:
    def __init__(self, name, isvip = False):
        self.name = name
        self.isvip = isvip
        self.order_history = []
        self.cart = Cart()

    def create_order(self):
        total = self.cart.calculate_total()
        print(total)
        if self.isvip:
            total *= 0.9
        order = Order(self.name, total, 2024, self.cart.all_products)
        self.order_history.append(order)
        self.cart = Cart()
        return order

    def view_history(self):
        for i in self.order_history:
            print(f'Information order\n User {i.user} Summa {i.total} Day order {i.date}  Items: {[(item["product"].name, item["quantity"]) for item in order.items]}  \n ======================================')




p = Product("apple", "яблоко", 50, 6)
u = User('AK')
u.cart.add_to_cart(p, 2)  # Add 2 apples to the cart

order = u.create_order()
order.pay()
u.view_history()

print(order.status, order.total)