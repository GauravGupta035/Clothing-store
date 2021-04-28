import sqlite3

def add_customer(name, address, contact, email):
    conn = sqlite3.connect('database.db', timeout=15)
    c = conn.cursor()

    c.execute('''INSERT INTO customers (NAME, ADDRESS, CONTACT, EMAIL) VALUES (?, ?, ?, ?)''', (name, address, contact, email))

    conn.commit()
    print('Successful')
    conn.close()

# add_customer('Jin Woo', 'Seoul', '888-555', 'jinwoo@gmail.com')

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

# add_shippings(2, 3, 1)