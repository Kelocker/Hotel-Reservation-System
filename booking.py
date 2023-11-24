import function
import json
import datetime
from datetime import date
from datetime import datetime, timedelta

#############################################################################
#############################################################################
"""
1) View_room
2) Valid_date
3) check_date_validation
4) generate booking id
5) view_specific_available_room
6) booking
7) active booking
8) ongoing room
9) cancel booking
"""


#############################################################################
#############################################################################
#Content

def view_room():
    function.header_topic("View Room")
    with open("room_type.txt", "r") as file:
        data = file.readlines()

    room_data = [json.loads(line) for line in data]

    with open("room_details.txt","r") as room_detail_file:
        datas = room_detail_file.readlines()

    room_datas = [json.loads(room_detail_line) for room_detail_line in datas]

    for idx, (room, rooms) in enumerate(zip(room_data, room_datas), start=1):
        room_type = room["Room type"]
        price = room["price"]
        print(f"{idx}. Room type: {room_type} | Rate: RM{price} per night")



#validate date format
def valid_date(date_str):
    try:
        datetime.strptime(date_str, '%d/%m/%Y')
        return True
    except ValueError:
        return False



#Validate for user input checkin and checkout 
def check_date_validation(checkin_date,checkout_date): 
    
    checkin_datetime = datetime.strptime(checkin_date, "%d/%m/%Y")
    checkout_datetime = datetime.strptime(checkout_date, "%d/%m/%Y")
    today = datetime.now()
    if checkin_datetime >= today and checkout_datetime > today:
        if checkin_datetime < checkout_datetime:
            return True
        print("CheckOUT date should be after CheckIN date")
    print("You are not allow to book past room")
    return False    



#Generating booking ID
def generate_booking_id():
    try:
        with open("log.txt", "r") as file:
            data = file.readlines()
            if data:
                last_entry = json.loads(data[-1])
                last_id = int(last_entry["Booking id"])
                next_id = str(last_id + 1).zfill(5)  # Increment and pad with leading zeros
            else:
                next_id = "00001"
    except FileNotFoundError:
        next_id = "00001"
    return next_id




#View Specific Room
def view_specific_available_room(room_type_input,user_input_room_checkin_date,user_input_room_checkout_date):
     

       

 

    def overlap(list1, list2):

        set1 = set(list1)

        set2 = set(list2)

 

        return len(set1.intersection(set2)) > 0

   

 

 

 
    data = []
    if check_date_validation(user_input_room_checkin_date,user_input_room_checkout_date):  

       

       

        available_rooms =[]

        with open("room_details.txt","r") as room_file:

            data = room_file.readlines()

            room_data = [json.loads(line) for line in data]

            for room in room_data:

                if room["Room type"] == room_type_input and room["Status"] == "True":

                    available_rooms.append(room)

                   

 

           

        with open("log.txt", "r") as file:

            log_check = file.readlines()

            for log in log_check:

                log = json.loads(log)

 

               

                checkin_string = log["Checkin date"]

                checkout_string = log["Checkout date"]  

 

                range1 = function.dates_between(checkin_string, checkout_string)

                range2 = function.dates_between(user_input_room_checkin_date, user_input_room_checkout_date)

 

               

                for room in available_rooms:

                        if (log["Room number"] == room["Room number"]) and overlap(range1, range2):

                            available_rooms.remove(room)                  

               

 
            #data = []

            if available_rooms:

                for room in available_rooms:

                    room_number = room["Room number"]

                    "True" == room["Status"]

                    print(f"Room type: {room['Room type']} || Room number: {room_number}")

                    data.append(room_number)

                return data

            else:

                print(f"Rooms type {room_type_input} are currently unvailable.")

                return data and False

           

    print("Invalid CheckIN or CheckOUT date\n Please Try Again")

    return data and False
        
    


#Customer book room
def booking():
    function.header_topic('Room Booking')
    view_room()
    room_type_data = function.data_return("room_type.txt")
    room_details_data = function.data_return("room_details.txt")
    
    if room_type_data:
        if room_details_data:
            #Ask for room type (including validation)   
            room_type = function.prompt_user_for_input(function.room_type_validation,"Room type:","Invalid Room Type").upper()

            #Checkin and checkout date(including validation)
            #User input checkin date and checkout date
            checkin_date = function.prompt_user_for_input(valid_date,"Check-IN date:","Invalid date/Format")
            checkout_date = function.prompt_user_for_input(valid_date,"Check-OUT date:","Invalid date/Format")

            if check_date_validation(checkin_date,checkout_date):
                room_number_available_list = view_specific_available_room(room_type,checkin_date,checkout_date)
                if room_number_available_list:
                        

                    def check_room_number_available_list(ans):
                            return ans in room_number_available_list and function.only_3(ans)
                        

                    #dump date into booking.txt

                    book=function.prompt_user_for_input(function.check_option('yn'),"Do you want to book a room? [Y/N]:","Please insert correct option.").lower()
                
                
                    if book.lower()=="y":
                        room_number = function.prompt_user_for_input(check_room_number_available_list,"Room number:","Room number not available")
                        
                        
                        booking_date = date.today().strftime('%d/%m/%Y')
                        booking_id = generate_booking_id()
                    
                        
                    
                    
                        name = function.user_name()

                        
                        with open("customer_personal_data.txt","r") as detail_info_file:
                            content = detail_info_file.read().strip()

                        list = [json.loads(data) for data in content.splitlines()]


                        full_name = None
                        contact = None

                        for datas in list:
                            if name.lower() == datas["username"].lower():
                                username = datas["username"]
                                full_name = function.prompt_user_for_input(function.number_symbol_restrictor,"Full name: ","Only Alphabet")
                                contact = function.prompt_user_for_input(function.phone_num_validation,"Contact number: ","Invalid Phone Number")

                                with open('room_type.txt') as room_file:
                                    for l in room_file:
                                        room_data = json.loads(l)
                                        if room_data['Room type'] == room_type:
                                            room_price = float(room_data['price'])

                                total_price = room_price * float(len(function.dates_between(checkin_date, checkout_date)))


                                room_booking_detail = {

                                    
                                'Booking id' : booking_id,
                                'Room type': room_type,
                                'Checkin date': checkin_date,
                                'Checkout date' : checkout_date,
                                'Room number': room_number,
                                'username' : username,
                                'full name': full_name,
                                'contact number': contact,
                                'Booking date' : booking_date,
                                'total price': total_price
                                

                                }    

                                with open("log.txt", "a") as log_file:
                                    json.dump(room_booking_detail, log_file)
                                    log_file.write("\n")
                                    
                                print("Booking successful.")
                                return
                    #if no return
                    else:
                        return
                #if no more room return
                else:
                    return
            else:
                return
        #if room_details.txt empty return
        else:
            print("Contact Admin to add Room Information.")
            return
    #if room_type.txt empty return
    else:
        print("Contact Admin to add Room Type.")
        return




#customer
#Show user active booking
def show_active_booking():
    function.header_topic("Your Active booking")
    name = function.user_name()

    with open("log.txt", "r") as booking_info_file:
        user_data = booking_info_file.readlines()

    active_booking_found = False
    

    for line in user_data:
        room_data = json.loads(line)
        today = datetime.now()
        checkin_string = room_data["Checkin date"]
        date_format = "%d/%m/%Y"
        checkin_datetime = datetime.strptime(checkin_string, date_format)
        

        if name == room_data['username'] and (checkin_datetime > today):
                print(f"Booking ID: {room_data['Booking id']} || Room Type: {room_data['Room type']} || Room number: {room_data['Room number']}  || Check-In date: {room_data['Checkin date']}  ||  Check-OUT date: {room_data['Checkout date']}\n")
                active_booking_found = True


    if not active_booking_found:
        print("You do not have any active booking")
        return
    return





#Show ongoing room
def show_ongoing_room():
    function.header_topic("Ongoing Room")
    name = function.user_name()

    with open("log.txt", "r") as booking_info_file:
        user_data = booking_info_file.readlines()

    ongoing_room_found = False

    for line in user_data:
        room_data = json.loads(line)
        today = datetime.now()
        checkin_string = room_data["Checkin date"]
        checkout_string = room_data["Checkout date"]
        date_format = "%d/%m/%Y"
        checkin_datetime = datetime.strptime(checkin_string, date_format)
        checkout_datetime = datetime.strptime(checkout_string, date_format)
        room_data = json.loads(line)

        if name == room_data['username']:
            if (checkin_datetime <= today):
                if (today < checkout_datetime):
                    print(f"Booking ID: {room_data['Booking id']} || Room Type: {room_data['Room type']} || Room number: {room_data['Room number']} \n")
                    ongoing_room_found = True
                    

            

    if not ongoing_room_found:
        print("You do not have any active room")
        return False



def cancel_booking():
    show_active_booking()
    name = function.user_name()

    function.header_topic("Booking cancellation")
    booking_data = function.data_return("log.txt")
    
    if booking_data:

        with open("log.txt", "r") as booking_info_file:
            user_data = booking_info_file.readlines()

        ongoing_room_found = False

        for line in user_data:
            room_data = json.loads(line)
            today = datetime.now()
            checkin_string = room_data["Checkin date"]
            date_format = "%d/%m/%Y"
            checkin_datetime = datetime.strptime(checkin_string, date_format)
            
           

        if name == room_data['username']:
            if (checkin_datetime > today):
                ongoing_room_found = True
        else:
            ongoing_room_found = False
    

        if ongoing_room_found:
            booking_id = function.prompt_user_for_input(function.only_5,"Booking ID:","Invalid Booking ID")

                
            
                
            booking_check = False
            
            
                
            with open("log.txt","r") as booking_info_file:
                
                data = booking_info_file.readlines()
                today = datetime.now()

                user_booking_list = []

            for line in data:
                    room_data = json.loads(line)
                    today = datetime.now()
                    checkin_string = room_data["Checkin date"]
                    date_format = "%d/%m/%Y"
                    checkin_datetime = datetime.strptime(checkin_string, date_format)
                    
                    

                    if room_data['username'] == name and room_data["Booking id"] == booking_id and (checkin_datetime > today):
                        booking_check = True
                            
                    else:
                        user_booking_list.append(line)
                        
                    
                    
                                
            if booking_check:
                with open("log.txt", "w") as booking_info_file:
                    for room_data in user_booking_list:
                        booking_info_file.write(room_data)
                
                print(f"Booking for {booking_id} have been successfully Cancelled")
                return
            else:
                print("Invalid Booking")
                return
    else:
        print("No booking record found")
        return

                  


           






def customer_room_interface():
    function.header_topic("Room")
    print("View upcoming Booking    Type [U]")
    print("View On-Going Room       Type [A]")
    print("Room Booking             Type [B]")
    print("Cancel Booking           Type [C]")
    print("Exit                     Type [E]")
    ans = function.prompt_user_for_input(function.check_option('uabce'), "Please insert: ", "Invalid option").lower()
       
    if ans == "u":
        show_active_booking()
    
    elif ans == "a":
        show_ongoing_room()

    elif ans == "b":
        booking()
    
    elif ans == "c":
        cancel_booking()
    else:
        return


