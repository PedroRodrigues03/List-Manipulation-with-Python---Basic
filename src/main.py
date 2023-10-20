import package

if __name__ == "__main__":
    lists = package.create_list()
    lists_copy = package.deep_copy(lists)

    while True:
        operation = str(input("Do you want to order by name[n], price[p], category[c]? ")).strip().upper()[0]
        if operation in "N":
            ordered_by_name_list = package.order_by_name(lists_copy)
            package.through_dictinary(ordered_by_name_list)
            package.next_line()
        elif operation in "P":
            ordered_by_price_list = package.order_by_price(lists_copy)
            package.through_dictinary(ordered_by_price_list)
            package.next_line()
        elif operation in "C":
            ordered_by_category_list = package.order_by_category(lists_copy)
            package.through_dictinary(ordered_by_category_list)
            package.next_line()
        else:
            print('Invalid Option!')

        question_increase = str(input("Do you want to increase the price [y/n]? ")).strip().upper()[0]
        if question_increase in "Y":
            multiplier = int(input("By what amount do you want to increase (%)? "))
            increased_lists = package.increase(lists_copy, multiplier)
            for d in increased_lists:
                for key, value in d.items():
                    print(f'{key} : {value}', end=' | ')
                package.next_line()

        question = str(input("Do you want to exit [y/n]? ")).strip().upper()[0]
        if question in "Y":
            package.exit()
            break
