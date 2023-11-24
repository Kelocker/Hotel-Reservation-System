import function
import time
import json
import datetime

#function list

#Function to check gender validation
def gender_validation(ans):
    if len(ans) == 1 and ans.lower() in ("mf"):
        return True
    return False


#date of birth validation
def validate_date(ans):
    try:
        datetime.datetime.strptime(ans, '%d/%m/%Y')

        day, month, year = map(int, ans.split('/'))

        today = datetime.date.today()
        date_of_birth = datetime.date(year, month, day)
        age = today.year - date_of_birth.year

        if date_of_birth >= today:
            return False,"Invalid date of birth"
        if age <18:
            return False,"You are not allow to registered under 18 years old"

        return True, None
    except ValueError:
        return False,"Invalid date format."




#Function to check email format
def email_format(ans):
    if "@" in ans:
        front, back = ans.split("@")
        if front and back and "." in back and back[0] != "." and ans[-1] != ".":
            return True

    return False








#=======================================================================================================================
#Content 



def new_customer_registration_window():

    function.header_topic("New Customer Registration")

    print("Personal Information")


    # Ask New Customer for full name
    new_customer_Full_name = function.prompt_user_for_input\
        (function.number_symbol_restrictor, "Full name: ", "Only alphabet in name\n")



    # Ask New Customer for Gender
    new_customer_gender = function.prompt_user_for_input(gender_validation, "Gender ([M] for male, [F] for female]): ", "Type [M] for Male Type [F] for Female\n")


    # Ask New Customer for Date of Birth
    while True:
        new_customer_date_of_birth = input("Date of birth (DD/MM/YYYY): ")
        valid, error_message = validate_date(new_customer_date_of_birth)

        if valid:
            break

        else:
            print("Error:", error_message)


    # Ask New Customer for E-mail
    new_customer_email = function.prompt_user_for_input(email_format, "Email: ", "Invalid email format\n")

    


    # Ask New Customer for Contact Number
    new_customer_contact_number = function.prompt_user_for_input\
        (function.phone_num_validation, "Contact Number (Example: 01xxxxxxxxx) :", "Invalid Contact Number\n")



    function.header_topic("Emergency Contact")

    # Ask New Customer for Relation with the Emergency contact number
    new_customer_emergency_contact_number_name = function.prompt_user_for_input \
        (function.number_symbol_restrictor, "Name: ", "Only alphabet in Name\n")



    # Ask New Customer for Relation with the Emergency contact number
    new_customer_emergency_contact_number_relation = function.prompt_user_for_input \
        (function.number_symbol_restrictor, "Relationship to contact: ", "Only alphabet\n")



    # Ask New Customer for Emergency Contact Number
    new_customer_emergency_contact_number = function.prompt_user_for_input\
        (function.phone_num_validation, "Emergency contact Number (Example: 01xxxxxxxxx) :", "Invalid Contact Number\n")


    function.header_topic("Username and Password")



    # Ask New Customer for creating a username
    new_customer_username = function.prompt_user_for_input(function.username_validation,
                                                           "Customer Username:","Username existed").lower()
    
   


    #TODO:: add user name(should be unique)







    # Ask user for password
    while 1:
            new_user_password = function.prompt_user_for_input \
    (function.password_validation,
        "Create a Password with a combination of Upper-Lower Letter, number and symbol. Minimum 8-Character \nCreate a Password:",
        "Password should consist of Upper-Lower Letter, number and symbol\n")

            new_user_re_type_password = input("Retype your password: ")

            if new_user_password == new_user_re_type_password:
                break
            else:
                print("Passwords do not match. Please try again.")
    



    time.sleep(2)
    function.header_topic("Registration success")

    #dictionary
    information = {
            
        'full name': new_customer_Full_name,
        'gender': new_customer_gender,
        'date of birth': new_customer_date_of_birth,
        'email': new_customer_email,
        'contact number': new_customer_contact_number,
        'emergency contact name': new_customer_emergency_contact_number_name,
        'emergency contact relation': new_customer_emergency_contact_number_relation,
        'emergency contact number': new_customer_emergency_contact_number,
        'username': new_customer_username,
        'password': new_user_re_type_password

    }

    #save the data into the text file
    with open('customer_personal_data.txt', 'a') as file:
        json.dump(information, file)
        file.write("\n")





    


    
