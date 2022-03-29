import time

print("Welcome to the bar.")

name = input("What is your name?\n")

print("Hello " + name + ", what would you like to order?\n")

menu = "----- Menu -----\n1) White Coffee\n2) Black Coffee\n3) Water\n4) Coca-Cola\n5) Pepsi\n"

print(menu)

orderNumber = input("Enter your order: ")

print("Your order of " + orderNumber + " will be ready shortly ...\n")

if orderNumber == "1":
    time.sleep(10)
elif orderNumber == "2":
    time.sleep(6)
elif orderNumber == "3":
    time.sleep(1)
elif orderNumber == "4":
    time.sleep(3)
elif orderNumber == "5":
    time.sleep(3)

print("Here is your order " + name + ", enjoy your day.")

