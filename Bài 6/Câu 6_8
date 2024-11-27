class Bank:
    Account_type = "Savings"
    location = "Guntur"

    def __init__(self, name, Account_Number, balance):
        self.name = name
        self.Account_Number = Account_Number
        self.balance = balance
        self.location = Bank.location

    def __repr__(self):
        return f'Khách hàng: {self.name}, Số tài khoản: {self.Account_Number}, Số dư: {self.balance}'

    def start(self):
        print("Welcome to the SBI ATM Machine")
        print("-------------------------------")
        account_pin = int(input("Please enter your pin number: "))
        if account_pin == 123:
            self.Account()
        else:
            print("Pin Incorrect. Please try again.")
            self.Error()

    def Error(self):
        account_pin = int(input("Please enter your pin number again: "))
        if account_pin == 123:
            self.Account()
        else:
            print("Pin Incorrect. Please try again.")
            self.Error()

    def Account(self):
        print("Your Card Number is: XXXX XXXX XXXX 1337")
        print("Would you like to deposit/Withdraw/Check Balance?")
        print("""
1) Balance
2) Withdraw
3) Deposit
4) Quit
""")
        option = int(input("Please enter your choice: "))
        if option == 1:
            self.Balance()
        elif option == 2:
            self.Withdraw()
        elif option == 3:
            self.Deposit()
        elif option == 4:
            self.Exit()
        else:
            print("Invalid option. Please try again.")
            self.Account()

    def Balance(self):
        print("Balance: ", self.balance)
        self.Account()

    def Withdraw(self):
        w = int(input("Please enter the amount to withdraw: "))
        if self.balance >= w:
            self.balance -= w
            print("Your transaction was successful.")
            print("Your Balance: ", self.balance)
        else:
            print("Transaction canceled: Insufficient funds.")
        self.Account()

    def Deposit(self):
        d = int(input("Please enter the amount to deposit: "))
        self.balance += d
        print("Your transaction was successful.")
        print("Balance: ", self.balance)
        self.Account()

    def Exit(self):
        print("Thank you for using our ATM. Goodbye!")


t1 = Bank('mahesh', 1453210145, 5000)
print(t1)
t1.start()

                















            
