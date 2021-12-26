import sqlite3
con = sqlite3.connect('contacts.db')
cur = con.cursor()
cur.execute("""CREATE TABLE contacts (
                    name text,
                    address text,
                    phone_number text,
                    email_address text
                    )""")
class Contact:
    def __init__(self, name, address, phone_number, email_address):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email_address = email_address
    
    def __repr__(self):
        return f"Contact('{self.name}', '{self.address}', '{self.phone_number}', '{self.email_address}'"

contact_1 = Contact('John Doe', '0000 Random Address', '000-000-0000', 'johndoe@email.com')
contact_2 = Contact('Jane Doe', '1111 Random Address', '111-111-1111', 'janedoe@email.com')


def insert_contact(contact):
    with con:
        cur.execute("INSERT INTO contacts VALUES (?, ?, ?, ?)", (contact.name, contact.address, contact.phone_number, contact.email_address))

def get_contact_by_name(name):
    cur.execute("SELECT * FROM contacts WHERE name = ?", (name,))
    return print(cur.fetchall())

def get_contact_by_address(address):
    cur.execute("SELECT * FROM contacts WHERE address = ?", (address,))
    return print(cur.fetchall())

def get_contact_by_phone_number(phone_number):
    cur.execute("SELECT * FROM contacts WHERE phone_number = ?", (phone_number,))
    return print(cur.fetchall())

def get_contact_by_email_address(email_address):
    cur.execute("SELECT * FROM contacts WHERE email_address = ?", (email_address,))
    return print(cur.fetchall())

def remove_contact(contact):
    with con:
        cur.execute("DELETE from contacts WHERE name = ? AND address = ? AND phone_number = ? AND email_address = ?", (contact.name, contact.address, contact.phone_number, contact.email_address))

def update_name(contact, name):
    with con:
        cur.execute("UPDATE contacts SET name = ? WHERE address = ? AND phone_number = ? AND email_address = ?", (name, contact.address, contact.phone_number, contact.email_address))

def update_address(contact, address):
    with con:
        cur.execute("UPDATE contacts SET address = ? WHERE name = ? AND phone_number = ? AND email_address = ?", (address, contact.name, contact.phone_number, contact.email_address))

def update_phone_number(contact, phone_number):
    with con:
        cur.execute("UPDATE contacts SET phone_number = ? WHERE name = ? AND address = ? AND email_address = ?", (phone_number, contact.name, contact.address, contact.email_address))

def update_phone_number(contact, phone_number):
    with con:
        cur.execute("UPDATE contacts SET phone_number = ? WHERE name = ? AND address = ? AND email_address = ?", (phone_number, contact.name, contact.address, contact.email_address))
        
def update_email_address(contact, email_address):
    with con:
        cur.execute("UPDATE contacts SET email_address = ? WHERE name = ? AND address = ? AND phone_number = ?", (email_address, contact.name, contact.address, contact.phone_number))

insert_contact(contact_1)
insert_contact(contact_2)

con.commit()
con.close()



# This is one of the excellent python projects for beginners. Everyone uses a contact book to save contact details, including name, address, phone number, and even
# email address. This is a command-line project where you will design a contact book application that users can use to save and find contact details. The application should
# also allow users to update contact information, delete contacts, and list saved contacts. The SQLite database is the ideal platform for saving contacts. To handle a
# project with Python for beginners can be helpful to build your career with a good start.

