# 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
import openai

class Snack:
    def __init__(self, snack_id, snack_name, price, quantity):
        self.snack_id = snack_id
        self.snack_name = snack_name
        self.price = price
        self.quantity = quantity

    def update_price(self, new_price):
        self.price = new_price

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    def is_available(self):
        return self.quantity > 0

    def __str__(self):
        availability = "yes" if self.is_available() else "no"
        return f"ID: {self.snack_id}, Name: {self.snack_name}, Price: {self.price}, Availability: {availability}"


class DivineFood:
    def __init__(self, chatgpt_api_key):
        self.snacks = []
        self.sales_records = []
        self.chatgpt_api_key = chatgpt_api_key

    def add_snack(self, snack_id, snack_name, price, quantity):
        snack = Snack(snack_id, snack_name, price, quantity)
        self.snacks.append(snack)

    def remove_snack(self, snack_id):
        snack = self.find_snack(snack_id)
        if snack:
            self.snacks.remove(snack)
            return True
        return False

    def update_snack_quantity(self, snack_id, quantity):
        snack = self.find_snack(snack_id)
        if snack:
            snack.update_quantity(quantity)
            return True
        return False

    def sell_snack(self, snack_id):
        snack = self.find_snack(snack_id)
        if snack:
            if snack.is_available():
                snack.update_quantity(snack.quantity - 1)
                self.sales_records.append(snack)
                return True
            else:
                print("Snack is currently unavailable.")
        return False

    def find_snack(self, snack_id):
        for snack in self.snacks:
            if snack.snack_id == snack_id:
                return snack
        return None

    def display_snacks(self):
        if not self.snacks:
            print("No snacks available.")
        else:
            for snack in self.snacks:
                print(snack)

    def display_sales_records(self):
        if not self.sales_records:
            print("No sales records available.")
        else:
            for snack in self.sales_records:
                print(snack)

    def calculate_total_sales_price(self):
        total_price = 0.0
        for snack in self.sales_records:
            total_price += snack.price
        return total_price

    def chat_with_staff(self, message):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=message,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.7,
            api_key=self.chatgpt_api_key
        )
        return response.choices[0].text.strip()


# Example usage of DivineFood class and ChatGPT API

def display_menu():
    print("===== Divine Food Menu =====")
    print("1. Add a snack")
    print("2. Remove a snack")
    print("3. Update snack quantity")
    print("4. Sell a snack")
    print("5. Display snacks")
    print("6. Display sales records")
    print("7. Calculate total sales price")
    print("8. Exit")
    print("============================")


# Creating an instance of the DivineFood class
divine_food = DivineFood("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")

while True:
    display_menu()
    option = input("Enter an option: ")

    if option == "1":
        snack_id = int(input("Enter snack ID: "))
        snack_name = input("Enter snack name: ")
        price = float(input("Enter snack price: "))
        quantity = int(input("Enter snack quantity: "))
        divine_food.add_snack(snack_id, snack_name, price, quantity)
        print("Snack added successfully.")

    elif option == "2":
        snack_id = int(input("Enter snack ID to remove: "))
        if divine_food.remove_snack(snack_id):
            print("Snack removed successfully.")
        else:
            print("Snack not found.")

    elif option == "3":
        snack_id = int(input("Enter snack ID to update quantity: "))
        quantity = int(input("Enter new quantity: "))
        if divine_food.update_snack_quantity(snack_id, quantity):
            print("Quantity updated successfully.")
        else:
            print("Snack not found.")

    elif option == "4":
        snack_id = int(input("Enter snack ID to sell: "))
        if divine_food.sell_snack(snack_id):
            print("Snack sold successfully.")
        else:
            print("Snack not found.")

    elif option == "5":
        print("Current Snacks:")
        divine_food.display_snacks()

    elif option == "6":
        print("Sales Records:")
        divine_food.display_sales_records()

    elif option == "7":
        total_sales_price = divine_food.calculate_total_sales_price()
        print(f"Total sales price: ${total_sales_price}")

    elif option == "8":
        print("Exiting Divine Food application...")
        break

    else:
        print("Invalid option. Please try again.")





# import openai

# class Snack:
#     def __init__(self, snack_id, snack_name, price, quantity):
#         self.snack_id = snack_id
#         self.snack_name = snack_name
#         self.price = price
#         self.quantity = quantity

#     def update_price(self, new_price):
#         self.price = new_price

#     def update_quantity(self, new_quantity):
#         self.quantity = new_quantity

#     def is_available(self):
#         return self.quantity > 0

#     def __str__(self):
#         availability = "yes" if self.is_available() else "no"
#         return f"ID: {self.snack_id}, Name: {self.snack_name}, Price: {self.price}, Availability: {availability}"


# class DivineFood:
#     def __init__(self, chatgpt_api_key):
#         self.snacks = []
#         self.sales_records = []
#         self.chatgpt_api_key = chatgpt_api_key

#     def add_snack(self, snack_id, snack_name, price, quantity):
#         snack = Snack(snack_id, snack_name, price, quantity)
#         self.snacks.append(snack)

#     def remove_snack(self, snack_id):
#         snack = self.find_snack(snack_id)
#         if snack:
#             self.snacks.remove(snack)
#             return True
#         return False

#     def update_snack_quantity(self, snack_id, quantity):
#         snack = self.find_snack(snack_id)
#         if snack:
#             snack.update_quantity(quantity)
#             return True
#         return False

#     def sell_snack(self, snack_id):
#         snack = self.find_snack(snack_id)
#         if snack:
#             if snack.is_available():
#                 snack.update_quantity(snack.quantity - 1)
#                 self.sales_records.append(snack)
#                 return True
#             else:
#                 print("Snack is currently unavailable.")
#         return False

#     def find_snack(self, snack_id):
#         for snack in self.snacks:
#             if snack.snack_id == snack_id:
#                 return snack
#         return None

#     def display_snacks(self):
#         if not self.snacks:
#             print("No snacks available.")
#         else:
#             for snack in self.snacks:
#                 print(snack)

#     def display_sales_records(self):
#         if not self.sales_records:
#             print("No sales records available.")
#         else:
#             for snack in self.sales_records:
#                 print(snack)

#     def chat_with_staff(self, message):
#         response = openai.Completion.create(
#             engine="text-davinci-003",
#             prompt=message,
#             max_tokens=50,
#             n=1,
#             stop=None,
#             temperature=0.7,
#             api_key=self.chatgpt_api_key
#         )
#         return response.choices[0].text.strip()


# # Example usage of DivineFood class and ChatGPT API

# def display_menu():
#     print("===== Divine Food Menu =====")
#     print("1. Add a snack")
#     print("2. Remove a snack")
#     print("3. Update snack quantity")
#     print("4. Sell a snack")
#     print("5. Display snacks")
#     print("6. Display sales records")
#     print("7. Exit")
#     print("============================")


# # Creating an instance of the DivineFood class
# divine_food = DivineFood("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")

# while True:
#     display_menu()
#     option = input("Enter an option: ")

#     if option == "1":
#         snack_id = int(input("Enter snack ID: "))
#         snack_name = input("Enter snack name: ")
#         price = float(input("Enter snack price: "))
#         quantity = int(input("Enter snack quantity: "))
#         divine_food.add_snack(snack_id, snack_name, price, quantity)
#         print("Snack added successfully.")

#     elif option == "2":
#         snack_id = int(input("Enter snack ID to remove: "))
#         if divine_food.remove_snack(snack_id):
#             print("Snack removed successfully.")
#         else:
#             print("Snack not found.")

#     elif option == "3":
#         snack_id = int(input("Enter snack ID to update quantity: "))
#         quantity = int(input("Enter new quantity: "))
#         if divine_food.update_snack_quantity(snack_id, quantity):
#             print("Quantity updated successfully.")
#         else:
#             print("Snack not found.")

#     elif option == "4":
#         snack_id = int(input("Enter snack ID to sell: "))
#         if divine_food.sell_snack(snack_id):
#             print("Snack sold successfully.")
#         else:
#             print("Snack not found.")

#     elif option == "5":
#         print("Current Snacks:")
#         divine_food.display_snacks()

#     elif option == "6":
#         print("Sales Records:")
#         divine_food.display_sales_records()

#     elif option == "7":
#         print("Exiting Divine Food application...")
#         break

#     else:
#         print("Invalid option. Please try again.")
