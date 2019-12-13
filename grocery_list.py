
'''

Date: 11/29/2019
Project 1: Grocery List

Script will collect information for groceries to be purchased and output required totals.

The task is broken down into three sections.
Section 1 - User Input
Section 2 - loop through the grocery list
Section 3 - provide output to the console
Lastly, reset the item_total & grand_total to 0 although not completely necessary since the script stops
'''

# Data Structure Creation - Create grocery_item dictionary and grocery_history lists.

grocery_item = {}
grocery_history = []

# Section 1 - User Input - Menu Creation and Loop Structure

stop = 'c'

while stop != 'q':

  item_name = input("Item name:\n")
  quantity = input("Quantity purchased:\n")
  cost = input("Price per item:\n")

 # Setting the dictionary and addiing the items to history
  grocery_item ={'name': item_name, 'number': int(quantity), 'price': float(cost)}
  grocery_history.append(grocery_item)

# Prompt to action
  stop = input("Would you like to enter another item?\nType 'c' for continue or 'q' to quit:\n")

# Define variable to hold grand total called 'grand_total'

grand_total = int(0)
item_total = int(0)

# Section 2 - Loop through grocery list 

for i in range(0, len(grocery_history)):
    item_total = int(grocery_history[i]['number']) * float(grocery_history[i]['price'])

    grand_total += item_total

# Section 3 - provide output to the console    
# Output requirements: #2 apple	@	$1.49	ea	$2.98
    
    print(grocery_history[i]['number'], grocery_history[i]['name'], "@", '${:,.2f}'.format(grocery_history[i]['price']),
          " ea ", '${:,.2f}'.format(item_total))

# Output Grand total for Grocery Order
print("Grand Total: ", '${:,.2f}'.format(grand_total))

