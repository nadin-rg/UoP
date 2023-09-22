#PART 1

#The circumference of a circle is calculated by 2πr, where π = 3.14159 (rounded to five decimal places). 
#Write a function called print_circum that takes an argument for the circle’s radius and prints the circle's radius. 

def print_circum(r):
    pi = 3.14159
    circumference = 2*pi*r
    return circumference

#Call your print_circum function three times with different values for radius. 
print("The circle circumference is: ",round(print_circum(3),5))
print("The circle circumference is: ",round(print_circum(6),5))
print("The circle circumference is: ",round(print_circum(9),5))
#the round function help us to reduce the quantity of decimal number, I selected a maximun of 5 degits after the period

#PART 2

def purchase(arg):
    if arg == 1:
        product = "Item 1"
        description = ""
        price = 200
    if arg == 2:
        product = "Item 2"
        description = ""
        price = 400
    if arg == 3:
        product = "Item 3"
        description = ""
        price = 600
    if arg == "combo_1":
        product = "Combo 1"
        description = " (Item 1 + Item 2)"
        price = 540
    if arg == "combo_2":
        product = "Combo 2"
        description = "(Item 2 + Item 3)"
        price = 900
    if arg == "combo_3":
        product = "Combo 3"
        description = "(Item 1 + Item 3)"
        price = 720
    if arg == "combo_4":
        product = "Combo 4 "
        description = "(Item 1 + Item 2 + Item 3)"
        price = 900
    print("Super Store Online")
    print("-------------------------------------------------")
    print("Product(s)                                  Price")
    print(product,"                                  ",price)
    print(description)
    print("___________________________________________________")
    print("Delivery COntact: +57 302338472")
    print("                thanks for your buy              ")
    

purchase("combo_1")



def purchase(): #this function shows the catalogue of the store
    product_1 = "Item 1" # name of the Item
    price_1 = 200  #Item´s price
    product_2 = "Item 2"
    price_2 = 400
    product_3 = "Item 3"
    price_3 = 600
    product_c1 = "Combo 1 (Item 1 + Item 2)"
    price_c1 = int((price_1 + price_2) - (price_1 + price_2)*10/100) # with this expresion is calculated the sum of item 1 and item 2 less the  10%
    product_c2 = "Combo 2 (Item 2 + Item 3)"
    price_c2 = int((price_2 + price_3) - (price_2 + price_3)*10/100)# with this expresion is calculated the sum of item 2 and item 3 less the  10%
    product_c3 = "Combo 3 (Item 1 + Item 3)"
    price_c3 = int((price_1 + price_3) - (price_1 + price_3)*10/100) # with this expresion is calculated the sum of item 1 and item 2 less the  10%
    product_c4 = "Combo 4 (Item 1 + Item 2 + Item 3)"
    price_c4 = int((price_1 + price_2 + price_3) - (price_1 + price_2 + price_3)*25/100) # with this expresion is calculated the sum of item 1 , item 2 and item 3 
                                                                                         #less the  25%
    print("                                                 ") # using the print function can I diagram the structure od the catalogue
    print("_________________________________________________")
    print("Super Store Online") # name of the store
    print("-------------------------------------------------")
    print("Product(s)                                  Price")
    print(product_1,"                                      ",price_1)
    print(product_2,"                                      ",price_2)
    print(product_3,"                                      ",price_3)
    print(product_c1,"                   ",price_c1)
    print(product_c2,"                   ",price_c2)
    print(product_c3,"                   ",price_c3)
    print(product_c4,"          ",price_c4)
    print("_________________________________________________")
    print("      Delivery Contact: +57 302338472")
    print("                thanks for your buy              ")
    

purchase()


    