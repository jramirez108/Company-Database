from tkinter import *
from tkinter import messagebox
import mysql.connector
import re

cnx = mysql.connector.connect(
    user='jose', password="ramirez", database='girrafe')
cursor = cnx.cursor()


def showEmployees():
    root = Tk()
    root.title("Employee Database")
    root.geometry("650x500")
    root.configure(background="#4f5b66")
    setRowNames(root)
    showEmployeesQuery = "SELECT * FROM employee"
    cursor.execute(showEmployeesQuery)
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
        w5 = Label(root, text=rows[i][4], foreground="#c0c5ce", background="#4f5b66")
        w5.grid(row=i+2, column=4)
        w6 = Label(root, text=rows[i][5], foreground="#c0c5ce", background="#4f5b66")
        w6.grid(row=i+2, column=5)
        w7 = Label(root, text=rows[i][6], foreground="#c0c5ce", background="#4f5b66")
        w7.grid(row=i+2, column=6)
        w8 = Label(root, text=rows[i][7], foreground="#c0c5ce", background="#4f5b66")
        w8.grid(row=i+2, column=7)
        i += 1

    Button(root, text="Add Employee", command=AddEmployeeWindow, background="#a7adba").grid(row=0)
    Button(root, text="Delete Employee", command=deleteEmployee, background="#a7adba").grid(row=0, column=1)

    return root.mainloop()


def setRowNames(root):
    Label(root, text="Employee ID", bg="#65737e",
        font="bold").grid(row=1, column=0, sticky=W+E)
    Label(root, text="First Name", bg="#65737e",
        font="bold").grid(row=1, column=1, sticky=W+E)
    Label(root, text="Last Name", bg="#65737e", font="bold").grid(row=1, column=2, sticky=W+E)
    Label(root, text="Date of Birth", bg="#65737e",
        font="bold").grid(row=1, column=3, sticky=W+E)
    Label(root, text="Sex", bg="#65737e", font="bold").grid(row=1, column=4, sticky=W+E)
    Label(root, text="Salary", bg="#65737e", font="bold").grid(row=1, column=5, sticky=W+E)
    Label(root, text="Supervisor ID", bg="#65737e",
        font="bold").grid(row=1, column=6, sticky=W+E)
    Label(root, text="Branch ID", bg="#65737e", font="bold").grid(row=1, column=7, sticky=W+E)


def AddEmployeeWindow():
    empW = Tk()
    empW.configure(background="#4f5b66")
    empid = Entry(empW)
    empid.grid(row=0, column=1)
    firstN = Entry(empW)
    firstN.grid(row=1, column=1)
    lastN = Entry(empW)
    lastN.grid(row=2, column=1)
    dob = Entry(empW)
    dob.grid(row=3, column=1)
    sex = Entry(empW)
    sex.grid(row=4, column=1)
    salary = Entry(empW)
    salary.grid(row=5, column=1)
    supId = Entry(empW)
    supId.grid(row=6, column=1)
    branchID = Entry(empW)
    branchID.grid(row=7, column=1)

    Label(empW, text="Employee ID", background="#4f5b66").grid(row=0, column=0)
    Label(empW, text="First Name", background="#4f5b66").grid(row=1, column=0)
    Label(empW, text="Last Name", background="#4f5b66").grid(row=2, column=0)
    Label(empW, text="Date of Birth", background="#4f5b66").grid(row=3, column=0)
    Label(empW, text="Sex", background="#4f5b66").grid(row=4, column=0)
    Label(empW, text="Salary", background="#4f5b66").grid(row=5, column=0)
    Label(empW, text="Supervisor", background="#4f5b66").grid(row=6, column=0)
    Label(empW, text="Branch ID", background="#4f5b66").grid(row=7, column=0)

    def AddEmployee():
        data = (empid.get(), firstN.get(),lastN.get(), dob.get(), sex.get(), salary.get(),
        supId.get(),branchID.get())
        query = """INSERT INTO employee VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"""
        
        try:
            cursor.execute(query, data)
            cnx.commit()
            messagebox.showinfo("Success", "Employee added successfully!")
        except mysql.connector.Error as error:
            messagebox.showerror("Error", "Failed to insert record. {}".format(error))
            
        empW.delete(0, 'end')
        firstN.delete(0, 'end')
        lastN.delete(0, 'end')
        dob.delete(0, 'end')
        sex.delete(0, 'end')
        salary.delete(0, 'end')
        supId.delete(0, 'end')
        branchID.delete(0, 'end')
    Button(empW, text="Add Employee", command=AddEmployee, background="#a7adba").grid(row=8)

    empW.mainloop()

def deleteEmployee():
    root = Tk()
    root.title("Delete Employee")
    root.configure(background="#4f5b66")
    Label(root, text="Employee ID", background="#4f5b66").grid(row=0)
    empID = Entry(root)
    empID.grid(row=0, column=1)
    
    def queryDelete():
        query = "DELETE FROM employee WHERE emp_id=" + str(empID.get())
        try:
            cursor.execute(query)
            cnx.commit()
            messagebox.showinfo("Success", "Employee #" + str(empID.get()) + " Deleted successfully!")
        except mysql.connector.Error as error:
            messagebox.showerror("Error", "Could not delete employee " + error)
    empID.delete(0, 'end')
    Button(root, text="Delete", command=queryDelete, background="#a7adba").grid(row=1, column=1)
