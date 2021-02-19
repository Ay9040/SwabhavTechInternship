from services import DatabaseService
db = DatabaseService()

def add_contact():
    name = input("Enter Name: ")
    mobile_no = input("Enter Mobile No.: ")
    if db.add_contact(name,mobile_no) == -1:
        print("Invalid Input")

def add_address():
    name = input("Enter stored contact name: ")
    city = input("Enter city: ")
    pin = input("Enter pincode: ")
    if db.add_address(name, city, pin):
        print("Invalid Input")

def modify_contact():
    current_name = input("Enter stored contact name: ") 
    name = input("Enter new name(- to keep same): ")
    mobile_no = input("Enter new mobile no.(- to keep same): ")
    data = {}
    if name != '-':
        data['CNAME'] = name
    if mobile_no != '-':
        data['MOBILE_NO'] = mobile_no
    if db.modify_contact(current_name, data):
        print("Invalid Input")

def remove_contact():
    name = input("Enter stored contact name:")
    if db.remove_contact(name):
        print("Invalid Input")

def show_contacts():
    contacts = db.get_all_contacts()
    count = 0
    name = None
    for i, contact in enumerate(contacts):
        if(contact[0] != name):
            count += 1
            name = contact[0]
            print("Contact", count)
            print("\tName:", contact[0])
            print("\tMobile No.:", contact[1])
        if contact[2] != None:
            print("\tAddress:\n\tCity: ", contact[2], "\tPincode: ", contact[3])

def contact_app():
    while(True):
        print("1. Add Contact\n2. Modify Contact\n3. Remove Contact\n4. Show Contacts\n5. Add Address\n6. Exit\n:", end="")
        c = int(input())
        if c == 1:
            add_contact()
        elif c == 2:
            modify_contact()
        elif c == 3:
            remove_contact()
        elif c == 4:
            show_contacts()
        elif c == 5:
            add_address()
        else:
            break

if __name__ == "__main__":
    contact_app()