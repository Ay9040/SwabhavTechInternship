from services import DatabaseService
db = DatabaseService()

def add_contact():
    name = input("Enter Name: ")
    mobile_no = input("Enter Mobile No.: ")
    if db.add_contact(name,mobile_no) == -1:
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
        print("Invalid input")

def show_contacts():
    contacts = db.get_all_contacts()
    for i,contact in enumerate(contacts):
        print("Contact", i+1)
        print("\tName:", contact[1])
        print("\tMobile No.:", contact[2])

def contact_app():
    while(True):
        print("1. Add Contact\n2. Modify Contact\n3. Remove Contact\n4. Show Contacts\n5. Exit\n:", end="")
        c = int(input())
        if c == 1:
            add_contact()
        elif c == 2:
            modify_contact()
        elif c == 3:
            remove_contact()
        elif c == 4:
            show_contacts()
        else:
            break

if __name__ == "__main__":
    contact_app()