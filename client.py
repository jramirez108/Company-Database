from tkinter import *
from tkinter import messagebox
import mysql.connector
import re

cnx = mysql.connector.connect(
    user='jose', password="ramirez", database='girrafe')
cursor = cnx.cursor()


def showClient():
    root = Tk()
    root.title("Client Database")
    root.geometry("300x250")
    root.configure(background="#4f5b66")
    setRowNames(root)
    showClientQuery = "SELECT * FROM client"
    cursor.execute(showClientQuery)
    rows = cursor.fetchall()
    
    for i in range(0, len(rows)):
        w1 = Label(root, text=rows[i][0], foreground="#c0c5ce", background="#4f5b66")
        w1.grid(row=i+2, column=0)
        w2 = Label(root, text=rows[i][1], foreground="#c0c5ce", background="#4f5b66")
        w2.grid(row=i+2, column=1)
        w3 = Label(root, text=rows[i][2], foreground="#c0c5ce", background="#4f5b66")
        w3.grid(row=i+2, column=2)
        i += 1

    Button(root, text="Add Client", command=addClient, background="#a7adba").grid(row=0)
    return root.mainloop()

def setRowNames(root):
    Label(root, text="Client ID", bg="#65737e", font="bold").grid(row=1, column=0, sticky=W+E)
    Label(root, text="Client Name", bg="#65737e", font="bold").grid(row=1, column=1, sticky=W+E)
    Label(root, text="Branch ID", bg="#65737e", font="bold").grid(row=1, column=2, sticky=W+E)

def addClient():
    add = Tk()
    add.geometry("300x150")
    add.title("Add Client")
    add.configure(background="#4f5b66")
    Label(add, text="Client ID", background="#4f5b66", font="bold").grid(row=0, column=0)
    Label(add, text="Client Name", background="#4f5b66", font="bold").grid(row=1, column=0)
    Label(add, text="Branch ID", background="#4f5b66", font="bold").grid(row=2, column=0)
    
    ID = Entry(add)
    ID.grid(row=0, column=1)
    name = Entry(add)
    name.grid(row=1, column=1)
    branchID = Entry(add)
    branchID.grid(row=2, column=1)
    
    
    
    def addClientDB():
        data = (ID.get(), name.get(), branchID.get())
        query = """INSERT INTO client VALUES(%s,%s,%s)"""
        try:
            cursor.execute(query, data)
            cnx.commit()
            messagebox.showinfo("Success", "Client added successfully!")
        except mysql.connector.Error as error:
            messagebox.showerror("Error", "Failed to insert record. {}".format(error))
        ID.delete(0, 'end')
        name.delete(0, 'end')
        branchID.delete(0, 'end')
    Button(add, text="Submit", command=addClientDB, background="#a7adba").grid(row=4)
    