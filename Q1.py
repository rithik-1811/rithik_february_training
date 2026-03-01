student_name = input("Enter student name: ")
age = int(input("Enter age: "))
percentage = float(input("Enter percentage: "))
family_income = float(input("Enter family income: "))
is_rural = input("Is the student from a rural area? (True/False):")

is_rural = True if is_rural == "True" else False

eligible = (percentage > 90) or (percentage > 85 and family_income < 300000)

print("\n--- Student Details ---")
print(f"Name: {student_name}")
print(f"Age: {age}")
print(f"Percentage: {percentage}")
print(f"Family Income: {family_income}")
print(f"Rural Area: {is_rural}")

if (eligible):
    print("\nEligible for scholarship")
else:
    print("\nNot eligible")
