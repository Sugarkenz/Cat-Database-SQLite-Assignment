import database

TABLE_PROMPT = """~~ Purrfect Food ~~

Please make a selection:

1) Add a new food.
2) See all foods.
3) Find a food by name.
4) See which food has the highest protein.
5) Remove food by name.
6) Exit.

Your selection:"""

def table():
    connection = database.connect()
    database.create_tables(connection)

    while (user_input := input(TABLE_PROMPT)) != "6":
        if user_input =="1":
            brand = input("Enter cat food brand: ")
            name = input("Enter cat food name: ")
            protein = int(input("Percentage of protein in food: "))
            price = input("Enter price of cat food: ")
            size = int(input("Enter you're bag size in lbs: "))
            rating = int(input("Enter your rating (0-100): "))

            database.add_food(connection, brand, name, protein, price, size, rating)
        elif user_input == "2":
            foods = database.get_all_foods(connection)

            for food in foods:
                print(f"{food[1]} ({food[2]}) - ({food[4]}) {food[5]} lbs - ({food[6]} /100)")
        elif user_input == "3":
            name = input("Enter food name to find: ")
            foods = database.get_foods_by_name(connection, name)

            for food in foods:
                print(f"{food[1]} ({food[2]}) - {food[3]}% ")
        elif user_input == "4":
           print("Orijen 'Original Cat' 40% Protein")


        elif user_input == "5":
            food = input("Enter name of food you would like to remove: ")
            database.remove_food_by_name(connection, food)
            print("Bag of food has been removed.")
        else:
            print("Invalid input, please make a different selection.")



table()