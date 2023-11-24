import function
import newcus
import time
import existingcustomer
import json
import admin
import room


#Function to check input of user for type of end user

def end_user(ans):
    if len(ans) == 1 and ans.lower() in ("ln"):
        return True
    return False


# login page
def login_page():
    print("\n\nAdmin login page\n")

    # Ask for username
    name = input('User name:')

    # Ask for password
    password = input("password: ")


#Function to check input of user for term and condition
def term_and_condition_option(ans):
    if len(ans) == 1 and ans.lower() in ("ad"):
        return True
    return False


def new_customer_option(ans):
    if len(ans) == 1 and ans.lower() in ("rne"):
        return True
    return False

#Password
def username_and_password(username, password):
    with open("admin_database.txt", "r") as admin_file:
        for line in admin_file:
            data = json.loads(line)
            if username == data['username'] and password == data['password']:
                return True, 'admin'

    with open("customer_personal_data.txt", "r") as file:
        for line in file:
            data = json.loads(line)
            if username == data['username'] and password == data['password']:
                return True, 'customer'
        
    return False, None



#=======================================================================================================================
#Content


def main_menu():
    while True:

        function.header_topic("Welcome to random hotel")

        print("Dear user,")
        print("For log-in please type       [L]")
        print("For New Customer please type [N]")
        
        

        # Determine identity of user and direct them to respective login page

        ans = function.prompt_user_for_input(function.check_option('ln'), "Please insert: ", "[L] for log-in and [N] for new customer\n").lower()


        if ans.lower() == "l":
            login_window()
            
        else:
            new_customer_interface()
            



    
    




def new_customer_interface():

    
    function.header_topic("New Customer Page")


    print("Dear user,")
    print("For New Registration please   type [N]")
    print("For room details please       type [R]")
    print("For Exit please               type [E]")

    
    ans = function.prompt_user_for_input(function.check_option('nre'), "Please insert: ", "Type [N] for new registration, type [R] for room details or [E] for exit\n").lower()


    if ans == "n":
        newcus.new_customer_registration_window()
    elif ans == "r":
        function.header_topic("Room Type")
        room.view_all_room_details()
    else:
        main_menu()


def login_window():

    print("Loading.....")
    time.sleep(2)

    function.header_topic("Login Page")


    inputusername = input("Username: ").lower()
    inputpassword = input("Password: ")

    data, user = username_and_password(inputusername, inputpassword)
    
    
    if data: 
        print("Login......")
        time.sleep(1)
        print("Login successful!")
        with open("tempfile.txt", "w") as file:
                file.write(inputusername)
            
        if user == 'customer':
            existingcustomer.homepage()
        elif user == 'admin':
            admin.adminpage()
    

    else:
        print("Invalid username or password.")
        login_window()


main_menu()   



