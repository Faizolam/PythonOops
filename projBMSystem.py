# custName,orderId,order,orderQut,orderDate all can stor and if needed export in csv and if needed customer can update or change and only orderId can fetch all details of order.
import pandas as pd
from datetime import datetime
class Bakery:
    all_orders = []  # Class variable to store all orders, It will access from all instance of class
    def __init__(self,custName) -> None:
        self.custName = custName
        self.orderId = 0
        self.orders = []
        # self.order = order
        # self.orderQut = orderQut
        # self.orderDate = datetime


        self.__menu()

    def __menu(self):
        user_input = input(f"""
                        Hello {self.custName}, Your Sweet Clicks And Tasty Picks Await – Welcome To Our Online Bakery!
                        1. Enter 1 to order.
                        2. Enter 2 to update order.
                        3. Enter 3 to view order details.
                        4. Enter 4 to export in csv.
                        5. Enter 5 to Exit.
    """)
        
        if user_input == '1':
            self.get_order()
            print("You order has successfully booked")
        elif user_input == '2':
            self.update_order()
        elif user_input == '3':
            # pass
            self.get_order_detail()
        elif user_input == '4':
            self.export_to_csv()
        else:
            print("Thank you for visit.")


    def get_order(self):
        self.orderId += 1
        dics = {
            'orderId' : self.orderId,
            'order' : input("What would you like to purches: "),
            'orderQut' : int(input("What quantity do you want: ")),
            'orderDate' : datetime.now().replace(second=0,microsecond=0).strftime("%d-%m-%Y %H:%M")
        }
        self.orders.append(dics)
        Bakery.all_orders.append(dics)
        return dics
    
    def get_order_detail(self):
        df=pd.DataFrame(self.orders)
        return df
    # def get_ordre(self):
    #     self.orderId = +1
    #     self.order = input("What would you like to purches: ")
    #     self.orderQut = int(input("What quantity do you want: "))
    #     self.orderDate = datetime.now().replace(second=0,microsecond=0)
    #     return [self.orderId,self.custName,self.order,self.orderQut,self.orderDate]
    def update_order():
        pass
    def export_to_csv(self):
        for order in  Bakery.all_orders:
            print(order)
    
