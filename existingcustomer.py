import json
import function
import booking
import food
import newcus


#Can view, update, and delete personal information.
#personal information

#view personal information
# Define the file path
def view_personal_details():
    with open('customer_personal_data.txt') as f:
        data_list = f.readlines()
        with open('tempfile.txt') as file:
            username = file.read()
        for data in data_list:
            customer = json.loads(data)
            if customer['username'] == username:
                function.header_topic("Customer Details")
                print("Full Name:", customer['full name'])
                print("Gender:", customer['gender'])
                print("Date of Birth:", customer['date of birth'])
                print("Email:", customer['email'])
                print("Contact Number:", customer['contact number'])
                print("Emergency Contact Name:", customer['emergency contact name'])
                print("Emergency Contact Relation:", customer['emergency contact relation'])
                print("Emergency Contact Number:", customer['emergency contact number'])
                break# Exit the function after finding the customer
        return


#update personal information
#update personal information
def update_personal_details():
     #validation for new data
    function_lists = [function.number_symbol_restrictor, newcus.gender_validation, newcus.validate_date, newcus.email_format, function.phone_num_validation, function.number_symbol_restrictor, function.number_symbol_restrictor, function.phone_num_validation]
    with open('customer_personal_data.txt') as f:
        data_list = f.readlines()
        with open('tempfile.txt') as file:
            username = file.read().strip()
    for index, data in enumerate(data_list, start=1):
        customer = json.loads(data)
        if customer['username'] == username:
            function.header_topic("Update Personal Details")
            for i, (key) in enumerate(customer, start=1):
                if key not in ['username', 'password']:
                    print(f"{i}. {key}")
            while True:
                selected_option=function.prompt_user_for_input(function.number,"Please select the option that needs to be edited: ","Only numbers are acceptable!")
                selected_option=int(selected_option) #str are not acceptable with arithmetic option so change to int
                if 1 <= selected_option <= len(customer):
                    selected_key = list(customer.keys())[selected_option - 1]

                    if 1 <= selected_option <= len(function_lists):

                        validation = function_lists[selected_option - 1]

                        new_value = function.prompt_user_for_input(validation, f"Enter the new value for {selected_key}: ", 'Invalid format')

                        customer[selected_key] = new_value
                        # Assuming you want to update the customer_personal_data.txt file with the new data
                        with open('customer_personal_data.txt', 'w') as f:
                            for data_line in data_list:
                                if json.loads(data_line)['username'] == username:
                                    f.write(json.dumps(customer) + '\n')
                                else:
                                    f.write(data_line)
                        print("Personal information updated successfully!")
                        return
                    else:
                        print("Invalid option.Please select a valid option between 1 and 8.")
                else:
                    print("Invalid option.")
                    update_personal_details()


#delete
def delete_personal_details():
    with open('customer_personal_data.txt') as f:
        data_list = f.readlines()
        with open('tempfile.txt') as file:
            username = file.read().strip()

    for index, data in enumerate(data_list, start=1):
        customer = json.loads(data)
        if customer['username'] == username:
            function.header_topic("Delete Personal Information")
            for i, (key, value) in enumerate(customer.items(), start=1):
                if key not in ['username', 'password']:
                    print(f"{i}. {key}")
            while True:
                selected_option = function.prompt_user_for_input(function.number, "Please select the option that needs to be deleted or press '0' to cancel:", "Only numbers are acceptable!")
                selected_option = int(selected_option)

                if selected_option == 0:
                    print("Deletion canceled.")
                    modify_personal_details()
                    break
                elif 1 <= selected_option <= len(customer) - 2:  # Exclude 'username' and 'password' keys
                    selected_key = list(customer.keys())[selected_option - 1]
                    if selected_key not in ['username', 'password']:
                        confirm_delete = input(f"Are you sure you want to delete {selected_key}? (yes/no): ").lower()
                        if confirm_delete == "yes":
                            # Remove the selected key from the customer dictionary
                            customer[selected_key] = 'Deleted'
                            # Assuming you want to update the customer_personal_data.txt file with the new data
                            with open('customer_personal_data.txt', 'w') as f:
                                for data_line in data_list:
                                    if json.loads(data_line)['username'] == username:
                                        f.write(json.dumps(customer) + '\n')
                                    else:
                                        f.write(data_line)
                            print(f"{selected_key} deleted successfully!")
                            return
                        else:
                            print(f"Deletion of {selected_key} canceled.")
                            return
                    else:
                        print("Cannot delete 'username' or 'password'. Please select a valid option.")

                else:
                    print("Invalid input. Please select a valid option.")





def modify_personal_details():
    while True:
        function.header_topic("Modify Personal Details")
        print("View Personal Details      [V]")
        print("Update Personal Information[U]")
        print("Delete Personal Information[D]")
        print("Exit                       [E]")
        modify_opt=function.prompt_user_for_input(function.check_option("vude"),"Insert an option:","[V] for view customer,[U] for update personal information,[D] for delete personal information").lower()

        if modify_opt.lower()=="v":
            view_personal_details()
        elif modify_opt.lower()=="u":
            update_personal_details()
        elif modify_opt.lower()=="d":
            delete_personal_details()
        else:
            return







def homepage():

    interface = '\nModify Personal Details   Type[M]\nRoom                      Type[R]\nFood Menu                 Type[O]\nLogout                    Type[L]\nPlease insert an option:'


    while True:
        function.header_topic('Homepage')
        function.welcome_user()
        opt = function.prompt_user_for_input(function.check_option("mrol"), interface,
                                             "Invalid option").lower()
        if opt.lower() == "m":
            modify_personal_details()
        elif opt.lower()=="r":
            booking.customer_room_interface()
        elif opt.lower()=="o":
            food.order_food()
        else:
            print("Exiting the customer page...")
            return

















