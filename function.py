import json
from datetime import datetime,timedelta

#Reusable

'''
Function in function.py
1)header_topic(topic)
2)prompt_user_for_input(condition, question, error_message)
3)symbol_checker(item)
4)number_symbol_restrictor(ans)
5)number(ans)
6)username_validation(ans)
7)password_validation(ans)
8)only_3
9)only_5
10)room_type_validation(ans)
11)data_return(filename) 
12)user_name()
13)Function to check number validation
'''



#Function to print header
def header_topic(topic):
    print(f"\n{'-'*50}")
    print(f"{topic:^50}")
    print(f"{'-'*50}\n")





#prompt user for input until condition is met
def prompt_user_for_input(condition, question, error_message):
    while 1:
        ans = input(question)
        if condition(ans):
            break
        else:
            print(error_message)
    return ans


#Function to check symbol
def symbol_checker(item):
    Symbol = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "\\", "|", ";", ":", "'", '"', ",", "<", ".", ">", "?", "/"]

    if item in Symbol:
        return True
    else:
        return False



#Function for restricting user from inputing number and symbol. Alphabet and space are allow
def number_symbol_restrictor(ans):
    if len(ans) > 0:
        if all(char.isalpha() or char.isspace() for char in ans):
            return True

        else:
            return False
    else:
        print("You are not allow to leave blank in this section")
        return False

# function to check option but only limited to alphabets
def check_option(ans):
    ans = ans.lower()
    def check(input):
        if len(input) == 1 and input.lower() in ans:
            return True
        return False
    return check


#Function for number only
def number(ans):
    if ans.isdigit() and len(ans) >0:
        return True
    return False



#Function to check if the username is unique
def username_validation(ans):
    ans = ans.lower()
    with open('customer_personal_data.txt','r') as file1:
        with open('admin_database.txt','r') as file2:
            list1 = file1.readlines()
            list2 = file2.readlines()
            all_list = list1 + list2
            for data in all_list:
                details = json.loads(data)
                if ans == details['username']:
                    return False
    return True


#Function to validate password
def password_validation(ans):

    if len(ans) >= 8:
        uppercase = False
        lowercase = False
        alphanumeric = False
        Symbols = False

        for char in ans:
            if char.isalnum():
                alphanumeric = True

            if char.isalpha():

                if char.isupper():
                    uppercase = True

                if char.islower():
                    lowercase = True

            if symbol_checker(char):

                Symbols = True
        if alphanumeric and uppercase and lowercase and Symbols:
            return True

    return False
#TODO: function for date validation

def welcome_user():
    with open("tempfile.txt", "r") as file:
        name = file.read()
        print(f"Welcome back, {name}!"+"\n")
    

def only_3(ans):
    if len(ans) == 3:
        return True
    return False

    
def only_5(ans):
    if len(ans) == 5:
        return True
    return False



def room_type_validation(ans):

    with open("room_type.txt","r") as file:

        for line in file:

            room_exists = json.loads(line.strip())

            if room_exists["Room type"] == ans.upper():

                return True    

    return False


def data_return(filename):
    try:
        #Function will try to read the data inside the text file
        with open(filename,"r") as file:
            data = [json.loads(line.strip()) for line in file]
    #Function will return empty list if there is no data in the text file
    except FileNotFoundError:
        data = []
    return data


#User name
def user_name():
    with open("tempfile.txt", "r") as user_info_file:
        name = user_info_file.read().strip()
    return name




#Function to check number validation
def phone_num_validation(ans):
    if ans.isdigit() and len(ans) >= 8:
        return True
    return False


#return days between two input dates
def dates_between(start, end):

    date_format = "%d/%m/%Y"

    start_date = datetime.strptime(start, date_format)

    end_date = datetime.strptime(end, date_format)

    dates_list = []
    # Add the start date to the list

    current_date = start_date

    while current_date < end_date:
        dates_list.append(current_date.strftime("%Y-%m-%d"))
        current_date += timedelta(days=1)


    return dates_list