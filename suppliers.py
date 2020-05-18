from tkinter import *
from tkinter import messagebox
import mysql.connector
import re

cnx = mysql.connector.connect(
    user='jose', password="ramirez", database='girrafe')
cursor = cnx.cursor()


def showSuppliers():
    root = Tk()
    root.title("Supplier Database")
    root.geometry("500x500")
    root.configure(background="#4f5b66")
    setRowNames(root)
    Query = "SELECT * FROM branch_supplier"
    cursor.execute(Query)
    rows = cursor.fetchall()
    
    for i in range(0, len(rows)):
        w1 = Label(root, text=rows[i][0], foreground="#c0c5ce", background="#4f5b66", font="bold")
        w1.grid(row=i+2, column=0)
        w2 = Label(root, text=rows[i][1], foreground="#c0c5ce", background="#4f5b66", font="bold")
        w2.grid(row=i+2, column=1)
        w3 = Label(root, text=rows[i][2], foreground="#c0c5ce", background="#4f5b66", font="bold")
        w3.grid(row=i+2, column=2)
        i += 1

    Button(root, text="Add Supplier", command=addSupplier, background="#a7adba").grid(row=0)
    return root.mainloop()

def setRowNames(root):
    Label(root, text="Branch ID", bg="#65737e", font="bold").grid(row=1, column=0, sticky=W+E)
    Label(root, text="Suplier Name", bg="#65737e", font="bold").grid(row=1, column=1, sticky=W+E)
    Label(root, text="Supply Type", bg="#65737e", font="bold").grid(row=1, column=2,sticky=W+E)

def addSupplier():
    add = Tk()
    add.geometry("300x150")
    add.title("Add Supplier")
    add.configure(background="#4f5b66")
    Label(add, text="Branch ID ", background="#4f5b66", font="bold").grid(row=0, column=0)
    Label(add, text="Supplier Name", background="#4f5b66", font="bold").grid(row=1, column=0)
    Label(add, text="Supply Type", background="#4f5b66", font="bold").grid(row=2, column=0)
    
    ID = Entry(add)
    ID.grid(row=0, column=1)
    name = Entry(add)
    name.grid(row=1, column=1)
    supType = Entry(add)
    supType.grid(row=2, column=1)
    
    
    
    def addClientDB():
        data = (ID.get(), name.get(), supType.get())
        query = """INSERT INTO branch_supplier VALUES(%s,%s,%s)"""
        try:
            cursor.execute(query, data)
            cnx.commit()
            messagebox.showinfo("Success", "Supplier added successfully!")
        except mysql.connector.Error as error:
            messagebox.showerror("Error", "Failed to insert record. {}".format(error))
        
        ID.delete(0, 'end')
        name.delete(0, 'end')
        supType.delete(0, 'end')
            
    Button(add, text="Submit", command=addClientDB, background="#a7adba").grid(row=4)

