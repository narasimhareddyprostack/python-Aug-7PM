class bank_Account:
    ''' Account Opending '''
    account_No = 5657
    def __init__(self):
        
        print(id(self))
        print('*' * 10)

    def deposit():
        print("Pleaser Deposit 50 USD")


b = bank_Account()
print(id(b))
bank_Account.deposit()

