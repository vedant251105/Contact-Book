# contact book 
contact = {}

def add_contact():
    name = input("Enter name: ")
    phone_no = input("Enter phone number: ")
    contact[name] = {'name':name,'Phone':phone_no}
    print(f"\nContact for {name} saved successfully !!")

def view_contact():
    for name,info in contact.items():
        print(f"\nName: {name}")
        print(f"Phone: {info['Phone']}")
    if not contact:
        print("\nNo Contact found.")

def delete_contact():
    view_contact()
    name = input("Enter name to delete :")
    if name in contact:
        contact.pop(name) # or del contact[name] 
        print(f"\nContact {name} deleted.")
    else:
        print(f"\nContact not found for {name}.")

def search_contact():
    name= input("Search here :")
    if name in contact:
        print(f"\nContact found for {name} ")
        print(f"Name: {name}")
        print(f"Phone: {contact[name]['Phone']}")    
    else:
        print(f"\nNot found any contact with {name}")

def main():
    while True:
        print("* * * Contact Menu * * *")
        print("1. Add Contact.")
        print("2. View Contact list.")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice(1-5) :")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contact()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("\nContact Book exited...")
            break
        else:
            print("\nInvalid input.")
main()