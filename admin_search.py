import function
import json
import datetime

#function to check if the customer exist
def check_exist(ans):
    return not function.username_validation(ans)


def search_customer_booking():
    while True:
        #ask for the username of the customer
        cus_name = function.prompt_user_for_input(check_exist, 'Username of customer: ', 'This user does not exist')

        #read the file
        with open('log.txt', 'r') as file:
            lists = []
            for line in file:

                record = json.loads(line)
                #check line by line to find the customer
                if record['username'] == cus_name:
                    lists.append(record)
            if lists:
                print('\n')
                print(f'{"ID":7} {"Room type":20} {"Room number":15} Checkin date   Checkout date ')
                print('-'*75)

                for data in lists:
                    print(f'{data["Booking id"]:7} {data["Room type"]:20} {data["Room number"]:15} {data["Checkin date"]:14} {data["Checkout date"]} ')
            else:
                print("This user has no record of booking\n")

            answer = function.prompt_user_for_input(function.check_option('sb'), f'{"Search new customer": <20}[s]\n{"Back": <20}[B]\n{"Please insert:":<20}', 'Invalid option\n')

            if answer.lower() == 'b':
                break
    return 'b'




def view_all_booking():
    current_time = datetime.date.today()

    with open('log.txt', 'r') as file:
        print(f'{"ID":7} {"Name":20} {"Room type":20} {"Room number":15} Checkin date   Checkout date ')
        print('-'*95)
        lists = []
        for line in file:
            data = json.loads(line)

            #change the date in file to datetime.date
            date_string = data["Checkin date"]
            date_format = "%d/%m/%Y"
            date_object = datetime.datetime.strptime(date_string, date_format).date()

            #Check if the date is equal or greater than current time
            if date_object >= current_time:
                data['datetime.checkin'] = date_object
                lists.append(data)

        #Sort the booking in ascending order based on checkin date
        def get_date(ans):
            return ans['datetime.checkin']

        sorted_lists = sorted(lists, key=get_date)

        #print the bookings
        for data in sorted_lists:
            print(f'{data["Booking id"]:7} {data["full name"]:20} {data["Room type"]:20} {data["Room number"]:15} {data["Checkin date"]:14} {data["Checkout date"]} ')
            return

def admin_booking():
    while True:
        function.header_topic('Customer booking page')
        print("View All Booking:        [V]")
        print("Search Customer Booking: [S]")
        print("Back                     [B]")
        ans = function.prompt_user_for_input(function.check_option('vsb'),"Insert option:","Invalid option.").lower()
        if ans =="v":
            view_all_booking()
        elif ans == "s":
            search_customer_booking()
        else:
            break









