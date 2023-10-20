import copy
import os
from time import sleep

def creat_list():
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
    return copy.deepcopy(list)

def order_by_name(list):
    ordered_by_name = sorted(list, key=lambda item : item['name'])
    return ordered_by_name

def order_by_price(list):
    ordered_by_price = sorted(list, key=lambda item : item['price'])
    return ordered_by_price

def order_by_category(list):
    ordered_by_category = sorted(list, key=lambda item : item['category'])
    return ordered_by_category

def increase(list, multiplier):
    increased_lists = [
        {**product, 'price' : round(product['price'] * ((multiplier/100) + 1), 2)}
        for product in list
    ]
    return increased_lists

def through_dictinary(list):
    for dictionary in list:
        for key, value in dictionary.items():
            print(f'{key} : {value}', end=' | ')
        next_line()

def exit():
    print('Goodbye! 🤖')
    print('Closing System. Wait.')
    sleep(3)
    os.system('clear')

def next_line():
    return print()