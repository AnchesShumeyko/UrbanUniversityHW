import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()


def initiate_db():
    with connection:
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Products(
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
            )
            """)
        connection.commit()
    # connection.close()


def get_all_products():
    all_products = []
    with connection:
        cursor.execute('''
        SELECT * FROM Products
        ''')
        products = cursor.fetchall()
        return products




def add_products(new_product):
    with connection:
        for item in new_product:
            product_id = item.get('id')
            title = item.get('title')
            description = item.get('description')
            price = item.get('price')

            check_product = cursor.execute('SELECT * FROM Products WHERE title = ?', (title,))
            if check_product.fetchone() is None:
                sql_request = f"INSERT OR IGNORE INTO Products(id, title, description, price) VALUES(?,?,?,?);"
                cursor.execute(sql_request, (product_id, title, description, price))

            connection.commit()


if __name__ == '__main__':

    initiate_db()
    new_products = [
        {
            'id': 1,
            'title': 'Vit_A',
            'description': 'Ретинола Ацетата Драже 30 шт',
            'price': 40
        },
        {
            'id': 2,
            'title': 'Vit_D',
            'description': 'Витамин Д3 2000 МЕ капс. 120 шт',
            'price': 1200
        },
        {
            'id': 3,
            'title': 'Vit_E',
            'description': 'Витамин Е 150мг Премиум капсулы №30',
            'price': 130
        },
        {
            'id': 4,
            'title': 'Vit_K',
            'description': 'Витамин К2 натуральный 120 мкг Капсулы 570 мг 30шт',
            'price': 637
        }
    ]
    add_products(new_products)

    for i in get_all_products():
        print(i)


