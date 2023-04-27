from datetime import datetime

today = datetime.now()
day_of_week = today.weekday()


subtotal = float(input("Please enter the subtotal: "))

if subtotal >= 50 and day_of_week == 1 or day_of_week == 2:
        discount = 10 * subtotal / 100
        print(f"Discount amount: {discount:.2f}")

        total_discount = subtotal - discount

        tax = 6 * total_discount / 100
        total = subtotal - discount + tax
        print(f"Sales tax amount: {tax:.2f}")
        print(f"Total: {total:.2f}")

else:
    sales_tax = 6 * subtotal / 100
    add = subtotal + sales_tax
    print(f"Sales tax amount: {sales_tax:.2f}")
    print(f"Total: {add:.2f}")