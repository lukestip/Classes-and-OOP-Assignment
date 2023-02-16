import FoodClass as fc

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

'''
customer_id	Name	address	email	phone	member_status
570	Danni Sellyar	97 Mitchell Way Hewitt Texas 76712	dsellyarft@gmpg.org	254-555-9362	False
569	Aubree Himsworth	1172 Moulton Hill Waco Texas 76710	ahimsworthfs@list-manage.com	254-555-2273	True
'''

dict = {'trans1': ['2/15/2023', 'The Lone Patty', 17, 569],
        'trans2': ['2/15/2023', 'The Octobreakfast', 18, 569],
        'trans3': ['2/15/2023', 'The Octoveg', 16, 570],
        'trans4': ['2/15/2023', 'The Octoburger', 20, 570],
        }

order_total = 0

# Create customer instance
# customer = fc.Customer(570, 'Danni Sellyar', '97 Mitchell Way Hewitt Texas 76712', 'dsellyar@gmpg.org', '254-555-9362', False)
customer = fc.Customer(569, 'Aubree Himsworth', '1172 Moulton Hill Waco Texas 76710',
                       'ahimsworthfs@list-manage.com', '254-555-2273', True)

# Turn dictionary into transaction class instances
trans1 = fc.Transaction(
    dict['trans1'][0], dict['trans1'][1], dict['trans1'][2], dict['trans1'][3])
trans2 = fc.Transaction(
    dict['trans2'][0], dict['trans2'][1], dict['trans2'][2], dict['trans2'][3])
trans3 = fc.Transaction(
    dict['trans3'][0], dict['trans3'][1], dict['trans3'][2], dict['trans3'][3])
trans4 = fc.Transaction(
    dict['trans4'][0], dict['trans4'][1], dict['trans4'][2], dict['trans4'][3])

transactionList = [trans1, trans2, trans3, trans4]
discount = .2

print(f'Customer Name: {customer.getName()}')
print(f'Phone: {customer.getPhone()}')

for i in transactionList:
    if i.getCustomerid() == customer.getid():
        print(f'Order Item: {i.getItemName()} Price: ${i.getCost():,.2f}')
        order_total += i.getCost()

print(f'Order total: ${order_total:,.2f}')
if customer.getMemstatus() == True:
    print(f'Member Discount: ${order_total*discount:,.2f}')
    print(
        f'Total Cost after discount: ${order_total-(order_total*discount):,.2f}')
