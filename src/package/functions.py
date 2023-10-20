import copy
import os
from time import sleep

def create_list():
    """
    -> THIS FUNCTION CREATE OUR MAIN LIST OF PRODUCTS
    :param: None
    :return: A list of products called "products_list"
    """
    products_list = []

    while True:

        name = str(input("Which is the product's name? ")).strip().upper()
        price = float(input("Which is the product's price? "))
        category = str(input("Which is the product's category? ")).strip().upper()

        products_attributes = {
            'name' : name,
            'price' : price,
            'category' : category,
        }

        products_list.append(products_attributes)

        next_line()
        question = str(input("Do you want to keep adding products [y/n]? ")).strip().upper()[0]
        if question in "N":
            break
    

    return products_list

def deep_copy(list):
    """
    -> THIS FUNCTION ONLY DOES A DEEP COPY OF A LIST
    :param list: YOU MUST GIVE A LIST AS PARAMETER
    :return: A DEEP COPY OF A LIST
    """
    return copy.deepcopy(list)

def order_by_name(list):
    """
    -> THIS FUNCTION ORDER A LIST GIVEN AS PARAMETER BY THE PRODUCT'S NAME
    :param list: YOU MUST GIVE A LIST AS PARAMETER
    :return: A VARIABLE THAT CONTAINS THE LIST ORDERED BY NAME
    """
    ordered_by_name = sorted(list, key=lambda item : item['name'])
    return ordered_by_name

def order_by_price(list):
    """
    -> THIS FUNCTION ORDER A LIST GIVEN AS PARAMETER BY THE PRODUCT'S PRICE
    :param list: YOU MUST GIVE A LIST AS PARAMETER
    :return: A VARIABLE THAT CONTAINS THE LIST ORDERED BY PRICE
    """
    ordered_by_price = sorted(list, key=lambda item : item['price'])
    return ordered_by_price

def order_by_category(list):
    """
    -> THIS FUNCTION ORDER A LIST GIVEN AS PARAMETER BY THE PRODUCT'S CATEGORY
    :param list: YOU MUST GIVE A LIST AS PARAMETER
    :return: A VARIABLE THAT CONTAINS THE LIST ORDERED BY CATEGORY
    """
    ordered_by_category = sorted(list, key=lambda item : item['category'])
    return ordered_by_category

def increase(list, multiplier):
    """
    -> THIS FUNCTION INCREASE A LIST GIVEN AS PARAMETER BY A MULTIPLIER ALSO GIVEN AS PARAMETER
    :param list: YOU MUST GIVE A LIST AS PARAMETER
    :param multiplier: YOU MUST GIVE A MULTIPLIER TO OPERATE ON THE PRODUCT'S PRICE
    :return: A VARIABLE THAT IS A NEW LIST WITH PRICE INCREASED
    """
    increased_lists = [
        {**product, 'price' : round(product['price'] * ((multiplier/100) + 1), 2)}
        for product in list
    ]
    return increased_lists

def through_dictinary(list):
    """
    -> THIS FUNCTION GO DEEP THROUGH OUT LIST ITERATING WITH ALL THE PRODUCT'S ATTRIBUTES
    :param list: YOU MUST GIVE A LIST AS PARAMETER
    :return: NONE
    """
    for dictionary in list:
        for key, value in dictionary.items():
            print(f'{key} : {value}', end=' | ')
        next_line()

def exit():
    """
    -> THIS FUNCTION ALLOW THE USER TO EXIT THE PROGRAM
    :param: NONE
    :return: NONE
    """
    print('Goodbye! 🤖')
    print('Closing System. Wait.')
    sleep(3)
    os.system('clear')

def next_line():
    """
    -> THIS FUNCTION SKIP A LINE
    :param: NONE
    :return: THE FUNCTION PRINT()
    """
    return print()