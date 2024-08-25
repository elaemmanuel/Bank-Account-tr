from bank_accounts import *


lari_acct = BankAccount(90000, 'Lari')



def menu(bank_acct):
        while True:
            print("\nWelcome to MyBank!\n")
            print("Press 1 For Deposit\n")
            print("Press 2 For Withdrawal\n")
            print("Press 3 to Check Balance\n")
            print("Press 4 to Transfer\n")
            print("Press 5 to Exit\n")

            choice = int(input("\nEnter Number: \n"))
            if choice == 1:
                amount_to_deposit = float(input("\nEnter amount to be deposited: \n"))
                bank_acct.deposit(amount_to_deposit)
            elif choice == 2:
                amount_to_withdraw = float(input("\nEnter amount to withdraw: \n"))
                bank_acct.withdraw(amount_to_withdraw)
            elif choice == 4:
                amount_to_transfer = float(input("\nEnter amount to transfer: \n"))
                lari_acct.transfer(amount_to_transfer, bank_acct)
            elif choice == 3:
                bank_acct.get_balance()
            elif choice == 5:
                print("\nThank you for Banking with us!🚀🚀\n")
                print ("👋\n")
                break
            else:
                print("\nInvalid Number. Enter 1, 2, 3, 4, or 5.\n")


#create another account
acct_name = input("\nEnter your account names: \n")
initial_amount = int(input("\nEnter amount to open the Account with... (This amount will be credit to your account): \n"))

bank_acct = BankAccount(initial_amount, acct_name)
menu(bank_acct)

