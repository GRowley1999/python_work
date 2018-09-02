sandwich_orders = ['ham', 'cheese', 'chicken', 'ham and pickle', 'pastrami', 
            'pastrami', 'pastrami']
        
print("The deli has run out of pastrami!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)