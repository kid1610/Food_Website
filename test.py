cart_list = [{'product_name': 'Moesli', 'quantity': '1'},{'product_name': 'oat cake', 'quantity': '2'},{'product_name': 'Mango Cake', 'quantity': '1'}]

c = {'product_name': 'Moesli', 'quantity': '2'}

list_of_all_values = [value for elem in cart_list
                      for value in elem.values()]
if c['product_name'] not in list_of_all_values:
    cart_list.append(c)
else:
    cart_list = [i for i in cart_list if not (i['product_name'] == c['product_name'])]
    cart_list.append(c)

print(cart_list)