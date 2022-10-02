# Group Expense Tracker

### Main.py

dataframe: all data will be stored in nested dictionary format.


class API:

	def create_group:
		1) checks the group name: 
			a) present -> error 
			b) not present --> new group created (group_name as key)
		2) Value stored in the dataframe:
			a) Name: name of grp
			b) Items: list of expense
			c) Members: members of the grp
		returns dataframe

	def add_expense:
		1) checks the group name: [error handling]
			a) present -> value store in group 
			b) not present -->  error
		2) checks if value == sum of paidby and value == sum of owedby. [error handling]
		3) create expense record: (name, value, paidby,owedby)
		4) Update members: (in case a new member is present in the expense record)
		returns dataframe		

	def update_expense:
		1) checks the group name: [error handling]
			a) present -> update value in expense
			b) not present --> error 
		2) search expense in items:
		3) update the expense value needs to be updated:
			a) value
			b) paidby [error handling](value == sum of paidby)
			c) owedby [error handling](value == sum of owedby)
		returns dataframe

	def delete_expense:
		1) checks the group name: [error handling]
			a) present -> delete expense if present
			b) not present --> error 
		2) search for expenses in items:
		3) delete expenses from items 
		returns dataframe

	def balance:
		1) checks the group name: [error handling]
			a) present -> return balance based on the expense record in items
			b) not present --> error  		
		2) create a balance record = {}
		3) Value stored in balance record: 
			( name, balance (person name(total balance, owes_to, owed_by)))
		4) Structure of balance record:			
                    {
                      "name": "Home",
                      "balances": {
                        "A": {
                          "total_balance": -100.0
                          "owes_to": [{"C": 100}],
                          "owed_by": []
                        },
                        "B": {
                          "total_balance": 0.0
                          "owes_to": [],
                          "owed_by": []
                        },
                        "C": {
                          "total_balance": 100.0
                          "owes_by": [{"A": 100}],
                          "owed_to": []
                        }
                      }
                      }
		print(balance record)

### subfunctions.py

def add members(): add members to the array

def check() :  compare value with paidby [for error handling]

## Overall function analysis:

1 main file and 1 sub file

5 main functions and 2 subfunctions

Create group --> add, update, delete expense of the group

Balance: give total balance, owes_to, owed_by for each member of the group

## Storage analysis:
1 Main bucket containing all the values

## Could be improved:
1. Separate bucket to store different values and assign a unique id to form an E-R relation between databases.
2. Use of no-SQL database.
