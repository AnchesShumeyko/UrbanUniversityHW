"""Учёт товаров"""


class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'product.txt'

    def get_product(self):
        file = open(self.__file_name, 'r')
        products_list = file.read()
        file.close()
        return print(products_list)

    def add(self, *products):
        file = open(self.__file_name, 'r+')
        text = file.read()
        self.get_product()

        for i in products:
            if i.name not in text:
                file = open(self.__file_name, 'a')
                file.write(f'{i}\n')
                file.close()
            else:
                print(f'продукт {i.name} уже есть в магазине')
                file.close()



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)
