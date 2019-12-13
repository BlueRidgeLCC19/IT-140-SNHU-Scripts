# Get the filepath from the command line

import sys

F1 = sys.argv[1]
F2 = sys.argv[2]

# Your code goes here

file1 = open(F1, 'r')
file2 = open(F1, 'r')

data1 = file1.read()
data2 = file2.read()


# Functions
# load_accounts - parses the data and strips the account info into a 2D list.
# instructions - parse the command list into a working list that can be executed
# verify - uses account_num & pin to verify account existence & access for transaction execution
# add - function will add funds to account
# sub - function will deduct funds to account with check to ensure balance > sub amount
# Load account information from file and split by | delimiter

def load_accounts(data1):
    lines1 = data1.split("\n")
    for i in range(0, len(lines1)):
        lines1[i] = lines1[i].split("|")
        return lines1

def instructions(data2):
    lines2 = data2.split("\n")
    for i in range(0, len(lines2)):
        lines2[i] = lines2[i].split("|")
        return lines2


def verify(acct, acct_num, pin):
    for i in range(0, len(acct)):
        if acct[i][0] == acct_num and acct[i][1] == pin:
            return [i]
        return -1


def add(tran, index, amt):
    tran[index][2] += amt


def sub(tran, index, amt):
    if amt <= tran[index][2]:
        tran[index][2] -= amt


# -------------------------------------------------------------------------
#
#    Main code body, where functions are called
#
# -------------------------------------------------------------------------

# Load accounts
accounts = load_accounts(data1)

#  Load Transactions
commands = instructions(data2)

# Find index and verify account_num and pin code
# Perform commands from F2

for i in range(0, len(commands)):
    accountNum = commands[i][2]
    pin = commands[i][3]
    trans = verify(commands, accountNum, pin)

    for i in range(0, len(trans)):
        amount = commands[i][1]
        if commands[i][0] == "add":
            add(accounts, i, amount)
        if commands[i][0] == "sub":
            sub(accounts, i, amount)

        # Execute join function to rebuild file into "write" list

    for i in range(0, len(accounts)):
        accounts[i] = "|".join(accounts[i])
        output = "\n".join(accounts)

# Write the account changes to file
        open(F1, 'w').write(output)

file.close()


