from operator import itemgetter
print("*"*117 + "\n" + "\t\t\t"*3 + "!!! Welcome to Online Shopping !!!\n" + "*"*117)
passwd = input("Enter the admin password please : ")    # the password is admin
if passwd == "admin":
    print("*"*117 + "\n" + "\t\t\t"*3 + "   !!! Admin module started !!!\n" + "*"*117)
    while 1:
        op = int(input("Enter the choice for which you wish to perform the following operations : "
             "\n1] Add Product in stock\n2] Update Product in stock\n3] Remove product from the stock\n4]"
             " View all products in stock\n5]"
             " Logout admin\n"))
        if op == 1:
            print(" Now you can add product(s) to the stock\n ")
            n = int(input("Enter the number of products you wish to add : "))
            print
            st = {}
            for i in range(n):
                key = input("Please enter the name of the product : ")
                value = int(input("Please enter the price of the product : "))
                st[key] = value
                print
        elif op == 2:
            opkey = input("Enter the product which you wish to update : ")
            i0 = sorted(st, key=itemgetter(0))
            for i in range(len(i0)):
                if i0[i] == opkey:
                    print("!! You can now update the price of the product !! \n")
                    newprice = int(input("Enter the new price for the desired product : "))
                    st[opkey] = newprice
                    print("The product has been updated!!\n")
        elif op == 3:
            print("Now you can delete any product of your wish ")
            deletedprod = input("Enter the product you wish to delete : ")
            if deletedprod in st:
                del st[deletedprod]
                print("\nThe product has been deleted from the stock successfully!")
            else:
                print("Sorry! Product not found in the stock.Try again!!")
        elif op == 4:
            print("You are now viewing the products in the stock : ")
            productList = st.keys()
            for k in sorted(productList):
                print("Product name : %-10s" % k, "\tPrice : %10d" % st[k])
        elif op == 5:
            break
else:
    print("Not an admin")
    print("Entering customer module.... \n")
print("*"*117 + "\n" + "\t\t\t"*3 + "!! Welcome consumer to online shopping !!\n" + "*"*117)
while 1:
    op2 = int(input("Enter the choice for which you wish to perform the following operations : "
               "\n1] View all the products in the stock\n2] Add to the shopping basket\n"
               "3] View all the products in the basket\n"
               "4] Search for a product in the stock\n5] Remove a product from the basket\n6]"
               " Print Invoice\n7] Sign out\n"))
    if op2 == 1:
        print("You are now viewing the products in the stock : ")
        productList = st.keys()
        for k in sorted(productList):
            print("Product name : %-10s" % k, "\tPrice : %3d" % st[k])
    elif op2 == 2:
        basket = {}
        n1 = int(input("Enter the number of products you want to add to your basket : "))
        for i in range(n1):
            bprod = input("Enter the product from the stock you wish to add : ")
            quant = int(input("Enter the quantity of the product you wish to add to the basket : "))
            if bprod in st:
                basket[bprod] = quant
        listofbasket = basket.items()
    elif op2 == 3:
        print("You are now viewing the products in the basket : ")
        basketKeys = basket.keys()
        for l in sorted(basketKeys):
            print("Product name : %-10s" % l, "\tQuantity : %3d" % basket[l])
    elif op2 == 4:
        searchprod = input("Enter the name of the product you wish to search for in the stock : ")
        i0 = sorted(st, key=itemgetter(0))
        if searchprod in i0:
            print("Product found! Its price is :\t", st[searchprod])
        else:
            print("Product not found!")
    elif op2 == 5:
        deleteprod = input("Enter the product you wish to delete from the basket : ")
        del basket[deleteprod]
        print("\nThe product has been deleted from the basket successfully!")
    elif op2 == 6:
        print("*"*117 + "\n" + "\t\t\t"*4 + "Billing Invoice\n" + "*"*117)
        bill = 0
        basketKeys = basket.keys()
        for k in sorted(basketKeys):
            price = st[k]
            quantity = basket[k]
            print("Product name = %-10s" % k, "\tQuantity = %3d" % basket[k], "\tPrice = %3d" % st[k], "\tTotal = %3d" % (price*quantity))
            bill = bill + (price*quantity)
        print("Total Bill = ", bill)
    elif op2 == 7:
        break
    else:
        print("Wrong option selected! Try again !!")