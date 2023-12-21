import sqlite3

CREATE_CAT_FOOD_TABLE = " CREATE TABLE IF NOT EXISTS foods (id INTERGER PROMARARY KEY, brand TEXT, name TEXT, protein INTERGER, price TEXT, size INTERGER, rating INTERGER);"

INSERT_CAT_FOOD = "INSERT INTO foods (brand, name, protein, price, size, rating) VALUES (?, ?, ?, ?, ?,?,?);"

GET_ALL_FOODS = "SELECT * FROM foods;"
GET_FOODS_BY_NAME = "SELECT * FROM foods WHERE NAME = ?;"
GET_MOST_PROTEIN_FOR_FOOD = """
SELECT * FROM foods
WHERE NAME = ?
ORDER by rating DESC
LIMIT 1;"""
REMOVE_FOOD_BY_NAME = "DELETE FROM foods WHERE name = ?;"



def connect():
    return sqlite3.connect("data.db")

def create_tables(connection):
    with connection:
        connection.execute(CREATE_CAT_FOOD_TABLE)

def add_food(connection, brand, name, protein , price, size, rating):
    with connection:
        connection.execute(INSERT_CAT_FOOD, (brand, name, protein, price, size, rating))

def get_all_foods(connection):
    with connection:
      return   connection.execute(GET_ALL_FOODS).fetchall()

def get_foods_by_name(connection, name):
    with connection:
      return connection.execute(GET_FOODS_BY_NAME, (name,)).fetchall()

def get_most_protein_for_food(connection, name):
    with connection:
        return connection.execute(GET_MOST_PROTEIN_FOR_FOOD, (name,)).fetchone()

def remove_food_by_name(connection, name):
    with connection:
        return connection.execute(REMOVE_FOOD_BY_NAME, (name,)).fetchone()

