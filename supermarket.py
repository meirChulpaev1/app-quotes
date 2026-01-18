def supermarket():

    list = []

    while True:

        main_screen=int(input("Hello To select/add a product, press 1. To delete a product, press 2. To complete the purchase, press 3."))
        if main_screen != 1 and main_screen != 2 and main_screen != 3:
            break

        if main_screen == 1:
            ProductName = input("input your Product name")
            priceProduct = int(input("input the price of the product"))
            amountUnits = int(input("input the amount of units"))
            
            found = False
            
            for i in list:
                if ProductName in i:
                    i[ProductName]["amount"] += amountUnits
                    found = True
                    break
            if not found:
                new_doct = {ProductName:{"price" : priceProduct , "amount" : amountUnits}} 
                list.append(new_doct)   

        elif main_screen == 2:
            if not list:
                print("empty list")
                continue

            ProductName = input("input your Product name")
            if ProductName not in list:
                print("eror")
            
            amountUnits_to_remove = int(input(f"Input the amount of units to remove (or type a large number to remove all): "))

            if list [ProductName]["amount"] <= amountUnits_to_remove:
                print(f"removing all")
                del list[ProductName]

            else:
                list[ProductName]["amount"] -= amountUnits_to_remove
                print(f"Removed {amountUnits_to_remove} units of {ProductName}. Remaining: {list[ProductName]['amount']}")    

            

        elif main_screen == 3:
            if not list:
                break
            total_price = 0
            for i in list:
                for name,details in new_doct.items():
                    i = details["price"] * details["amount"]
                    total_price += i
                    print(f"prodact:{name},amount:{details['amount']}")
            
            print(f"{total_price}")
            print("Thank you for shopping with us")
            break




           

                            


                
                
                
            
