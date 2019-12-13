import sys

'''
Date: 11/29/2019

Project Three: ATM Script 

1. Collect customer input
2. Calculate the ending balance
3. Display the results to the customer
'''

# Global Variable
account_balance = float(500.25)

'''
printBalance() function sets expected format and display for customer account balance.
:return nothing
:param nothing
'''
def printbalance():
    print('Your current balance:\t' + '${:,.2f}'.format(account_balance))

'''
deposit() function facilitates adding funds to the customers account balance and displaying on screen information.
:return a + b)
:param a = temp deposit_amount | b = temp account_balance
'''
def deposit(a, b):
    return a + b

'''
withdraw(() function enables the customer to withdrawal money from their account balance. It invokes a test to ensure
there is enough money in the account balance and executes based on the reesult.
:return nothing
:params a = temp withdrawal_amount | temp account_balance 
'''

def withdraw(a, account_balance):
    if a > account_balance:
        print('${:,.2f}'.format(a) + ' is greater than your account balance of ' + '${:,.2f}'.format(account_balance))

    else:
        return account_balance - a

def quit(msg):
    print(msg)

'''
Customer Portal Menu - used to instruct the user what options are available to accessing and managing their account.
'''
stop = 'go'
while stop.upper() != 'Q':
    print()
    print('Enter \'B\' Balance | \'D\' Deposit | \'W\' Withdrawal | \'Q\' Quit:')
    userchoice = input("What would you like to do?\t")

    if (userchoice.upper() == 'D'):
        deposit_amount = float(input('How much would you like to deposit today?\n'))
        account_balance = deposit(deposit_amount, account_balance)
        #print(account_balance)
        print('Deposit was ' + '${0:,.2f}'.format(deposit_amount) + ', current balance is ${0:,.2f}'.format(
            account_balance))

    if (userchoice.upper() == 'B'):
        printbalance()

    if (userchoice.upper() == 'W'):
        withdrawal_amount = float(input('How much would you like to withdraw today?\n'))
        account_balance = withdraw(withdrawal_amount, account_balance)

        print('Withdrawal amount was ${:,.2f}'.format(withdrawal_amount) + ', current balance is ${:,.2f}'.format(
            account_balance))

    if (userchoice.upper() == 'Q'):
        quit('Thank you for banking with us.')
