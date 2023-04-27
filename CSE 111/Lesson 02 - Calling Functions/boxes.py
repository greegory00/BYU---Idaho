import math

items = int(input("Enter the number of items: "))
boxes = int(input("Enter the number of items per box: "))

division = items / boxes

boxes_needed = math.ceil(division)

print()

print(f"For {items} items, packing {boxes} items in each box, you will need {boxes_needed} boxes.")