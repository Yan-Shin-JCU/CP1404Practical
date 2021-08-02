num_items = int(input('Number of items: '))
if num_items < 0:
    while num_items < 0:
        print('Invalid number of items!')
        num_items = int(input('Number of items: '))

while num_items > 0:
    item_counter = 0
    total_cost = 0

    while item_counter < num_items:
        total_cost += float(input('Price of item: '))
        item_counter += 1

    if total_cost > 100:
        total_cost = total_cost - (total_cost * (10/100))
        print('Total price for {num} items is ${price:.2f}' .format(num=num_items, price=total_cost))
    else:
        print('Total price for {num} items is ${price:.2f}'.format(num=num_items, price=total_cost))
