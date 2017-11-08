year = 2017
birthYear = 1988

age = year - birthYear

print("you are either", age-1, "or", age, "years old.")


radius = 4
print("the radius is", radius)

circumference = (2 * radius * 3.14)
print("the circumference is", circumference)

area = 3.14 * (radius**2)
print("the area is", area)

area = 3.14 * radius * radius
print("the area is", area)


bill = 12.95
tax = 0.08
tip = 0.20

afterTip = bill * (tip + 1)

total = afterTip + (bill * tax)

print(total)
print("for a bill total of", bill, "and a", (tip * 100), "percent tip, with a tax percentage of", (tax * 100), "your total will be", total)
