from tkinter import *
from tkinter import messagebox
import mysql.connector
import re
from employee import *
from branch import *
from client import *
from sales import *
from suppliers import *


main = Tk()
main.configure(background="#4f5b66")
main.title("Database")
main.geometry("300x300")
Label(main, text="Databases", font=('Helvetica', 24), foreground="#a7adba", background="#4f5b66").pack()
Button(main, text="Employees", command=showEmployees, background="#a7adba").pack()
Button(main, text="Branch", command=showBranch, background="#a7adba").pack()
Button(main, text="Clients", command=showClient, background="#a7adba").pack()
Button(main, text="Suppliers", command=showSuppliers, background="#a7adba").pack()
Button(main, text="Sales", command=showSales, background="#a7adba").pack()
main.mainloop()
