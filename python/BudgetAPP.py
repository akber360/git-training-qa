class banking:
    def __init__(self,shop,money):
        self.money = int(money)

    def get_balance(self):
        return self.money    #gives you balance money
    
    def withdraw(self, amount):
        self.money=int(self.money) - int(amount)
        return self.money   # takes money and - amount returns updated var
     
    def transfer(self, place, amount):
        if amount < self.money:
            self.withdraw(amount)
            place.deposit(amount)
            return self.money 
    def deposit(self, amount):
        self.money=int(self.money) + int(amount)
        return self.money

food =banking ("food",10)
clothes =banking ("clothing",10)
entertainement =banking ("entertainment",10)