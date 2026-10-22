import os
import configparser
import pandas as pd

from pgdb import PGDatabase

dirname = os.path.dirname(__file__)

config = configparser.ConfigParser()
config.read(os.path.join(dirname, "config.ini"))

DATA_DIR = os.path.join(dirname, config["Files"]["DATA_DIR"])
DB_CONFIG = dict(config["Database"])

INSERT_QUERY = """
    insert into sales (sale_date, doc_id, item, category, amount, price, discount)
    values (%s, %s, %s, %s, %s, %s, %s)
"""

def is_sales_file(file_name): # проверяет имя файла по шаблону {номер магазина}_{номер кассы}.csv
    name, extension = os.path.splitext(file_name)
    if extension != ".csv":
        return False
    parts = name.split("_")
    return len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit()

def load_file (db, file_path): # загружаем один файл
    df = pd.read_csv(file_path)
    for row in df.itertuples(index=False):
        db.post(INSERT_QUERY, row)

db = PGDatabase(**DB_CONFIG)

for file_name in sorted(os.listdir(DATA_DIR)):
    file_path = os.path.join(DATA_DIR, file_name)

    if not os.path.isfile(file_path) or not is_sales_file(file_name):
        continue

    try:
        load_file(db, file_path)
        os.remove(file_path)
        print(f"Загружен и удален фаил: {file_name}")
    except Exception as err:
        print(f"Ошибка при загрузке файла {file_name}: {err!r}")

db.close()