print("Welcome to our restaurent.\nHere's the menu:")

menu = {
  "Pizza": 40,
  "Pasta" : 50,
  "Burger": 60,
  "Salad": 70,
  "Coffee":80
}

print("=====================================")   
print("Pizza : Rs 40\nPasta : Rs 50\nBurger: 60\nSalad: 70 \nCoffee: 80")

print("=====================================\n")


order_total = 0

print("\n")

item_1 = input("Enter Your first item you want to order = ")

if item_1 in menu:
  order_total = order_total + menu[item_1]
  print(f"Your item {item_1} has been added to your order")

else:
  print(f"Ordered item {item_1} is not available yet!")

print("\n")

another_order = input("Do you want to add another item? (Yes/No) ")

if another_order == "Yes":
  item_2 = input("Enter Your Second item you want to order = ")

  if item_2 in menu:
    order_total = order_total + menu[item_1]
    print(f"Your item {item_2} has been added to your order")

  else:
    print(f"Ordered item {item_2} is not available yet!")
print("\n")

print("==============Pay=================")  

print(f"The total amount of items to pay is:{order_total}")

print("=============Thanks! You Can Order More=================")