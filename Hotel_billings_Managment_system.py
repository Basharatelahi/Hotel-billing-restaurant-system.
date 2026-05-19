print("---------welcome to the BEH---------")

dishes = {

    "chicken_karahi_full": 1400,
    "chicken_karahi_half":700,
    "baryani_plate_sada":200,
    "baryani_plate_with_chicken":300,
    "sada_polaw":300,
    "polaw_plate_with_chicken":400,
    "chicken_handi_full":1600,
    "chicken_handi_half":800,
    "rosh_full":1800,
    "rosh_half":900,
    "kabab":150,
    "chai_cup":50,
    "lubya_plate":150,
    "chana_plate":150,
    "naan":30,
    "parata":50,
    "mix_sabzi_plate":150,
    "bindi_plate":150,

}

print()
print("-----dishes with prices-----")
print("------------------------------------")


def show_dishes(dishes):
    s_no = 1
    for dish,price in dishes.items():
        print(f"{s_no}.{dish} : {price}.")
        s_no += 1
show_dishes(dishes)        
print("=====================================")
print()


while True:
    customer = input(f"enter your name: ")
    if customer == "":
        print("you not enter name plz enter your name thanks.")
    elif any(char.isdigit() for char in customer):
        print("name is only (text).number or not allowed in name thanks.")
    else:
        break
print() 
   

order_with_qty = {}
def order_selection(dishes,order_with_qty):
    while True:
        while True:
            user_order = input(f"enter dish name for ordering: ").strip().replace(" ","_")
            if user_order == "":
                print("you not enter dish name plz enter dish name for ordering.")
            elif any(char.isdigit() for char in user_order):
                print("the dish name is only (text).number or not allowed in dish name for ordering.")
            else:
                break        

        if user_order in dishes:
            while True:
                try:
                    quantity = int(input(f"enter the quantity(How much '{user_order}' to order): "))
                    print()
                    break
                except ValueError:
                    print("Enter only number in qauntity.")

            if user_order in order_with_qty:
                order_with_qty[user_order] +=  quantity
            else:   
                order_with_qty[user_order] =  quantity 

        else:
            print(f"({user_order}) is not in dishes.")
            continue

        while True:
            choice_of_another_order = input("do you want to order another dish. (yes/no): ").strip().lower()
            if choice_of_another_order == "":
                print("you not enter (yes/no) plz enter (yes/no)")
                print()

            elif any(char.isdigit() for char in choice_of_another_order):
                print("Plz enter only text (yes/no).Number not aloowed.")
                print()

            elif choice_of_another_order == "no":
                print("thanks of ordering.")
                return order_with_qty
            
            elif choice_of_another_order == "yes":
                print()
                break

            else:
                print("invalid inpute")            


orders_details = {}
def show_order_details(customer,orders_details,dishes,order_with_qty):
    for name,quantity in order_with_qty.items():
        qty_price = {}
        price = dishes[name] * quantity
        qty_price["quantity"] = quantity
        qty_price['price'] = price 
        orders_details[name] = qty_price 
    
    print(f"------{customer} Orders_details-----")
    print("---------------------------------")
    for show_name,show_details in orders_details.items():
        print(f"{show_name} (quantity: {show_details["quantity"]}) : Rs {show_details["price"]}.") 
    print("==================================")           


def bill_calculation(customer,orders_details_stores):
    total_bill = 0
    
    print(f"-------{customer} Total bills--------")
    print("-----------------------------------")
    for name,details in orders_details_stores.items():
        qty = details["quantity"]
        price = details["price"]
        print(f"{name} (quantity: {qty}) : Rs {price}.")
        total_bill += price

    discount = 0
    if total_bill >= 2000:
        discount = total_bill * (10/100)
        total_bill -= discount

    
    tax_amount = 0
    if total_bill <= 500:
        tax_amount = 20 

    elif total_bill <= 2000:
        tax_amount = 50

    elif total_bill <= 5000:
        tax_amount = 100
        
    else:
        tax_amount = 500

    total_bill += tax_amount  
    print()
    print("final total bills...")
    print("--------------------")
    print(f"Discount (10%): -Rs {discount}.")
    print(f"Tax applied: +Rs {tax_amount}.")
    print(f"Final total payable: Rs {total_bill}.")
    print("===================================")
  

while True:
    print(f"enter one option in below....\n1.Order Now.\n2.Show order details.\n3.Show Total bill.\
          \n4.exit.")

    while True:
        try:
            option = int(input("enter your option in number(1-4): "))
            break
        except ValueError:
            print("plz enter only number/digit for option.") 
            print()   

    if option == 1:
        print()
        order_selection(dishes,order_with_qty) 
        print()

    elif option == 2:
        print()
        if order_with_qty == {}:
            print("First select option 1. for ordering something.")
            print()
        else:    
            show_order_details(customer,orders_details,dishes,order_with_qty)
            print()

    elif option == 3:
        print()
        if order_with_qty == {}:
            print("First select option 1. for ordering something.")
            print()
        else:    
            bill_calculation(customer,orders_details)
            print()

    elif option == 4:
        print("thanks for using Hotel billing Managment system.")
        break 
    else:
        print("invalid option")
        print()
