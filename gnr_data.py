import os
from datetime import date, timedelta

import pandas as pd
from random import randint

# Константы
SHOPS_COUNT = 5  # N - количество магазинов
MAX_CASHES_PER_SHOP = 3  # у каждого магазина от 1 до этого числа касс
MIN_RECEIPTS = 3  # чеков в одной выгрузке: от и до
MAX_RECEIPTS = 10
MAX_ITEMS_IN_RECEIPT = 5  # товарных строк в одном чеке: от 1 до этого числа
DISCOUNT = 0  # сумма скидки на позицию

dirname = os.path.dirname(__file__)
data_dir = os.path.join(dirname, "data")
dt = (date.today() - timedelta(days=1)).isoformat()

COLUMNS = ["date", "doc_id", "item", "category", "amount", "price", "discount"]

# Создадим каталог товаров
CATALOG = {
    "бытовая химия": [
        ("Стиральный порошок", 550),
        ("Средство для мытья посуды", 160),
        ("Гель для стирки", 720),
        ("Чистящее средство для ванной", 280),
    ],
    "текстиль": [
        ("Полотенце банное", 850),
        ("Комплект постельного белья", 3200),
        ("Плед флисовый", 1400),
        ("Штора для ванной", 950),
    ],
    "посуда": [
        ("Сковорода", 2300),
        ("Набор кастрюль", 5500),
        ("Тарелка обеденная", 320),
        ("Кружка", 250),
    ],
    "хранение": [
        ("Контейнер пищевой", 380),
        ("Корзина для белья", 1300),
        ("Органайзер для ящика", 450),
    ],
}


def generate_rows(shop_num, cash_num):  # Генерирует все строки одной выгрузки, одной кассы.
    rows = []
    categories = list(CATALOG.keys())

    receipts_count = randint(MIN_RECEIPTS, MAX_RECEIPTS)
    for receipt_num in range(1, receipts_count + 1):
        doc_id = f"DOC{shop_num}-{cash_num}-{receipt_num:04d}"  # собираем номер чека, последний идентификатор выравниваем

        items_count = randint(1, MAX_ITEMS_IN_RECEIPT) # создаем случайное количество строк в чеке
        for _ in range(items_count):
            category = categories[randint(0, len(categories) - 1)]
            products = CATALOG[category]
            item, price = products[randint(0, len(products) - 1)]

            amount = randint(1, 5)

            rows.append([dt, doc_id, item, category, amount, price, DISCOUNT])

    return rows

os.makedirs(data_dir, exist_ok=True) 

for shop_num in range(1, SHOPS_COUNT + 1): # генерируем список магазинов
    cashes_count = randint(1, MAX_CASHES_PER_SHOP) # генерируем случайное количество, работающих в этот раз, касс для каждого магазина
    for cash_num in range(1, cashes_count + 1): # для каждой кассы генерируем чеки с помощью generate_rows
        rows = generate_rows(shop_num, cash_num)
        df = pd.DataFrame(rows, columns=COLUMNS)

        file_name = f"{shop_num}_{cash_num}.csv"
        df.to_csv(os.path.join(data_dir, file_name), index=False, encoding="UTF-8")