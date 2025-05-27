menu={
    'Pizza ': 40,
    'Pasta': 80,
    'Coffe': 90,
    'Burger': 60,
    'Salat': 50,
}
# Greedy

print("Welcome to my Resturant")
print("Pizza : 40\nPasta : 80\nCoffe : 90\nBurger : 60\nSalat : 50 ")

order_total=0


item_1= input("Enter the name of item you want to order = ")

if item_1 in menu:
    order_total +=menu[item_1];
    print(f"Your item {item_1} have been added to your order ")
else:
    print(f"Order item {item_1} is not available yet! ")    
another_item=input("Do you want to add another order? (Yes/No): ")
if another_item=="Yes":
    item_2=input("Enter the name of item you want another items: ")
    if item_2 in menu:
        order_total +=menu[item_2] 
        print(f"Your item {item_2} have been added to your order ") 
    else:
        print(f"Order item {item_1} is not available yet") 
print(f"The total Amount of item is {order_total}")             