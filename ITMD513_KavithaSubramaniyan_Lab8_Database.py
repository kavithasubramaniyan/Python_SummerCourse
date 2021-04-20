import sqlite3


# A function to create a table
def create_table():
    conn = sqlite3.connect('contacts.db')
    print('**' * 20, "Creating table in %s Database" % conn, '**' * 20)
    conn.execute('''CREATE TABLE Kavitha_Contacts
             (NAME TEXT     NOT NULL UNIQUE,
              CONTACT  TEXT    NOT NULL UNIQUE,
              PRIMARY KEY (NAME, CONTACT));''')
    print("Table created successfully")
    conn.close()
    print('**' * 50)


# A function to update a table
def update_table(c_name, c_number,o_name,o_number):
    print('**' * 20, "Updating Records in Database", '**' * 20)
    from tkinter import messagebox
    try:
        conn = sqlite3.connect('contacts.db')
        update_cmd = "UPDATE Kavitha_Contacts SET NAME = '%s',CONTACT= '%s'  where NAME = '%s' AND CONTACT = '%s'" %(c_name, c_number, o_name, o_number)
        conn.execute(update_cmd)
        conn.commit
        print("Total number of rows updated :", conn.total_changes)
        print("Successfully updated %s - %s with new details %s - %s" % (o_name, o_number, c_name, c_number))
        cursor = conn.execute("SELECT name, CONTACT from Kavitha_Contacts")
        for row in cursor:
            print("Name : ", row[0], "\nContact Number : ", row[1])
        conn.close()
    except sqlite3.IntegrityError:
        print("Violating integrity constraint. Contact with this number already exists !")
        messagebox.showinfo(message="Contact with this number already exists !")
    print('**' * 50)


# A function to delete from a table
def delete_records(c_name):
    print('**' * 20, "Deleting Records in Database", '**' * 20)
    conn = sqlite3.connect('contacts.db')
    delete_cmd = "DELETE from Kavitha_Contacts where NAME = '%s';"%c_name
    conn.execute(delete_cmd)
    conn.commit()
    print("Total number of rows deleted :", conn.total_changes)
    print("Successfully deleted %s from database" %(c_name))
    cursor = conn.execute("SELECT name, CONTACT from Kavitha_Contacts")
    for row in cursor:
        print("Name : ", row[0], "\nContact Number : ", row[1])
    print('**' * 50)

# A function to insert into a table
def insert_records(c_name, c_number):
    print('**' * 20, "Inserting Records in Database", '**' * 20)
    from tkinter import messagebox
    try:
        conn = sqlite3.connect('contacts.db')
        insert_cmd = "INSERT INTO Kavitha_Contacts (NAME,CONTACT)VALUES ('%s','%s')"%(c_name, c_number)
        conn.execute(insert_cmd);
        conn.commit()
        conn.close()
        print("Inserted Records successfully !!!")
        messagebox.showinfo(message="Contacts Added Successfully!! Please click save")
    except sqlite3.IntegrityError:
        print("Violating integrity constraint. Contact with this number already exists !")
        messagebox.showinfo(message="Contact with this number already exists !")
    print('**' * 50)


# .A function to read (load in) record(s) from a table
def load_records():
    print('**' * 20, "Loading Records from Database", '**' * 20)
    conn = sqlite3.connect('contacts.db')
    cursor = conn.execute("SELECT NAME, CONTACT from Kavitha_Contacts")
    for row in cursor:
        print("Name : ", row[0], "\nContact Number : ", row[1])
    conn.close()
    print('**' * 50)
