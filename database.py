# customers = {}

# def add_customer(name, address, contact, email, password):
#     for i in range(100):

#         customers[i]['Name'] = name
#         customers[i]['Address'] = address
#         customers[i]['Contact'] = contact
#         customers[i]['Email'] = email
#         customers[i]['Password'] = password

# add_customer('', '', '', '', '')

# customers = {
#     'Name': [],
#     'Address': [],
#     'Contact': [],
#     'Email': [],
#     'Password': [],
#     'Cart Items': {
#         'Product Name': [],
#         'Product Price': []
#     }
# }

# def add_customer(name, address, contact, email, password):
#     customers['Name'].append(name)
#     customers['Address'].append(address)
#     customers['Contact'].append(contact)
#     customers['Email'].append(email)
#     customers['Password'].append(password)

# # add_customer('Gaurav Gupta', 'Bangalore, Karnataka', 132456, 'gaurav@gmail.com', 1234)

# def add_to_cart(name, product_name, product_price):
#     for k, v in customers:
#         for i in v:
#             if i == 'Gaurav Gupta':
#                 customers['']
# print(customers)


import sqlite3

def add_customer(name, address, contact, email):
    conn = sqlite3.connect('database.db', timeout=15)
    c = conn.cursor()

    c.execute('''INSERT INTO customers (NAME, ADDRESS, CONTACT, EMAIL) VALUES (?, ?, ?, ?)''', (name, address, contact, email))

    conn.commit()
    print('Successful')
    conn.close()

add_customer('Jin Woo', 'Seoul', '888-555', 'jinwoo@gmail.com')

def add_product(product_name, category, size, price):
    conn = sqlite3.connect('database.db', timeout=15)
    c = conn.cursor()

    c.execute('''INSERT INTO products (PRODUCT_NAME, CATEGORY, SIZE, PRICE) VALUES (?, ?, ?, ?)''', (product_name, category, size, price))

    conn.commit()
    print('Successful')
    conn.close()

# add_product('Floral skirt', 'Women', 'M', '399.99')

def add_order(customerID):
    conn = sqlite3.connect('database.db', timeout=15)
    c = conn.cursor()

    c.execute('''INSERT INTO orders (CUSTOMER_ID) VALUES (?)''', (customerID))

    conn.commit()
    print('Successful')
    conn.close()

# add_order('3')

def add_shippings(orderID, productID, quantity):
    conn = sqlite3.connect('database.db', timeout=15)
    c = conn.cursor()

    c.execute('''INSERT INTO shippings (ORDER_ID, PRODUCT_ID, QUANTITY) VALUES (?,?,?)''', (orderID, productID, quantity))

    conn.commit()
    print('Successful')
    conn.close()

# add_shippings(1, 3, 1)