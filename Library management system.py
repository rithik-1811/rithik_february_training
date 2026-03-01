class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def display_details(self):
        print(f"User ID: {self.__user_id}")
        print(f"Name: {self.__name}")


class Member(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__borrowed_books = []

    def borrow_book(self, book_name):
        self.__borrowed_books.append(book_name)
        print(f"{book_name} borrowed successfully!")

    def return_book(self, book_name):
        if book_name in self.__borrowed_books:
            self.__borrowed_books.remove(book_name)
            print(f"{book_name} returned successfully!")
        else:
            print("Book not found in borrowed list!")

    def get_books(self):
        return self.__borrowed_books

    def display_details(self):
        print("\n--- Member Details ---")
        print(f"Member ID: {self.get_user_id()}")
        print(f"Name: {self.get_name()}")
        print("Borrowed Books:", self.__borrowed_books)


class Librarian(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__managed_members = []

    def add_member(self, member):
        self.__managed_members.append(member)

    def display_details(self):
        print("\n--- Librarian Details ---")
        print(f"Librarian ID: {self.get_user_id()}")
        print(f"Name: {self.get_name()}")
        print("Managed Members:")
        for member in self.__managed_members:
            print(f"- {member.get_name()}")


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)

    def display_details(self, members, librarians):
        print("\n=== All Members ===")
        for member in members:
            member.display_details()

        print("\n=== All Librarians ===")
        for librarian in librarians:
            librarian.display_details()


# ---------------- MAIN PROGRAM ----------------

members = []
librarians = []
admin = Admin("A1", "Library Admin")

while True:
    print("\n===== Library Management System =====")
    print("1. Add Member")
    print("2. Add Librarian")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Assign Member to Librarian")
    print("6. Librarian View Managed Members")
    print("7. Admin View All Details")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        user_id = input("Enter Member ID: ")
        name = input("Enter Member Name: ")
        member = Member(user_id, name)
        members.append(member)
        print("Member added successfully!")

    elif choice == "2":
        user_id = input("Enter Librarian ID: ")
        name = input("Enter Librarian Name: ")
        librarian = Librarian(user_id, name)
        librarians.append(librarian)
        print("Librarian added successfully!")

    elif choice == "3":
        if not members:
            print("No members available!")
            continue
        for i, member in enumerate(members):
            print(i, member.get_name())
        index = int(input("Select member index: "))
        book = input("Enter Book Name: ")
        members[index].borrow_book(book)

    elif choice == "4":
        if not members:
            print("No members available!")
            continue
        for i, member in enumerate(members):
            print(i, member.get_name())
        index = int(input("Select member index: "))
        book = input("Enter Book Name to Return: ")
        members[index].return_book(book)

    elif choice == "5":
        if not members or not librarians:
            print("Members or Librarians not available!")
            continue
        for i, member in enumerate(members):
            print(i, member.get_name())
        m_index = int(input("Select member index: "))

        for i, librarian in enumerate(librarians):
            print(i, librarian.get_name())
        l_index = int(input("Select librarian index: "))

        librarians[l_index].add_member(members[m_index])
        print("Member assigned to librarian successfully!")

    elif choice == "6":
        if not librarians:
            print("No librarians available!")
            continue
        for i, librarian in enumerate(librarians):
            print(i, librarian.get_name())
        index = int(input("Select librarian index: "))
        librarians[index].display_details()

    elif choice == "7":
        admin.display_details(members, librarians)

    elif choice == "8":
        print("Exiting system...")
        break

    else:
        print("Invalid choice! Please try again.")
