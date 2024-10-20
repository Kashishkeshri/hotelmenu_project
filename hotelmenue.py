#define a menue of restaurant
menu ={'Pizza':50,'Burger':30,'noodles':60,'Pasta':80,'Cold_Coffee':50,'cold_drink':40}

#greet
print("Welcom to our restaurant")
print("The menu is :-\n")
print("Pizza:Rs50\nBurger:Rs30\nnoodles:Rs60\nPasta:Rs80\nCold_Coffee:Rs50\ncold_drink:Rs40")
order_total = 0
item1 = input("Enter the name of item you want to order = ")
if item1 in menu:
    order_total +=menu[item1]
    print(f"your item {item1}has been added to your order")
else: 
    print(f"Ordered item {item1}is not available yet!")


while True:
        another_order = input("Do you want to add another item?(yes/no)")
        
        if another_order == "yes":
            item2 = input("Enter the name of item = ")
            if item2 in menu:
                order_total +=menu[item2]    
                print(f"Item {item2} has been added to your order")
            else:
             print(f"Ordered item {item1}is not available yet!")
        else:
            break

    
print(f"the total amount you have to pay for items you ordered is {order_total}")
