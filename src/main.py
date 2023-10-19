import package

if __name__ == "__main__":
    lists = package.creat_list()
    lists_copy = package.deep_copy(lists)

    while True:
        operation = str(input("Do you want to order by name[n], price[p], category[c]? ")).strip().upper()[0]
        if operation in "N":
            ordered_by_name_list = package.order_by_name(lists_copy)
            for dictionary in ordered_by_name_list:
                for key, value in dictionary.items():
                    print(f'{key} : {value}', end=' | ')
                package.next_line()
        elif operation in "P":
            ordered_by_price_list = package.order_by_price(lists_copy)
            for dicti in ordered_by_price_list:
                for key, value in dicti.items():
                    print(f'{key} : {value}', end=' | ')
                package.next_line()
        elif operation in "C":
            ordered_by_category_list = package.order_by_category(lists_copy)
            for dic in ordered_by_category_list:
                for key, value in dic.items():
                    print(f'{key} : {value}', end=' | ')
                package.next_line()
        else:
            print('Invalid Option!')

        question = str(input("Do you want to exit [y/n]? ")).strip().upper()[0]
        if question in "Y":
            package.exit()
            break
