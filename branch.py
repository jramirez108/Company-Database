from tkinter import *
from tkinter import messagebox
import mysql.connector
import re

cnx = mysql.connector.connect(
    user='jose', password="ramirez", database='girrafe')
cursor = cnx.cursor()


def showBranch():
    root = Tk()
    root.title("Branch Database")
    root.geometry("420x300")
    root.configure(background="#4f5b66")
    Button(root, text="Add Branch", command=addBranch, background="#a7adba").grid(row=0, column=0)
    setRowNames(root)
    showBranchQuery = "SELECT * FROM branch"
    cursor.execute(showBranchQuery)
    rows = cursor.fetchall()
    
    for i in range(0, len(rows)):
        w1 = Label(root, text=rows[i][0], foreground="#c0c5ce", background="#4f5b66")
        w1.grid(row=i+2, column=0)
        w2 = Label(root, text=rows[i][1], foreground="#c0c5ce", background="#4f5b66")
        w2.grid(row=i+2, column=1)
        w3 = Label(root, text=rows[i][2], foreground="#c0c5ce", background="#4f5b66")
        w3.grid(row=i+2, column=2)
        w4 = Label(root, text=rows[i][3], foreground="#c0c5ce", background="#4f5b66")
        w4.grid(row=i+2, column=3)
        i += 1

    
    return root.mainloop()

def setRowNames(root):
    Label(root, text="Branch ID", bg="#65737e", font="bold").grid(row=1, column=0)
    Label(root, text="Branch Name", bg="#65737e", font="bold").grid(row=1, column=1)
    Label(root, text="Manager ID", bg="#65737e", font="bold").grid(row=1, column=2)
    Label(root, text="Manager Start Date", bg="#65737e", font="bold").grid(row=1, column=3)

def addBranch():
    add = Tk()
    add.geometry("400x150")
    add.configure( bg="#65737e")
    add.title("Add Branch")
    Label(add, text="Branch ID",  bg="#65737e", font="bold").grid(row=0, column=0)
    Label(add, text="Branch Name",  bg="#65737e", font="bold").grid(row=1, column=0)
    Label(add, text="Manager ID",  bg="#65737e", font="bold").grid(row=2, column=0)
    Label(add, text="Manager Start Date",  bg="#65737e", font="bold").grid(row=3, column=0)
    
    branchID = Entry(add)
    branchID.grid(row=0, column=1)
    name = Entry(add)
    name.grid(row=1, column=1)
    manId = Entry(add)
    manId.grid(row=2, column=1)
    start = Entry(add)
    start.grid(row=3, column=1)
    
    def addBranchDB():
        data = (branchID.get(), name.get(), manId.get(), start.get())
        query = """INSERT INTO branch VALUES(%s,%s,%s,%s)"""
        try:
            cursor.execute(query, data)
            cnx.commit()
            messagebox.showinfo("Success", "Branch added successfully!")
        except mysql.connector.Error as error:
            messagebox.showerror("Error", "Failed to insert record. {}".format(error))

        branchID.delete(0, 'end')
        name.delete(0, 'end')
        manId.delete(0, 'end')
        start.delete(0, 'end')
    Button(add, text="Submit", command=addBranchDB, background="#a7adba").grid(row=4)
