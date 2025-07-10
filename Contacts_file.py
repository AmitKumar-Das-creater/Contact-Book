CONTACTS_FILE = "contacts.txt"

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    with open(CONTACTS_FILE, "a") as file:
        file.write(f"{name},{phone}\n")
    print("Contact added successfully.\n")

def search_contact():
    search_name = input("Enter name to search: ")
    found = False
    with open(CONTACTS_FILE, "r") as file:
        for line in file:
            name, phone = line.strip().split(",")
            if name.lower() == search_name.lower():
                print(f"Found: {name} - {phone}\n")
                found = True
                break
    if not found:
        print("Contact not found.\n")

def delete_contact():
    delete_name = input("Enter name to delete: ")
    contacts = []
    deleted = False
    with open(CONTACTS_FILE, "r") as file:
        for line in file:
            name, phone = line.strip().split(",")
            if name.lower() != delete_name.lower():
                contacts.append(f"{name},{phone}")
            else:
                deleted = True
    with open(CONTACTS_FILE, "w") as file:
        for contact in contacts:
            file.write(contact + "\n")
    if deleted:
        print("Contact deleted successfully.\n")
    else:
        print("Contact not found.\n")

def view_all_contacts():
    print("\nAll Contacts:")
    try:
        with open(CONTACTS_FILE, "r") as file:
            for line in file:
                name, phone = line.strip().split(",")
                print(f"{name} - {phone}")
        print()
    except FileNotFoundError:
        print("No contacts found.\n")

def menu():
    while True:
        print("----- Contact Book -----")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. View All Contacts")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            view_all_contacts()
        elif choice == "5":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    menu()
