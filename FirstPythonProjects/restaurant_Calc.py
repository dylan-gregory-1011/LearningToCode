"""
A first forray into OOP.  TBH the restaurant name should have been something that actually sold the
products that are listed.  Will upgrade on the next go around.
"""
#menu_Order = {'v1':1, 'v2':2, 'v3':3, 'v4': 4, 'v5':5, 'v6':6, 'v7':7, 'v8':8, 'v9':9}
menu_Order = ['1','2','3','4','5','6','7','8','9']
menu_Foods = ['Chicken Stips', 'French Fries', 'Hamburger', 'Hot Dog', 'Large Drink', 'Medium Drink', 'Milk Shake', 'Salad', 'Small Drink']
menu_Prices= [3.50, 2.50,4.00, 3.50, 1.75, 1.50, 2.25, 3.75,1.25]
class my_Menu:

    def __init__(self, price, food):
        self.price = price
        self.food = food
        self.restaurant= 'Taco Bell'
        #self.menu_Number = menu_Number

    def order_Price(self):
        return self.price

    def order_Food(self):
        return self.food
i = 0
while i < (len(menu_Order)):
    menu_Order[i]= my_Menu(menu_Prices[i], menu_Foods[i])
    i+=1


#print menu_Order[8].order_Price()


def restaurant_Calc(str_Order):
    #table_Order = raw_input('What is your tables order?')
    #order= raw_input("What is your tables order?")

    total_Order = []
    total_price= 0.00

    for index in str_Order:
        int_Order = int(index)
        order_Num = int_Order-1
        total_Order.append(menu_Order[order_Num].order_Food())
        total_price+= menu_Order[order_Num].order_Price()

                #food_Or = menu_Order[].order_Food
    print "Your order is "
    for index in range(len(total_Order)):
        print total_Order[index]

    print "You owe %.2f dollars"% (total_price)

str_Order = raw_input("Enter your tables order with no spaces")
restaurant_Calc(str_Order)
