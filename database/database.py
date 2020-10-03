import sqlite3


class DataBase:
    connection_database = sqlite3.connect('database/data.db')
    database_cursor = connection_database.cursor()

    @staticmethod
    def food_table():
        try:
            DataBase.connection_database.execute("create table Food_Data (Id INTEGER PRIMARY KEY, Food_Dish Text, "
                                                 "Price INTEGER);")
        finally:
            return True

    @staticmethod
    def add_food_item(food_name, food_price):
        DataBase.database_cursor.execute("insert into Food_Data (Food_Dish, Price) value ('" + str(food_name) + "',"
                                         + str(food_price) + ")")
        DataBase.connection_database.commit()

    @staticmethod
    def get_food_data():
        data = DataBase.database_cursor.execute("select * from Food_Data;")
        DataBase.connection_database.commit()
        return data

    def change_food_item(self):
        pass

    def delete_food_item(self):
        pass
