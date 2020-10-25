print("Welcome to Object oriented piggybank")
statement = []

class Piggybank:
    """ this is classs decostinr"""

    def __init__(self):
        """ this is init moducle"""
        
        self.balance = 0
        self.lt = 0
    

    def deposit(self,amount):
        
        """ this is deposit module"""
        if amount > 0:
            self.balance = self.balance + amount
            self.lt = amount
            if len(statement) >= 10:
                statement.pop(0)
                statement.append(amount)
            else:
                statement.append(amount)
        else:
            print("Enter the valid amount")


    def withdraw(self,amount):
        """this is withdrwa module"""

        if amount <= self.balance:
            self.balance = self.balance - amount
            self.lt = -amount
    
            if len(statement) >= 10:
                statement.pop(0)
                statement.append(-amount)
            else:
            
                statement.append(-amount)
        else:
            print("insufficnet funds")


    def account_info(self):
        """this is account_info """       
        
        print("your balance is -->", self.balance)
        print("your last trascation is -->", self.lt)


    def statements(self):
        " this module show 10 statements"
        if len(statement) ==0:
            print("you don't have any trascation")
        else:
            for i in range(len(statement)):
                print("Trascation |{}| -->".format(i+1),statement[i])



    def manu(self):
        """this is for manu"""

        print("______Manu_______")
        print("prees 'd' for deposit")
        print("press 'w' for withdraw")
        print("press 'a' for account info")
        print("press 's' for statemetns")
        print("press 'q' for quite")


pg = Piggybank()

print("______Manu_______")
print("prees 'd' for deposit")
print("press 'w' for withdraw")
print("press 'a' for account info")
print("press 's' for statemetns")

action = input("Enter -->").lower()

while action != 'q':

    if action == "d":
        amount = int(input("Enter the amount for deposited-->"))
        pg.deposit(amount)
        pg.manu()
    elif action == 'w':
        amount = int(input("Enter the amout for witdrawing-->"))
        pg.withdraw(amount)
        pg.manu()
    elif action == 's':
        pg.statements()
        pg.manu()
    elif action == 'a':
        pg.account_info()
    else:
        print("Ente the corect input")
    
    action = input("Enter --->").lower()
print("thakn you")