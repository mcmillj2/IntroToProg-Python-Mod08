# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Josh McMillen,12.7.2020,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []


class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products  name
        product_price: (float) with the products standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Josh McMillen,12.7.2020,Modified code to complete assignment 8
    """

    def __init__(self, product_name: str, product_price: float):
        """  Initializes product name and value objects
        :param product_name: (string)
        :param product_price: (float)

        :return: nothing
        """
        self.__product_name = product_name
        self.__product_price = product_price

    @property
    def product_name(self):
        """  Returns product name

        :return: product name
        """
        return str(self.__product_name)

    @product_name.setter
    def product_name(self, value):
        """  Checks if product name is numeric and gives error

        :param value: (unknown)
        :return: nothing
        """
        if not str(value).isnumeric():
            self.__product_name = value
        else:
            raise Exception("Product name cannot be a number")

    @property
    def product_price(self):
        """  Returns product value

        :return: product value
        """
        return str(self.__product_price)

    @product_price.setter
    def product_price(self, value):
        """  Checks if product value is numeric and gives error if not

        :param value: (unknown)
         :return: nothing
         """
        if str(value).isnumeric():
            self.__product_price = value
        else:
            raise Exception("Product price must be a number")


# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Josh McMillen,12.7.2020,Modified code to complete assignment 8
    """

    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        """  Saves given file name and list of objects

         :param file_name: name of file to save to
         :param list_of_product_objects: object list to save
         :return: nothing
         """
        with open(file_name, 'w') as file:
            for row in list_of_product_objects:
                file.write(row.product_name + ", " + row.product_price + "\n")
            return

    @staticmethod
    def read_data_from_file(file_name):
        """  Reads from given file name

         :param file_name: name of file to read from
         :return: list_of_rows
         """
        list_of_rows = []
        with open(file_name, 'r') as file:
            for line in file:
                name, value = line.split(",")
                row = {"Name": name.strip(), "Value": value.strip()}
                list_of_rows.append(row)
            return list_of_rows


# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks:

    methods:
        print_menu_tasks():
        input_menu_choice(): -> (choice)
        print_products(list_of_rows)
        input_task_to_update(list_of_rows)
        input_yes_no_choice(message) -> (str(input(message)).strip().lower())

    changelog: (When,Who,What)
        Josh McMillen,12.7.2020,Created code to complete assignment 8
    """

    @staticmethod
    def print_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) View Current Products and Values
        2) Update Products and Values
        3) Save Data to File        
        4) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string choice
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_products(list_of_rows):
        """ Shows the current products

        :param list_of_rows: (list) of products you want to display
        :return: nothing
        """
        print()
        for row in list_of_rows:
            print("[Product Name]: " + row.product_name + " [Value]: " + row.product_price)
        print()  # Add an extra line for looks

    @staticmethod
    def input_task_to_update(list_of_rows):
        """ Goes through each row in the list_of_rows and asks user if it should be updated

        :param list_of_rows: (list) of rows you want to update
        :return: nothing
        """
        for row in list_of_rows:
            print("[Product Name]: " + row.product_name + " [Value]: " + row.product_price)
            choice = IO.input_yes_no_choice("Update Product? (y/n) - ")
            if choice.lower() == "y":
                temp_product_name = input("Product Name:")
                while True:
                    try:
                        row.product_name = temp_product_name
                    except Exception as e:
                        print(e)
                        temp_product_name = input("Product Name:")
                        continue
                    break

                temp_product_price = input("Product Value:")
                while True:
                    try:
                        row.product_price = temp_product_price
                    except Exception as e:
                        print(e)
                        temp_product_price = input("Product Value:")
                        continue
                    break
                print("Product Updated!")
                break
            else:
                continue
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()


# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts
f = FileProcessor()
obj1 = Product(f.read_data_from_file(strFileName)[0]["Name"], f.read_data_from_file(strFileName)[0]["Value"])
obj2 = Product(f.read_data_from_file(strFileName)[1]["Name"], f.read_data_from_file(strFileName)[1]["Value"])
obj3 = Product(f.read_data_from_file(strFileName)[2]["Name"], f.read_data_from_file(strFileName)[2]["Value"])
obj4 = Product(f.read_data_from_file(strFileName)[3]["Name"], f.read_data_from_file(strFileName)[3]["Value"])
lstOfProductObjects.clear()
lstOfProductObjects = [obj1, obj2, obj3, obj4]

while True:
    IO.print_menu_tasks()  # Show user a menu of options
    strChoice = IO.input_menu_choice()  # Get user's menu option choice

    if strChoice.strip() == '1':  # Show user current data in the list of product objects
        IO.print_products(lstOfProductObjects)
        continue  # to show the menu

    elif strChoice == '2':  # Let user add data to the list of product objects
        IO.input_task_to_update(lstOfProductObjects)
        continue  # to show the menu

    elif strChoice == '3':  # let user save current data
        f.save_data_to_file(strFileName, lstOfProductObjects)
        print("Data Saved!")
        continue  # to show the menu

    elif strChoice == '4':  # let user exit program
        print("Goodbye!")
        break  # and Exit
