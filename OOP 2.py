class BankAccount:
    def __init__(self,account_number,balance,date_of_opening,costumer_name):
        self.account_number=account_number
        self.balance=balance
        self.date_of_opening=date_of_opening
        self.costumer_name=costumer_name
        
        
    def deposit(self,amount1):
        self.balance+=amount1
        return self.balance
    
    def widthdraw(self,amount):
        
        if amount>self.balance:
            return print(f"Insufficient Credits")
        else:
            self.balance-=amount
            return self.balance
        
    def __str__(self):
       return (f"Your balance is {self.balance}")
    

c1=BankAccount(312211,400,2003,"Jamal")

c1.deposit(100)
print(c1.balance)

print(c1.__str__())


