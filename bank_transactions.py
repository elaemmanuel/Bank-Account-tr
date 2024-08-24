from bank_accounts import *


lari_acct = BankAccount(90000, 'Lari')

#create another account
acct_name = input("\nEnter your account names: \n")
initial_amount = int(input("\nEnter amount to open the Account with... (This amount will be credit to your account): \n"))

bank_acct = BankAccount(initial_amount, acct_name)
print("")
bank_acct.get_balance()
print("")
amount_to_deposit = int(input("Enter amount to be deposited: \n"))
bank_acct.deposit(amount_to_deposit)
print("")
amount_to_withdraw = int(input("Enter amount to withdraw: \n"))
bank_acct.withdraw(amount_to_withdraw)
print("")
amount_to_transfer = int(input("Enter amount to be transfered: \n"))
lari_acct.transfer(amount_to_transfer, bank_acct)
print("")

