import sqlite3

def add_customer(name, address, contact, email):
    conn = sqlite3.connect('database.db', timeout=15)
    c = conn.cursor()

    c.execute('''INSERT INTO customers (NAME, ADDRESS, CONTACT, EMAIL) VALUES (?, ?, ?, ?)''', (name, address, contact, email))

    conn.commit()
    print('Successful')
    conn.close()

# add_customer('Jane Sat', 'Texas', '587-654', 'jane@gmail.com')

# def add_order()
# conn = sqlite3.connect('database.db')
# c = conn.cursor()

# c.execute('SELECT * FROM customers')

# conn.commit()
# print('Successful')
# conn.close()