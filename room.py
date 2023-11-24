import function
import json
import food

##############################################################################
##############################################################################
#Content start Here

#View room type
#This function did not use to return data because this function only called out to display
#Function used after return validation in other function
#view purposes
def view_room_type():
    data = function.data_return("room_type.txt")
    if data:
        with open("room_type.txt","r") as file:
            data = file.readlines()

        room_data = [json.loads(line) for line in data]

        for idx, (room) in enumerate(room_data, start=1):
            room_type = room["Room type"]
            print(f"{idx}. {room_type}")
            
    else:
        print("Contact admin to add room data")
        


def view_all_room_types_with_price_display():
    data = function.data_return("room_type.txt")

    if data:

        with open("room_type.txt", "r") as file:

            data = file.readlines()

        room_data = [json.loads(line) for line in data]

        for idx, (room) in enumerate(room_data, start=1):
            room_type = room["Room type"]

            room_price = room["price"]

            print(f"{idx}. Room type: {room_type} Price: {room_price} ")
            

    else:

        print("No room data. Contact admin to add room data")
        return



def view_all_room_details():
    data = function.data_return("room_details.txt")

    if data:

        with open("room_details.txt", "r") as file:

            data = file.readlines()

        room_data = [json.loads(line) for line in data]

        for idx, (room) in enumerate(room_data, start=1):
            room_type = room["Room type"]

            room_number = room["Room number"]

            print(f"{idx}. Room type: {room_type} Room number: {room_number} ")
            

    else:

        print("No room data. Add room type to display")
        return
    


#View room information
def view_room_information_for_customer():
    function.header_topic("Room Information")
    room_type_data = function.data_return("room_type.txt")
    if room_type_data:


            for idx, (room) in enumerate(room_type_data, start=1):
                room_type = room["Room type"]
                room_price = room["price"]
                print(f"{idx}. Room Type:{room_type}  Rate: RM{room_price} per night")
                return
    else:
        print("Contact Admin. Add Room Information")
        return



#Add Room Type
def add_room_type():
    function.header_topic("Room Type Existed")
    view_all_room_types_with_price_display()

    # add room type
    room_type = function.prompt_user_for_input(function.number_symbol_restrictor, "Please add room type:",
                                               "Only alphabets are allowed.")
    room_type = room_type.upper()  # to convert to upper case
    room_price = function.prompt_user_for_input(function.number, "Please add price for room:",
                                                "Only numbers are allowed")

    # To check validation

    

    # Open and read file to validate if the number exist or not

    with open("room_type.txt", "r") as file:
        room_type_data = file.readlines()
        for datas in room_type_data:
            room_datas = json.loads(datas)
            if room_type == room_datas["Room type"]:

                print(f"Room type: {room_type} already exist")
                return

            
        new_room_type = {

            'Room type': room_type,
            'price': room_price

        }

        with open('room_type.txt', 'a') as file:
            json.dump(new_room_type, file)
            file.write("\n")

        print(f"Room type {room_type} have successfully added.")
        return



#Edit Room Type information
#### edit_room_type_information only edit information in room type
def edit_room_type_information():
    
    room_type_data = function.data_return("room_type.txt")
    if room_type_data:
        #show user room type
        view_all_room_types_with_price_display()

        #room type user wish to edit
        room_type = function.prompt_user_for_input(function.room_type_validation,'Room type: ', 'Invalid room type').upper()

        

        price = input("Price:")

        found = False
        rooms_list = []

        with open("room_type.txt", "r") as file:
            rooms = [json.loads(line) for line in file]
        
        for room in rooms:
            #The room type which user input will not be append into the file
            if room['Room type'] != room_type:
                rooms_list.append(room)
            else:
                found = True


        
        
        if found:
            with open("room_type.txt", "w") as file:
                        for room in rooms_list:
                            file.write(json.dumps(room) + '\n')

                
            room_update = {
                    
                    'Room type': room_type,
                    'price': price
                    

                    }
            with open('room_type.txt','a') as file:
                json.dump(room_update, file)
                file.write("\n")

            print(f"Room type {room_type} have successfully updated.")
            return
        else:
            print("Room Type not found")
            return
    else:
        print("There are no room type. Please add room type")
        return

    

#Add Room number
def add_room_number():
    function.header_topic("Add Room")
    data = function.data_return("room_type.txt")
    if data:
        #Allow user to see which room type are available
        print("Room Type")
        view_all_room_details()

    
        #User input room number to be added into which room type
        room_type = function.prompt_user_for_input(function.room_type_validation,'Room type: ', 'Invalid room type').upper()
    

        room_number = function.prompt_user_for_input(function.only_3,"Room Number:","Only 3 Character")

        
        
        #To check validation
        room_number_existed_val = False

        #Open and read file to validate if the number exist or not
        with open("room_details.txt","r") as file:

            data = file.readlines()

            for number_list in data:

                number = json.loads(number_list)

    

                if number["Room number"] == room_number:

                    room_number_existed_val = True

    
        

    
            #If true means validation fail and will print a message
            if room_number_existed_val:
                
                print(f"Room number {room_number} exist in another room")

            #If False means data will be save
            else:
                new_room_number = {
                    
                    'Room type': room_type,
                    'Room number': room_number,
                    'Status': "True"
                    

                    }
                        
                with open('room_details.txt','a') as file:
                    json.dump(new_room_number, file)
                    file.write("\n")
                print(f"Room number {room_number} have successfully added.")
                return
    else:
        print("No room type available Please add room type first!")
        return



#Delete Room Type
def delete_room_type():
    function.header_topic("Delete Room Type")
    room_type_data = function.data_return("room_type.txt")
    room_details_data = function.data_return("room_details.txt")

    if room_type_data:
        
            view_room_type()
            #User input which room type to remove
            remove_room_type = function.prompt_user_for_input(function.room_type_validation,"Remove Room Type:","Invalid room type").upper()
            found = False
            updated_rooms = []
            room_detail = []



            for room in room_type_data:
                #The room type which user input will not be append into the file
                if room['Room type'] != remove_room_type:
                    updated_rooms.append(room)
                else:
                    found = True

            #To check if room details.txt are not empty
            if room_details_data:
                

                    for room in room_details_data:
                        #The room details which share the same room type will also be deleted
                        #Meaning all information related to "Room type" user input will be deleted
                        #This is to ensure data conflict does not happened
                        if room['Room type'] != remove_room_type:
                            room_detail.append(room)
                        else:
                            found = True

                    if found:
                            #Warning message will appear
                            print(f"Warning! All details about {remove_room_type} will be delete")
                    
                            #A comfirmation message will also appear
                            ans = function.prompt_user_for_input(function.check_option("yn"),"Do you wish to continue? (y/n):","Invalid Option")
                            if ans == "y":
                                with open("room_type.txt", "w") as file:
                                    for room in updated_rooms:
                                        file.write(json.dumps(room) + '\n')

                                with open("room_details.txt", "w") as file:
                                    for room in room_detail:
                                        file.write(json.dumps(room) + '\n')

                                
                                print(f"Success! {remove_room_type} have been removed.")
                                return

                            else:
                                print("Deletion process Cancelled")
                                return

                    else:
                        print("Room data not match or not found.")
                        return

            #If room details are empty. Room Type will be delete            
            else:
                if found:
                    #Warning message will appear
                    print(f"Warning! All details about {remove_room_type} will be delete.")
            
                    #A comfirmation message will also appear
                    ans = function.prompt_user_for_input(function.check_option("yn"),"Do you wish to continue? (y/n):","Invalid Option")
                    if ans == "y":
                        with open("room_type.txt", "w") as file:
                            for room in updated_rooms:
                                file.write(json.dumps(room) + '\n')

                        
                        print(f"Success! {remove_room_type} have been removed.")
                        return

                    else:
                        print("Deletion process Cancelled")
                        return

    else:
        print("No room type. Please add room type first")
        return



#view all status room room
def view_all_room_status():
    room_type_data = function.data_return("room_type.txt")
    room_details_data = function.data_return("room_details.txt")
    
    if room_type_data:
        if room_details_data:

            for idx, (room) in enumerate(room_details_data, start=1):
                room_type = room["Room type"]
                room_number = room["Room number"]
                room_status = room["Status"]
                if room["Status"] == "True":
                    room_status = "Available"
                else:
                    room_status ="Unvailable"
                print(f"{idx}. Room Type: {room_type} Room Number: {room_number} Room Status: {room_status}")
                
        else:
            print("No room to display. Please add room!")
            
    else:
        print("Please add room type first!")
        



#Delete Room number
def delete_room_number():
    function.header_topic("Delete Room Number")
    room_type_data = function.data_return("room_type.txt")
    room_details_data = function.data_return("room_details.txt")

    if room_type_data:
        if room_details_data:

        #Room number user wish to delete
            view_all_room_details()
            room_number_to_delete = function.prompt_user_for_input(function.only_3,"Room Number to delete: ","3 Character Only")

            with open("room_details.txt", "r") as booking_info_file:
                data = booking_info_file.readlines()
                updated_data = []
                update_file = False
                
            
                for line in data:
                    room_data = json.loads(line)
                    if room_data["Room number"] != room_number_to_delete:  # Check the correct key for room type
                        updated_data.append(line)
                    else:
                        update_file = True
            
            if update_file:
                        
                ans = function.prompt_user_for_input(function.check_option('yn'),"Do you want to continue? (y/n):","Invalid Option").lower()
                if ans == 'y':
                    
                    with open("room_details.txt", "w") as booking_info_file:
                        for room_data in updated_data:
                            booking_info_file.write(room_data)
                
                
                    print(f"Room {room_number_to_delete} have been succesfully deleted.")
                    return
                
                else:
                    print("Room number deletion Cancelled")
                    return
            else:
                print(f"Room {room_number_to_delete} not Found. Please Try Again")
                return
            
        else:
            print("No room data found. Please add room first!")
            return

    else:
        print("No room type. Please add Room Type first!")
        return



#Edit Room infomation
def edit_room_status():
    function.header_topic("Edit Room Information")
    room_type_data = function.data_return("room_type.txt")
    room_details_data = function.data_return("room_details.txt")
    if room_type_data:
        if room_details_data:
            view_all_room_status()

            

            #User input room type to be edit
            room_type = function.prompt_user_for_input(function.room_type_validation,'Room type: ', 'Invalid room type').upper()
            room_number = function.prompt_user_for_input(function.only_3,"Room number:","Invalid Room number")
            
            update = False
            change_to_unvailable = False
            change_to_available = False
            rooms_list = []

            
            
            for room in room_details_data:
                if room['Room type'] == room_type and room['Room number'] == room_number and room['Status'] == "True":
                    change_to_unvailable =True
                    

            for room in room_details_data:
                if room['Room type'] == room_type and room['Room number'] == room_number and room['Status'] == "False":
                    change_to_available = True
                    
            
            for room_checked in room_details_data:
                #The room type which user input will not be append into the file
                if room_checked['Room number'] != room_number and room_checked['Room type'] != room_type:
                    rooms_list.append(room_checked) 
                else:
                    update = True
                    
                    
            

            if update:
                if change_to_unvailable:
                    with open("room_details.txt", "w") as file:
                        for room in rooms_list:
                            file.write(json.dumps(room) + '\n')
                    
                
                
                    
                    room_update = {
                            
                            'Room type': room_type,
                            'Room number': room_number,
                            'Status': "False"
                            

                            }
                    
                    with open('room_details.txt','a') as file:
                        json.dump(room_update, file)
                        file.write("\n")

                    print(f"Room type {room_type} {room_number} Status change to unvailable..")
                    return
                elif change_to_available:
                    with open("room_details.txt", "w") as file:
                        for room in rooms_list:
                            file.write(json.dumps(room) + '\n')
                    
                    room_update = {
                            
                            'Room type': room_type,
                            'Room number': room_number,
                            'Status': "True"
                            

                            }
                    
                    with open('room_details.txt','a') as file:
                        json.dump(room_update, file)
                        file.write("\n")

                    print(f"Room type: {room_type}'s {room_number} Status change to available.")
                    return
                else:
                    print(f"Room for {room_number} not found")
                    return

            else:
                print(f"{room_type} has no room added")
                return

        else:
            print("No Room data add room first")
            return
    else:
        print("Add room type first!")
        return






#################################################################
#################################################################
#Interface
def room_add_interface():
    while True:
        function.header_topic("Add Page")
        print("Add Room Type         Insert[T]")
        print("Add Room Number       Insert[N]")
        print("Back                  Insert[B]")
        ans = function.prompt_user_for_input(function.check_option('tnb'), "Please insert: ", "Invalid Option\n").lower()

        if ans == "t":
            add_room_type()

        elif ans == "n":
            add_room_number()

        else:
            return
    


def room_deletion_interface():
    while True:
        function.header_topic("Delete Page")
        print("Delete Room Type         Insert[A]")
        print("Delete Room Number       Insert[N]")
        print("Back                     Insert[B]")
        ans = function.prompt_user_for_input(function.check_option('anb'), "Please insert: ", "Invalid Option\n").lower()

        if ans == "a":
            delete_room_type()

        elif ans == "n":
            delete_room_number()

        else:
            return
        


def upload_room_detail():
    while True:
        function.header_topic("Upload Room Detail")
        print("Edit Room Status            [E]")
        print("Edit Room Type Information  [R]")
        print("Room Service                [S]")
        print("Back                        [B]")
        ans = function.prompt_user_for_input(function.check_option('ersb'), "Please insert: ", "Invalid Option\n").lower()
        if ans == "e":
            edit_room_status()

        elif ans == "r":
            edit_room_type_information()

        elif ans== "s":
            food.modify_food_menu()
        else:
            return



