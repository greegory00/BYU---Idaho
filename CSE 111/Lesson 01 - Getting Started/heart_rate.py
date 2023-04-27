"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

age = int(input("Please enter your age: "))

heart_rate = 220 - age

minimum = 65 * heart_rate / 100

maximum = 85 * heart_rate / 100

print(f"When you exercise to strenhthen your heart, you should\nkeep your heart rate between {int(minimum)} and {int(maximum)} beats per minute.")