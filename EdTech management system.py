
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
class Student(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__courses = []     # Private variable
    def enroll_course(self, course_name):
        self.__courses.append(course_name)
        print(f"{course_name} enrolled successfully!")
    def get_courses(self):
        return self.__courses
    def display_details(self):
        print("\n--- Student Details ---")
        print(f"Student ID: {self.get_user_id()}")
        print(f"Name: {self.get_name()}")
        print("Enrolled Courses:", self.__courses)
class Mentor(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__assigned_students = []
    def assign_student(self, student):
        self.__assigned_students.append(student)
    def display_details(self):
        print("\n--- Mentor Details ---")
        print(f"Mentor ID: {self.get_user_id()}")
        print(f"Name: {self.get_name()}")
        print("Assigned Students:")
        for student in self.__assigned_students:
            print(f"- {student.get_name()}")
class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
    def display_details(self, students, mentors):
        print("\n=== All Students ===")
        for student in students:
            student.display_details()

        print("\n=== All Mentors ===")
        for mentor in mentors:
            mentor.display_details()
students = []
mentors = []
admin = Admin("A1", "System Admin")
while True:
    print("\n===== EdTech Management System =====")
    print("1. Add Student")
    print("2. Add Mentor")
    print("3. Enroll Student in Course")
    print("4. Assign Student to Mentor")
    print("5. Mentor View Assigned Students")
    print("6. Admin View All Details")
    print("7. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        user_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        student = Student(user_id, name)
        students.append(student)
        print("Student added successfully!")
    elif choice == "2":
        user_id = input("Enter Mentor ID: ")
        name = input("Enter Mentor Name: ")
        mentor = Mentor(user_id, name)
        mentors.append(mentor)
        print("Mentor added successfully!")
    elif choice == "3":
        if not students:
            print("No students available!")
            continue
        for i, student in enumerate(students):
            print(i, student.get_name())
        index = int(input("Select student index: "))
        course = input("Enter Course Name: ")
        students[index].enroll_course(course)
    elif choice == "4":
        if not students or not mentors:
            print("Students or Mentors not available!")
            continue
        for i, student in enumerate(students):
            print(i, student.get_name())
        s_index = int(input("Select student index: "))
        for i, mentor in enumerate(mentors):
            print(i, mentor.get_name())
        m_index = int(input("Select mentor index: "))
        mentors[m_index].assign_student(students[s_index])
        print("Student assigned successfully!")
    elif choice == "5":
        if not mentors:
            print("No mentors available!")
            continue
        for i, mentor in enumerate(mentors):
            print(i, mentor.get_name())
        index = int(input("Select mentor index: "))
        mentors[index].display_details()
    elif choice == "6":
        admin.display_details(students, mentors)
    elif choice == "7":
        print("Exiting system...")
        break
    else:
        print("Invalid choice! Please try again.")
