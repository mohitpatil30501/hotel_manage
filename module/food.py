from database.database import DataBase


class Food:
    @staticmethod
    def fetch_data():
        food_data = []
        data = DataBase.get_food_data()
        for food in data:
            food_data.append({
                "id": food[0],
                "food_dish": food[1],
                "price": food[2]
            })
        return food_data

    @staticmethod
    def add_food():
        food_dish_name = str(input("Enter Food dish name: "))
        food_data = Food.fetch_data()
        if not any(food['food_dish'].lower() == food_dish_name.lower() for food in food_data):
            food_price = int(input("Enter Price: Rs."))
            DataBase.add_food_item(food_dish_name, food_price)
