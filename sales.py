from tkinter import *
from tkinter import messagebox
import mysql.connector
import re

cnx = mysql.connector.connect(
    user='jose', password="ramirez", database='girrafe')
cursor = cnx.cursor()


def showSales():
    root = Tk()
    root.title("Client Database")
    root.geometry("300x300")
    root.configure(background="#4f5b66")
    setRowNames(root)
    Query = "SELECT * FROM works_with"
    cursor.execute(Query)
    rows = cursor.fetchall()
    
    for i in range(0, len(rows)):
        w1 = Label(root, text=rows[i][0], foreground="#c0c5ce", background="#4f5b66")
        w1.grid(row=i+2, column=0)
        w2 = Label(root, text=rows[i][1], foreground="#c0c5ce", background="#4f5b66")
        w2.grid(row=i+2, column=1)
        w3 = Label(root, text=rows[i][2], foreground="#c0c5ce", background="#4f5b66")
        w3.grid(row=i+2, column=2)
        i += 1

    Button(root, text="Add Sale", command=addSales, background="#a7adba").grid(row=0)
    return root.mainloop()

def addSales():
    add = Tk()
    add.geometry("300x150")
    add.title("Add Sale")
    add.configure(background="#4f5b66")
    Label(add, text="Employee ID", background="#4f5b66", font="bold").grid(row=0, column=0)
    Label(add, text="Client ID", background="#4f5b66", font="bold").grid(row=1, column=0)
    Label(add, text="Total Sales $", background="#4f5b66", font="bold").grid(row=2, column=0)
    
    empID = Entry(add)
    empID.grid(row=0, column=1)
    clieID = Entry(add)
    clieID.grid(row=1, column=1)
    sales = Entry(add)
    sales.grid(row=2, column=1)
    
    
    
    def addClientDB():
        data = (empID.get(), clieID.get(), sales.get())
        query = """INSERT INTO works_with VALUES(%s,%s,%s)"""
        try:
            cursor.execute(query, data)
            cnx.commit()
            messagebox.showinfo("Success", "Sale added successfully!")
        except mysql.connector.Error as error:
            messagebox.showerror("Error", "Failed to insert record. {}".format(error))
            
    Button(add, text="Submit", command=addClientDB, background="#a7adba").grid(row=4)
    

def setRowNames(root):
    Label(root, text="Employee ID", bg="#65737e", font="bold").grid(row=1, column=0)
    Label(root, text="Client ID", bg="#65737e", font="bold").grid(row=1, column=1)
    Label(root, text="Total Sales", bg="#65737e", font="bold").grid(row=1, column=2)
