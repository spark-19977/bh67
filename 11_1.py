import sqlite3
import csv

import pydantic


def create_table():
    connection = None
    try:
        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS category(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(50) UNIQUE,
            is_published BOOL DEFAULT(True))
            '''
        )
        cursor.close()
        connection.commit()
    except(Exception, sqlite3.Error) as err:
        print(err)
    finally:
        if connection is not None:
            connection.close()


def add_to_table(name, is_published):
    connection = None
    try:
        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()
        cursor.execute(
            '''
            INSERT INTO category(name, is_published)
            VALUES (?, ?)
            ''', (name, is_published)
        )
        cursor.close()
        connection.commit()
    except(Exception, sqlite3.Error) as err:
        print(err)
    finally:
        if connection is not None:
            connection.close()


def show_table():
    connection = None
    try:
        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()
        cursor.execute(
            '''
            SELECT name, is_published FROM category
            '''
        )
        result = cursor.fetchall()
        cursor.close()
        return result
    except(Exception, sqlite3.Error) as err:
        print(err)
    finally:
        if connection is not None:
            connection.close()


class Category(pydantic.BaseModel):
    name: str
    is_published: bool = pydantic.Field(default=True)

    @classmethod
    def from_csv(cls, filename: str) -> list['Category']:
        with open(filename, 'r', encoding='utf-8') as fh:
            reader = [*csv.DictReader(fh)]
        return [Category(**item) for item in reader]


def write_to_db(data: list[Category]):
    connection = None
    try:
        connection = sqlite3.connect('db.sqlite3')
        cursor = connection.cursor()
        cursor.executemany(
            '''
            INSERT INTO category(name, is_published)
            VALUES (?, ?)
            ''', ((category.name, category.is_published) for category in data)
        )
        cursor.close()
        connection.commit()
    except(Exception, sqlite3.Error) as err:
        print(err)
    finally:
        if connection is not None:
            connection.close()


def from_db_to_schema(db_name: str = 'db.sqlite3') -> list[Category]:
    data = show_table()
    return [Category(name=item[0], is_published=item[1]) for item in data]


# create_table()
# add_to_table('tea', True)
# add_to_table('coffe', False)
# add_to_table('cola', True)
# print(show_table())
# print(Category.from_csv('11_1.csv'))
# write_to_db(Category.from_csv('11_1.csv'))
# print(show_table())
# print(from_db_to_schema())
