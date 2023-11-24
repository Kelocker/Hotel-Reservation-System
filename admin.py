import function
import json
import room
import sys
from datetime import datetime

import admin_search


'''
Function in admin.py
1) view_admin 
2) add_admin 
3) remove_admin
'''

current_admin = function.user_name()












#Funciton to view all admin
def view_admin():
    function.header_topic('Admin list')

    #read food_menu.txt and print all the options
    with open('admin_database.txt', 'r') as file:
        list = file.readlines()
        for num, data in enumerate(list, start=1):
            admin = json.loads(data)
            print(num, admin['username'])






#Function to add admin
def add_admin():
    function.header_topic('Add Admin')
    with open('admin_database.txt','a') as file:
        details = {}
        #ask for username
        details['username'] = function.prompt_user_for_input(function.username_validation,'Enter the username of new admin:', 'Username has already been taken').lower()

        #ask for password
        while 1:
                new_password = function.prompt_user_for_input \
        (function.password_validation,
            "Create a Password with a combination of Upper-Lower Letter, number and symbol. Minimum 8-Character \nCreate a Password:",
            "Password should consist of Upper-Lower Letter, number and symbol\n")

                re_type_password = input("Retype your password: ")

                if new_password == re_type_password:
                    break
                else:
                    print("Passwords do not match. Please try again.")
                    return

        details['password'] = new_password

        json.dump(details, file)
        file.write('\n')
        return
#TODO couldnot run for add admin


#Function to remove admin
def remove_admin():
    function.header_topic('Remove Admin')

    #ask the name of admin to remove
    while True:
        remove_admin = input("Enter the username to remove: ").lower()
        if remove_admin == current_admin:
            print("You can't remove your own username")
        else:
            break


    #remove the adimin if found
    with open('admin_database.txt', 'r+') as file:
        new_list = []
        found = False
        for line in file:
            data = json.loads(line)
            if data['username'] == remove_admin:
                print(f"{remove_admin} found and removed.")
                found = True

            else:
                new_list.append(line)

        if found:
            file.seek(0)
            file.writelines(new_list)
            file.truncate()
            return
        else:
            print(f"'{remove_admin}' not found.")
            return



#TODO jump back to admin modification couldnot run for remove admin
def admin_modification():
    while True:
        function.header_topic("Admin Modification")
        print("For View All Admin Type [V]")
        print("For Add Admin Modified  [A]")
        print("For Remove Admin        [R]")
        print("Exit Back               [E]")

        ans = function.prompt_user_for_input(function.check_option('vare'), "Please insert: ", "Invalid Option\n").lower()


        if ans.lower() == "v":
            view_admin()
        elif ans.lower() == "a":
            add_admin()
        elif ans.lower() == "r":
            remove_admin()
        else:
            return


'''Content start here'''
def generate_hotel_record():
    function.header_topic('Record')
    ans = function.prompt_user_for_input(function.number_symbol_restrictor,

                                         "Please enter the username that you want to generate a record for:",

                                         "Invalid option").lower()

    found = False

    with open('log.txt', 'r') as file:

        for line in file:

            data_list=json.loads(line)

            today = datetime.now()
            checkout_string = data_list["Checkout date"]
            date_format = "%d/%m/%Y"
            checkout_datetime = datetime.strptime(checkout_string, date_format)
            

            if data_list['username'] == ans and checkout_datetime <= today:



                for x, y in data_list.items():

                    print(x,':', y, end= ', ')

                    found = True
                print('\n')

                       

        if not found:

            print("No record found!")




def generate_bills():
    function.header_topic("Generate Bill")
    print("Room Booking Bill   [R]")
    print("Food Bill           [F]")
    ans = function.prompt_user_for_input(function.check_option("rf"),"Please insert which bill do you want to generate:","[B]for room booking bill,[R] for restaurant bill").lower()
    if ans =="r":
        room_booking_bill()
    else:
        restaurant_bill()


def room_booking_bill():
    ans = function.prompt_user_for_input(function.number_symbol_restrictor,

                                         "Please enter the username that you want to generate a bill for:",

                                         "Invalid option")

    with open('log.txt', 'r') as file:

        records = []

        for line in file:

            data_list = json.loads(line)

            # append records into a list that matches the username

            if data_list['username'] == ans:
                records.append(data_list)

        for num, details in enumerate(records, start=1):
            print(
                f'{num:<3}ID: {details["Booking id"]:7}Booking date: {details["Booking date"]}')

        def validation(ans):

            return ans.isdigit() and (int(ans) - 1) in range(len(records))

        if records:

            # ask for which bill to generate

            answer = int(function.prompt_user_for_input(validation,
                                                        'PLease enter the respective number of bill you want to generate: ',
                                                        'Invalid option\n'))

            selected_bill = records[answer - 1]

            # print the bill

            function.header_topic('Room booking bill')

            key = ['username', 'full name', 'Booking id', 'Room type', 'total price']

            for i in key:
                print(f"{i:15}: {selected_bill[i]}")


        else:

            print("No record found")

        ans = function.prompt_user_for_input(function.check_option('yn'), "Do you want to continue?[Y/N]:",

                                             "Invalid option.").lower()

        if ans == "y":

            return

        else:

            exit()

def restaurant_bill():
    ans = function.prompt_user_for_input(function.number_symbol_restrictor,"Please enter username that you want to generate:","Invalid username.")

    with open('food_order.txt', 'r') as file:
        records = []
        for line in file:
            data_list = json.loads(line)

            #append records into a list that matches the username
            if data_list['username'] == ans:
                records.append(data_list)

        for num, details in enumerate(records, start=1):
            print(f'{num:<3} Order time: {details["time"]} Total price: {details["total price"]}')

        def validation(ans):
            return ans.isdigit() and (int(ans) - 1) in range(len(records))

        if records:
            #ask for which bill to generate
            answer = int(function.prompt_user_for_input(validation, 'PLease enter the respective number of bill you want to generate: ', 'Invalid option\n'))

            selected_bill = records[answer - 1]

            #print the bill
            function.header_topic('Restaurant bill')
            print(f"Username: {selected_bill['username']}\nTime: {selected_bill['time']}\n{'-' * 50}\n{'Food ordered':30} {'price':<6}    quanitty\n")

            with open('food_menu.txt') as file:
                food_price = {}
                for line in file:
                    data = json.loads(line)
                    food_price.update(data)

            for i in selected_bill['order']:

                print(f'{i:30} ({food_price[i]:6}) : {selected_bill["order"][i]}')


            print(f'{"-" * 50}\n{"Total Price":30}: {selected_bill["total price"]}')


        else:
            print("No record found")

        ans = function.prompt_user_for_input(function.check_option('yn'), "Do you want to continue?[Y/N]:",
                                                "Invalid option.").lower()
        if ans == "y":
            return
        else:
            exit()









def modify_room_page():
    while True:
        function.header_topic("Modify Room")
        print("Upload Room Detail         [U]")
        print("Add Room                   [A]")
        print("Delete Room                [R]")
        print("View all room              [V]")
        print("Exit Back                  [E]")

        ans = function.prompt_user_for_input(function.check_option('uarve'), "Please insert: ",
                                             "Invalid option").lower()

        if ans == "u":
            room.upload_room_detail()
        elif ans == "a":
            room.room_add_interface()
        elif ans == "r":
            room.room_deletion_interface()
        elif ans == "v":
            room.view_room_type()
        else:
            return

def adminpage():
    while True:
        function.header_topic('Admin page')
        function.welcome_user()

        interface = ("\n[A]For Admin Modified    \n[M]For Room Modified     \n[B]Booking          \n[G]Generate Bills        \
                     \n[R]For Generate Hotel Records    \n[T]For Terminate System  \n[L]For Logout            \nPlease insert:")

        ans = function.prompt_user_for_input(function.check_option('ambgrtl'),
                                             interface,"Invalid option\n").lower()

        if ans == "a":
            admin_modification()
        elif ans == "m":
            modify_room_page()
        elif ans == "b":
            admin_search.admin_booking()
        elif ans == "g":
            generate_bills()
        elif ans == "r":
            generate_hotel_record()
        elif ans == "t":
            print("Program closing.....")
            print("Goodbye")
            sys.exit()
        else:
            print("Exiting the admin page...")
            return





