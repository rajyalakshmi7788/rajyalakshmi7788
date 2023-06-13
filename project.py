class FoodItem:
    def __init__(self, food_id, name, quantity, price, discount, stock):
        self.food_id = food_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

    def __str__(self):
        return f"FoodID: {self.food_id}, Name: {self.name}, Quantity: {self.quantity}, Price: {self.price}, " \
               f"Discount: {self.discount}, Stock: {self.stock}"
class Menu:
    def __init__(self):
        self.food_items = []

    def add_food_item(self, name, quantity, price, discount, stock):
        food_id = len(self.food_items) + 1  
        food_item = FoodItem(food_id, name, quantity, price, discount, stock)
        self.food_items.append(food_item)
        return food_item

    def edit_food_item(self, food_id, name, quantity, price, discount, stock):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                food_item.name = name
                food_item.quantity = quantity
                food_item.price = price
                food_item.discount = discount
                food_item.stock = stock
                return True
        return False

    def remove_food_item(self, food_id):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                self.food_items.remove(food_item)
                return True
        return False

    def view_all_food_items(self):
        for food_item in self.food_items:
            print(food_item)
menu = Menu()

food_item1 = menu.add_food_item("Pizza", "Large", 15.99, 0.2, 10)
food_item2 = menu.add_food_item("Burger", "Single", 7.99, 0.1, 20)
food_item3 = menu.add_food_item("Salad", "Regular", 6.99, 0, 15)

menu.edit_food_item(food_item2.food_id, "Cheeseburger", "Single", 8.99, 0.15, 15)

menu.view_all_food_items()
menu.remove_food_item(food_item3.food_id)

class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.order_history = []

    def place_new_order(self):
        print("Place New Order:")
        food_items = [
            {"name": "Tandoori Chicken", "quantity": "4 pieces", "price": 240},
            {"name": "Vegan Burger", "quantity": "1 Piece", "price": 320},
            {"name": "Truffle Cake", "quantity": "500gm", "price": 900}
        ]
        print("Food Menu:")
        for index, item in enumerate(food_items, 1):
            print(f"{index}. {item['name']} ({item['quantity']}) [INR {item['price']}]")
        selection = input("Enter the numbers of the items you want to order (separated by commas): ")
        selected_items = [food_items[int(i)-1] for i in selection.split(",")]
        print("Selected Items:")
        for item in selected_items:
            print(f"{item['name']} ({item['quantity']}) [INR {item['price']}]")
        place_order = input("Do you want to place the order? (yes/no): ")
        if place_order.lower() == "yes":
            self.order_history.append(selected_items)
            print("Order placed successfully!")
        else:
            print("Order canceled.")

    def show_order_history(self):
        print("Order History:")
        for index, order in enumerate(self.order_history, 1):
            print(f"Order {index}:")
            for item in order:
                print(f"{item['name']} ({item['quantity']}) [INR {item['price']}]")

    def update_profile(self):
        print("Update Profile:")
        self.full_name = input("Enter your full name: ")
        self.phone_number = input("Enter your phone number: ")
        self.email = input("Enter your email: ")
        self.address = input("Enter your address: ")
        print("Profile updated successfully!")


def register():
    print("Register:")
    full_name = input("Enter your full name: ")
    phone_number = input("Enter your phone number: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    password = input("Enter your password: ")
    return User(full_name, phone_number, email, address, password)


def login(users):
    print("Log in:")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    for user in users:
        if user.email == email and user.password == password:
            return user
    return None


def main():
    users = []
    while True:
        print("\n--- Welcome to the Restaurant App ---")
        print("1. Register\n2. Log in\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            user = register()
            users.append(user)
            print("Registration successful!")
        elif choice == "2":
            user = login(users)
            if user:
                print(f"Logged in as {user.full_name}!")
                while True:
                    print("\n--- Main Menu ---")
                    print("1. Place New Order\n2. Order History\n3. Update Profile\n4. Log out")
                    option = input("Enter your option: ")
                    if option == "1":
                        user.place_new_order()
                    elif option == "2":
                        user.show_order_history()
                    elif option == "3":
                        user.update_profile()
                    elif option == "4":
                        break
                    else:
                        print("Invalid option!")
            else:
                print("Invalid email or password!")
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

    print("Thank you for using the Restaurant App!")


if __name__ == "__main__":
    main()

