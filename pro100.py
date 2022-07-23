class atm(value):
    def __init__ (self, name, creditNumber, dateOpened, Amount):
        self.name = name
        self.creditNumber = creditNumber
        self.dateOpened = dateOpened
        self.Amount = Amount
    def checkBalance(self):
        print("Your balance is $" + str(self.Amount) + ".")
    def withdraw(self):
        moneyTaken = int(input("How much money would you like to take out? "))
        print("Sucess! $" + str(moneyTaken) + " withdrawn! New account balance: $" + str(self.Amount - moneyTaken) + " remaining.")
        self.Amount = self.Amount - moneyTaken
    def deposit(self):
        moneyGiven = int(input("How much money would you like to deposit? "))
        print("Done! $" + str(moneyGiven) + " deposited in account! $" + str(self.Amount + moneyGiven) + " is the new balance of your account.")
        self.Amount = self.Amount + moneyGiven
John = atm("John", 90019063, "Jan 13 2021", 630)