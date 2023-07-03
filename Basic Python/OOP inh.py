class Restaurant:
    def __init__(self,menu_items,book_table,costumer_order):
        self.menu_items={}
        self.book_table=[]
        self.costumer_order=[]
        
    def add_item_to_menu(self,item,price):
        self.menu_items[item]=price
        
        return menu

    def book_tables(self,table_no):
        self.book_table=table_no
        return table_no
        
    def costumer_order(self,c_order):
        self.costumer_order=c_order
        order=[]
        order.append(c_order)
        return order
    def order_details(self):
        return f"Costumer order: {self.costumer_order} at table: {self.book_table}"
    
    
r1=Restaurant("Burger",5,"Burger")

r1.order_details()