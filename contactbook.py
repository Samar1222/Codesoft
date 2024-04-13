class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number):
        self.contacts[name] = {'Phone': phone_number}
        print(f"Contact {name} added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("Contact book is empty.")
        else:
            print("Contacts:")
            for name, info in self.contacts.items():
                print(f"Name: {name}, Phone: {info['Phone']}")
            print()

    def search_contact(self, name):
        if name in self.contacts:
            info = self.contacts[name]
            print(f"Name: {name}, Phone: {info['Phone']}")
        else:
            print(f"Contact {name} not found.")

    def remove_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} removed successfully!")
        else:
            print(f"Contact {name} not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("_______________________")
        print("")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Remove Contact")
        print("5. Exit")
        print("_______________________")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            contact_book.add_contact(name, phone_number)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            name = input("Enter name to search: ")
            contact_book.search_contact(name)
        elif choice == '4':
            name = input("Enter name to remove: ")
            contact_book.remove_contact(name)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()