from decimal import Decimal
from django.conf import settings
from shop.models import Product


def convert(price) -> str:
    res = "" 
    for i in range(len(price), 0, -1):
        if i % 3 == 0:
            res += " " + price[-i]
        else:
            res += price[-i]
    return res.lstrip()

def back(price) -> int:
    if price == "":
        return 0
    else:
        return int(price.replace(" ", ""))


class Cart(object):

    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        """
        Добавить продукт в корзину или обновить его количество.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                    'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = 1
        else:
            self.cart[product_id]['quantity'] = 1
        self.save()

    def save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Перебор элементов в корзине и получение продуктов из базы данных.
        """
        product_ids = self.cart.keys()
        # получение объектов product и добавление их в корзину
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            print(type(product))
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = item['price']
            item['name'] = item['product'].name
            item['image'] = item['product'].image
            item['image2'] = item['product'].image2
            item['image3'] = item['product'].image3
            item['image4'] = item['product'].image4
            item['id'] = item['product'].id
            item['total_price'] = item['price'] * item['quantity']
            item['url'] = item['product'].get_absolute_url()
            print(item)
            yield item

    def __len__(self):
        """
        Подсчет всех товаров в корзине.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """
        Подсчет стоимости товаров в корзине.
        """
        return convert(str(sum(back(item['price']) for item in self.cart.values())))
    
    def clear(self):
        # удаление корзины из сессии
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True