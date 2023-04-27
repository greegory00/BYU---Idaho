import math
from datetime import datetime

today = datetime.now()


w = int(input("Enter the width of the tire in mm (ex 205): "))
a = int(input("Enter the aspect ratio of the tire (ex 60): "))
d = int(input("Enter the diameter of the wheel in inches (ex 15): "))

v = math.pi * w**2 * a * (w * a + 2540 * d) / 10000000000

print(f"The approximate volume is {v:.2f} liters")

with open("volumes.txt", "at") as volumes:
    print(f"{today:%Y-%m-%d}", f"{w}, {a}, {d}, {v:.2f}", file=volumes, sep=", ")


purchase = input("Do you want to buy the tires with these dimensions? ")
if purchase == "yes":
    phone_num = int(input("Please type in your phone number: "))
    with open("volumes.txt", "at") as volumes:
        print(f"Phone number: {phone_num}", file=volumes)
        print("Number added satisfactorily.")
else:
    print("Thank you, good bye.")