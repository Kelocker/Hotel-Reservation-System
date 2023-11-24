import function
import json
from datetime import datetime

'''
Function in food.py
1) view_food_menu()
2) order_food() incomplete
3) modify_food_menu() incomplete
'''



#in-file function list
def check_digit(ans):
    try:
        ans = float(ans)
        if ans > 0.0:
            return True
    except ValueError:
        pass
    return False

with open('tempfile.txt', 'r') as file:
    current_user = file.readline()


#=======================================================================================================================
#Content


#FUNCTION to view food menu
#Input: NO
#Output: dict of all options e.g. ("100": {"Salad": 8})
def view_food_menu():
    function.header_topic('Food menu')

    #read food_menu.txt and print all the options
    with open('food_menu.txt', 'r') as file:
        list = {}
        i = 100
        for menu in file:
            item = json.loads(menu)
            for name in item:
                if name == 'restaurant':
                    print(f"\n{item['restaurant']}\n")

                else:
                    print(f'{i:5} {name:25} {item[name]:.2f}')
                    list[str(i)] = [name, item[name]]
                    i += 1
        return list







#FUNCTION to order food
#No input
#OUTPUT:
def order_food():
    #View menu and load all options into foods
    foods = view_food_menu()

    #Ask if the customer want to order food, if not, return
    option = function.prompt_user_for_input(function.check_option('yn'), '[Y] to proceed to order page or [N] to homepage: ', 'Invalid option')

    #TODO: which page to direct to if customer choose [N]
    if option == 'n':
        return

    function.header_topic('Order page')


    def food_validation(ans):
        return ans.lower() == 'c' or ans in foods




    #Ask customer for ordering
    cus_food = {}
    while True:
        # ask for numbering of food for order
        option = function.prompt_user_for_input(food_validation, 'Order by entering the respective number of food or press [c] to checkout: ', 'Invalid option\n')

        if option.lower() == 'c':
            break

        #ask the quantity of food
        quantity = int(function.prompt_user_for_input(check_digit, 'Enter the quantity of food: ', 'Invalid option\n'))
        if option in cus_food:
            cus_food[option] += quantity
        else:
            cus_food[option] = quantity


        #checkout interface
    function.header_topic('Checkout Page')
    print('You have ordered:\n ')

    order = {}
    #print the foods ordered and quantity
    for i in cus_food:
        food_ordered = foods[i][0]
        food_quantity = cus_food[i]
        print(f'{food_ordered:25} : {food_quantity}')
        order[food_ordered] = food_quantity






    #calculate the total price
    total = 0
    for i in cus_food:
        price = foods[i][1]
        total += price * float(cus_food[i])
    total = round(total, 2)
    print(f'\nTotal price: {total:.2f}')

    ans = function.prompt_user_for_input(function.check_option('yn'), "Confirm your order, [Y] for yes or [N] for no: ", 'Invalid option')



    if ans.lower()== 'y':
        print("Your order has been sent to restaurant")

        #save the customer order into food_order.txt
        with open('food_order.txt', 'a') as file:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cus_order = {

                "username": current_user,
                "time": current_time,
                "order": order,
                "total price": total
            }
            json.dump(cus_order, file)
            file.write('\n')
    else:
        #TODO: which page to direct if customer choose [N]
        pass






def modify_food_menu():

    function.header_topic("Modify Menu")

    number = {}
    lists = []
    with open('food_menu.txt', 'r+') as file:

        #print the name of restaurant
        for num, data in enumerate(file, start=1):
            menu = json.loads(data)
            print(num, menu['restaurant'])
            number[num] = menu['restaurant']
            lists.append(menu)
        print('\n')

        #validation for restaurant options
        def restaurant_validation(ans):
            restaurant = [str(num) for num in number]
            return ans in restaurant



        option = int(function.prompt_user_for_input(restaurant_validation, 'Which restaurant menu you wish to view (Insert Number): ', 'Invalid option insert number\n'))

        #new menu to replace the previous content in text file
        new_list = []
        changes = False

        function.header_topic(f'{number[option]} menu')

        for data in lists:
            if number[option] == data['restaurant']:
                for food in data:
                    print(f"{food:25} {data[food]}")
                option2 = function.prompt_user_for_input(function.check_option('arb'), '[A] to add, [R] to remove or [B] to back: ', 'Invalid option')

                #Add food option
                if option2.lower() == 'a':

                    #Ask for new food and price
                    new_food = input("Name:  ").lower()
                    new_price = float(function.prompt_user_for_input(check_digit, 'Price: ', 'Only numeric value'))
                    data[new_food] = new_price
                    new_list.append(data)
                    changes = True
                    print(f'{new_food} has been added')


                #Remove food option
                elif option2.lower() == 'r':

                    def remove_validation(ans):

                        return ans in [i.lower() for i in data.keys() if i != 'restaurant']



                    remove_food = function.prompt_user_for_input(remove_validation, 'Item to remove: ', 'Invalid option')
                    remove_key = ''

                    for i in data.keys():
                        if i.lower() == remove_food.lower():
                            remove_key = i
                    del data[remove_key]

                    new_list.append(data)

                    changes = True

                    print(f'{remove_food} has been removed')

                #what happen if user choose back
                else:
                    return 'b'

            else:
                #Add the unodify menu back to the new list
                new_list.append(data)
        if changes:
            file.seek(0)
            for lines in new_list:
                json.dump(lines, file)
                file.write('\n')
            file.truncate()






