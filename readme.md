# project-sales-etl

## Как запустить

1. Установите Python и PostgreSQL.
2. Скачайте проект и перейдите в его папку:
   ```
   git clone <ссылка на репозиторий>
   cd project-sales-etl
   ```
3. Создайте окружение и установите библиотеки:
   ```
   python -m venv venv
   venv\Scripts\python.exe -m pip install -r requirements.txt
   ```
4. Создайте базу данных: `CREATE DATABASE sales_db;`
5. В этой базе выполните файл `sql/create_tables.sql`.
6. В `config.ini`  впишите свой пароль от PostgreSQL и другие необходимые данные.
7. Создайте файлы выгрузки и загрузите их в базу:
   ```
   venv\Scripts\python.exe gnr_data.py
   venv\Scripts\python.exe load_data.py
   ```

**Важно:** после записи в базу файлы .csv удаляются из папки `data`.

## Можно настроить автозапуск через Планировщик заданий Windows или Cron


