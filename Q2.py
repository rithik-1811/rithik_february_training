customer_name = input("Enter customer name: ")
price = float(input("Enter product price: "))
is_premium = input("Is the customer a premium member? (True/False): ")
coupon_code = input("Enter coupon code: ")

is_premium = True if is_premium == "True" else False

discount = 0

if price > 5000 and is_premium:
    discount = 0.20
elif is_premium or coupon_code == "SAVE10":
    discount = 0.10

discount_amount = price * discount
final_price = price - discount_amount

print("\n--- Bill Details ---")
print(f"Customer Name: {customer_name}")
print(f"Original Price: {price}")
print(f"Discount Applied: {discount_amount}")
print(f"Final Price: {final_price}")

if is_premium:
    print("Premium benefits applied")
