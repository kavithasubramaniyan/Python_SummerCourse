import os
import sqlite3
from tkinter import *
from contacts import *
import datetime
import myDatabase




def selection():
    try:
        from tkinter import messagebox
        print("At %s of %d" % (select.curselection(), len(contactlist)))
        return int(select.curselection()[0])
    except IndexError:
        print("Please select contact to update")
        messagebox.showinfo(message="Please select contact")


def addContact():
    from tkinter import messagebox
    if nameVar.get() == "" or phoneVar.get() == "":
        print(nameVar.get(), "Trying to add blank name or contact no")
        messagebox.showinfo(message="Trying to add empty details..Please enter proper details")
    else:
        print("Inserting  ", nameVar.get(),' - ', phoneVar.get())
        c_name = nameVar.get()
        c_number = phoneVar.get()
        myDatabase.insert_records(c_name, c_number)
        contactlist.append([nameVar.get(), phoneVar.get()])
        setList()
    myDatabase.load_records()


def updateContact():
    try:
        old_contact = contactlist[selection()]
        o_name = old_contact.__getitem__(0)
        o_number = old_contact.__getitem__(1)
        from tkinter import messagebox
        if nameVar.get() == "" or phoneVar.get() == "":
            print(nameVar.get(), "Trying to update blank name or contact no")
            messagebox.showinfo(message="Trying to update empty details..Please enter proper details")
        else:
            contactlist[selection()] = [nameVar.get(), phoneVar.get()]
            setList()
            c_name = nameVar.get()
            c_number = phoneVar.get()
            myDatabase.update_table(c_name, c_number, o_name, o_number)
            messagebox.showinfo(message=" Successfully updated %s - %s with new details %s - %s" %(o_name, o_number, c_name, c_number))
    except IndexError:
        print("Please select contact to update")
        messagebox.showinfo(message="Please select contact to update")
    except TypeError:
        print("Type mismatch")


def deleteContact():
    try:
        from tkinter import messagebox
        c_name = contactlist[selection()].__getitem__(0)
        if messagebox.askokcancel(message="Are you sure ? You want to Delete %s" %c_name) == 1:
            print("Trying to delete", c_name)
            myDatabase.delete_records(c_name)
            del contactlist[selection()]
            setList()
            messagebox.showinfo(message="Contacts Deleted Successfully!! Please click save ")
    except IndexError:
        print("Please select contact to delete")
        messagebox.showinfo(message="Please select contact to delete")


def loadContact():
    try:
        from tkinter import messagebox
        myDatabase.load_records()
        name, phone = contactlist[selection()]
        nameVar.set(name)
        phoneVar.set(phone)
    except IndexError:
        print("Please select contact to load")
        messagebox.showinfo(message="Please select contact to load")


def saveContact():
    from tkinter import messagebox
    print("Saving contacts")
    temp = "contactlist = "
    org_file = open("contacts.py", 'w')
    temp = temp + str(contactlist.copy())
    print(temp)
    org_file.write(temp)
    org_file.close()
    messagebox.showinfo(message="All Contacts Saved Successfully!!!")


def exitApp():
    print("Trying to Exit the application")
    from tkinter import messagebox
    messagebox.showinfo(message="Please click save before exiting the app")
    if messagebox.askokcancel(message="Are you sure ? You want to Quit") == 1:
        print('#'*25, "Thank you for using application", '#'*25)
        os._exit(1)


def buildFrame():
    global nameVar, phoneVar, select
    root = Tk()
    frame1 = Frame(root)
    root.title("My Contact List")
    frame1.pack()
    Label(frame1, text="Name:").grid(row=0, column=0, sticky=W)
    nameVar = StringVar()
    name = Entry(frame1, textvariable=nameVar)
    name.grid(row=0, column=1, sticky=W)
    Label(frame1, text="Phone:").grid(row=1, column=0, sticky=W)
    phoneVar = StringVar()
    phone = Entry(frame1, textvariable=phoneVar)
    phone.grid(row=1, column=1, sticky=W)
    frame1 = Frame(root)  # add a row of buttons
    frame1.pack()
    btn1 = Button(frame1, text=" Add  ", command=addContact)
    btn2 = Button(frame1, text="Update", command=updateContact)
    btn3 = Button(frame1, text="Delete", command=deleteContact)
    btn4 = Button(frame1, text=" Load ", command=loadContact)
    btn5 = Button(frame1, text=" Save ", command=saveContact)

    btn1.pack(side=LEFT);
    btn2.pack(side=LEFT)
    btn3.pack(side=LEFT);
    btn4.pack(side=LEFT)
    btn5.pack(side=LEFT)
    frame1 = Frame(root)  # allow for selection of names
    frame1.pack()
    scroll = Scrollbar(frame1, orient=VERTICAL)
    select = Listbox(frame1, yscrollcommand=scroll.set, height=7)
    scroll.config(command=select.yview)
    scroll.pack(side=RIGHT, fill=Y)
    select.pack(side=LEFT, fill=BOTH)
    frame1 = Frame(root)  # add a row of buttons
    frame1.pack()
    btn6 = Button(frame1, text=" EXIT ", command=exitApp)
    btn6.pack(side=BOTTOM)
    conn = sqlite3.connect('contacts.db')
    print("Opened database successfully")
    #myDatabase.create_table()
    myDatabase.load_records()
    conn.close()
    return root


def setList():
    contactlist.sort()
    select.delete(0, END)
    for name, phone in contactlist:
        select.insert(END, name)


root = buildFrame()
setList()

root.mainloop()


