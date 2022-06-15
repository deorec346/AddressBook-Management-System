class Contact:
    def __init__(self, first_name, last_name, address, city, state, zip, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone = phone
        self.email = email

    def __str__(self):
        return f" First Name = {self.first_name}, Last Name = {self.last_name}, Address = {self.address}, City = {self.city}, State = {self.state}, Zip = {self.zip}, Phone Number = {self.phone}, Email = {self.email}"


class AddressBook:

    def __init__(self, address_book_name):
        self.contact_dict = {}
        self.address_book_name = address_book_name

    def display(self):
        print(self.contact_dict)

    def add_contact(self, contact_obj):
        self.contact_dict.update({contact_obj.first_name: contact_obj})

    def get_contact(self, first_name):
        return self.contact_dict.get(first_name)

    def display_data_string(self):
        print("---------------------------------------------------------------------------------------")
        print("First\tLast\tPhone\taddress\tCity \tState\tzip code")
        print("---------------------------------------------------------------------------------------")
        for v in self.contact_dict.items():
            print(f"{v.first_name}\t{v.last_name}\t{v.phone}\t{v.address} \t{v.city}\t{v.state}\t{v.zip}")


def add_addressbook_name():
    """
    Checking the book present or not and adding the addressbook.
    """
    try:
        address_book_name = input("Enter the name of addressbook : ")
        book_obj = addressbook_dict.get(address_book_name)
        # if book_obj is not None:
        if book_obj:
            print("Book already exist")
            return
        address_book = AddressBook(address_book_name)
        addressbook_dict.update({address_book_name: address_book})
        print("-----------------Your AddressBook added successfully ---------------------------\n")
    except Exception as e:
        print("Please enter valid book name", e)


def display_address_book():
    """
    Method to Displaying the Addressbook
    :return:
    """
    print("===============================Address Book Name==================================")
    for k, v in addressbook_dict.items():
        print(k, v)


def add_contact():
    """
    Before adding contact to Addressbook, checking contact is present or not, if contact i not present then add contact.
    """
    # print(addressbook_dict)
    try:
        address_book_name = input("Enter the name book name to add contact : ")
        book_obj = addressbook_dict.get(address_book_name)
        # print(addressbook_dict)
        if not book_obj:
            book_obj = AddressBook(address_book_name)
            addressbook_dict.update({address_book_name: book_obj})
        # print(addressbook_dict)

        first_name = input("Enter first name \n")
        last_name = input("Enter last name \n")
        address = input("Enter address \n")
        city = input("Enter city \n")
        state = input("Enter state \n")
        zip = input("Enter zip code \n")
        phone = input("Enter phone number \n")
        email = input("Enter email address \n")

        contact = Contact(first_name, last_name, address, city, state, zip, phone, email)
        book_obj.add_contact(contact)
        print("Your Address Book Successfully added")
    except Exception as e:
        print("Please enter correct Address book name", e)


if __name__ == '__main__':
    print("Welcome to Address Book Management System")
    address_book = AddressBook("Address_book_name")
    addressbook_dict = {}
    more_choice = True
    while more_choice:
        print("1. Add an address book\n" "2. Display address book\n"
              "3. Add contact\n" 
              "0. Exit address book...")
        choice = {1: add_addressbook_name, 2: display_address_book,
                  3: add_contact,
                  4: display_contact}
        try:
            user_input = int(input("Enter choice: "))
            if user_input != 0:
                choice.get(user_input)()
            elif user_input == 0:
                more_choice = False
                print("Existing from Addressbook")
                print()
        except Exception as e:
            print("Its a invalid input ", e)
            print()
