from tkinter import *
from tkinter import messagebox
import tkinter as tk
import sqlite3

class VotingExtended:
    def __init__(self):
        self.__pass="xyz"
        self.__voters=10

ob=VotingExtended()
key = ob._VotingExtended__pass
v=ob._VotingExtended__voters

print("For Voting Process: 0")
print("For Results: 1")
i=int(input())

top=Tk()
voter=Tk()
mystring=tk.StringVar(top)
mystring2=tk.StringVar(voter)
radio=IntVar()

#DB Work
conn=sqlite3.connect('test.db')
conn.execute('''
        CREATE TABLE IF NOT EXISTS Election (
            id INTEGER NOT NULL,
            Name TEXT,
            count INTEGER
        )
    ''')


def initialize(conn):
    conn.execute('''DELETE FROM Election''')
    conn.commit()
    conn.execute('''
        INSERT INTO Election (id, Name, count)
        VALUES 
            (1, "Sachin Tendulkar", 0),
            (2, "Virat Kohli", 0),
            (3, "MS Dhoni", 0);
    ''')
    conn.commit()
    
def result():
    global s
    while s!=key:
        print("For Accessing The Result Enter Passkey:")
        s=input()
    print("----------------------- Results -----------------------")
    cursor=conn.execute(''' select * from Election''')
    for row in cursor:
        print(row)
    print("-------------------------------------------------------")
    

def voteclose():
    if mystring2.get()==key:
        voter.destroy()
        print("Voting Closed Successfully!!!")
    else:
        messagebox.showwarning("Warning!", "Wrong Passkey")

def selection1(conn):
    messagebox.showinfo("VVPAT", "You Voted For Sachin Tendulkar")
    conn.execute('''
        UPDATE Election
        SET count = count + 1
        WHERE id = 1;
    ''')
    conn.commit()
    voter.after(3000, lambda: messagebox.showwarning("Wait!", "Wait for Three Seconds"))


def selection2(conn):
    messagebox.showinfo("VVPAT", "You Voted For Virat Kohli")
    conn.execute('''
        UPDATE Election
        SET count = count + 1
        WHERE id = 2;
    ''')
    conn.commit()

def selection3(conn):
    messagebox.showinfo("VVPAT", "You Voted For Mahendra Singh Dhoni")
    conn.execute('''
        UPDATE Election
        SET count = count + 1
        WHERE id = 3;
    ''')
    conn.commit()

def vote():
    top.destroy()
    
    voter.title("Voting Window")
    voter.geometry("500x500")
    auth=Label(voter,text="Choose Your Candidate").place(x=100,y=50)
    submitbtn=Button(voter,text="Sachin Tendulkar",activebackground="Red",command=lambda: selection1(conn)).place(x=100,y=120)
    submitbtn2=Button(voter,text="Virat Kohli",activebackground="Red",command=lambda: selection2(conn)).place(x=100,y=180)
    submitbtn3=Button(voter,text="Mahendra Singh Dhoni",activebackground="Red",command=lambda: selection3(conn)).place(x=100,y=240)

    auth=Label(voter,text="For Authority Use Only").place(x=100,y=320)
    e1=Entry(voter,text="Authority Only",textvariable=mystring2,show='*').place(x=100,y=340)
    submitbtn=Button(voter,text="Submit",activebackground="Red",command=voteclose).place(x=100,y=360)
    voter.mainloop()

def get_value():
    if(mystring.get()==key):
        print("Let's Go")
        vote()
    else:
        messagebox.showwarning("Warning!", "Wrong Passkey")


if not i:
    initialize(conn)
    top.title("Welcome To Vote Management System by Alok Tripathi")
    top.geometry("500x400")
    auth=Label(top,text="Enter Passkey for Authority Access").place(x=180,y=100)
    e1=Entry(top,textvariable=mystring,show='*').place(x=200,y=150)
    submitbtn=Button(top,text="Submit",activebackground="Red",command=get_value).place(x=240,y=200)
    top.mainloop()
else:
    result()