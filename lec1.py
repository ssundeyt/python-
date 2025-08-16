import os

#--------------------------------------------VARIABLES--------------------------------------------
"""
# String
name = "Mans"

# Int
age = 23

# Float
gpa = 3.95

# Bool
is_student = True

print(f"Hello {name}, you are {age} years old.")

if is_student:
    print(f"Your gpa is {gpa}.")
else:
    print("You are not a student")
"""

#--------------------------------------------Typecasting--------------------------------------------
"""
name = "Mans"
age = 23
gpa = 3.95
is_student = True

print(type(name)) # Print datatype of variable

gpa = int(gpa) # Change datatype
print(type(gpa))
"""

#--------------------------------------------User input--------------------------------------------
"""
name = input("What is your name?: ")
age = int(input("What is your age?: "))

age += 1

print(f"Hello {name}.")
print(f"You are {age} years old.")
"""
# EXERCISE 1, Calculate area of rectangle
"""
length = float(input("Enter length: "))
height = float(input("Enter height: "))

area = length * height

print(f"The area is: {area}cm²")
"""
# EXERCISE 2, Shopping cart
"""
def goto_checkout():
    os.system("cls")
    confirm = (input(f"You are about to buy {quantity1} {item1} for ${total1} Are you sure? [Y/n]: "))
    is_confirmed = False
    if confirm.lower() == "y":
        is_confirmed = True
    else:
        is_confirmed = False
    if is_confirmed:
        print(f"You have been charged ${total1}")
    else:
        print(f"You have not been charged")

def goto_checkout2():
    os.system("cls")
    confirm = (input(f"You are about to buy {quantity1} {item1} and {quantity2} {item2} for ${total2} Are you sure? [Y/n]: "))
    is_confirmed = False
    if confirm.lower() == "y":
        is_confirmed = True
    else:
        is_confirmed = False
    if is_confirmed:
        print(f"You have been charged ${total2}")
    else:
        print(f"You have not been charged")

item1 = input("What item would you like to buy?: ")
price1 = float(input("What is the price?: "))
quantity1 = int(input("How many would you like?: "))
total1 = round(price1 * quantity1, 2)

os.system("cls")
print(f"You have added {quantity1} {item1} to your shopping cart!\n Your total is now ${total1}")

choice = int(input("What do you want to do next? [1: Checkout] [2: Shop more]: "))

if choice == 1:
    goto_checkout()
elif choice == 2:
    os.system("cls")
    item2 = input("What item would you like to buy?: ")
    price2 = float(input("What is the price?: "))
    quantity2 = int(input("How many would you like?: "))
    total2 = round(price2 * quantity2 + total1, 2)
    os.system("cls")
    print(f"You have added {quantity2} {item2} to your shopping cart!\n Your total is now ${total2}. Going to checkout")
    goto_checkout2()
else:
    print("Invalid choice, quitting...")
"""
#--------------------------------------------Arithmetic & math--------------------------------------------

friends = 5
remainder = friends % 2 # Modulus (often used to find out if number is even or odd)

print(remainder)