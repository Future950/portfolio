class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def display_contacts(self):
        if self.contacts:
            print("Contacts:")
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}")
        else:
            print("No contacts in the contact book.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            contact = Contact(name, phone_number, email)
            contact_book.add_contact(contact)
            print("Contact added successfully!")
        elif choice == '2':
            contact_book.display_contacts()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
