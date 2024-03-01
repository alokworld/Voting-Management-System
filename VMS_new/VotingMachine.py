from tkinter import *
from tkinter import messagebox
import tkinter as tk
import sqlite3
from CentralBody.Passkey import Passkey
import hashlib

#Object of the imported Passkey class
ob = Passkey()

class VotingMachine:
    def __init__(self):
        self.__l = []  # Encapsulated list

        self.__key = ob.encrypted
        self.__conn = sqlite3.connect('test.db')

        self.__cursor = self.__conn.cursor()
        self.__cursor.execute("SELECT Name, id FROM Election")

        for row in self.__cursor:
            self.__l.append(row[0])
            self.__l.append(row[1])

    def get_candidate_list(self):
        return self.__l

    def get_passkey(self):
        return self.__key

    def get_connection(self):
        return self.__conn
    

#Components needed for GUI
top=Tk()
voter=Tk()
mystring=tk.StringVar(top)
mystring2=tk.StringVar(voter)
radio=IntVar()
    
#Function for vote closing
def voteclose():
    if hashlib.sha256(mystring2.get().encode()).hexdigest()==vote_instance.get_passkey():
        voter.destroy()
        print("Voting Closed Successfully!!!")
    else:
        messagebox.showwarning("Warning!", "Wrong Passkey")

def selection1(conn):
    textgen="You Voted For "+l[0]
    id=l[1]
    messagebox.showinfo("VVPAT",textgen)
    conn.execute('''
        UPDATE Election
        SET count = count + 1
        WHERE id = ?;
    ''',(id,))
    conn.commit()


def selection2(conn):
    textgen="You Voted For "+l[2]
    id=l[3]
    messagebox.showinfo("VVPAT",textgen)
    conn.execute('''
        UPDATE Election
        SET count = count + 1
        WHERE id = ?;
    ''',(id,))

    conn.commit()

def selection3(conn):
    textgen="You Voted For "+l[4]
    id=l[5]
    messagebox.showinfo("VVPAT",textgen)
    conn.execute('''
        UPDATE Election
        SET count = count + 1
        WHERE id = ?;
    ''',(id,))
    conn.commit()

#Here Voting Takes Place
def vote():
    top.destroy()
    
    voter.title("Voting Window")
    voter.geometry("500x500")
    auth=Label(voter,text="Choose Your Candidate").place(x=100,y=50)


    submitbtn=Button(voter,text=l[0],activebackground="Red",command=lambda: selection1(vote_instance.get_connection())).place(x=100,y=120)
    submitbt2=Button(voter,text=l[2],activebackground="Red",command=lambda: selection2(vote_instance.get_connection())).place(x=100,y=180)
    submitbtn3=Button(voter,text=l[4],activebackground="Red",command=lambda: selection3(vote_instance.get_connection())).place(x=100,y=240)

    auth=Label(voter,text="For Authority Use Only").place(x=100,y=320)
    e1=Entry(voter,text="Authority Only",textvariable=mystring2,show='*').place(x=100,y=340)
    submitbtn=Button(voter,text="Submit",activebackground="Red",command=voteclose).place(x=100,y=360)
    voter.mainloop()

#Authentication to start vote
def get_value():
    if(hashlib.sha256(mystring.get().encode()).hexdigest()==vote_instance.get_passkey()):
        print("Let's Go")
        vote()
    else:
        messagebox.showwarning("Warning!", "Wrong Passkey")


vote_instance=VotingMachine()
l = vote_instance.get_candidate_list()
top.title("Welcome To Vote Management System by Alok Tripathi")
top.geometry("500x400")
auth=Label(top,text="Enter Passkey for Authority Access").place(x=180,y=100)
e1=Entry(top,textvariable=mystring,show='*').place(x=200,y=150)
submitbtn=Button(top,text="Submit",activebackground="Red",command=get_value).place(x=240,y=200)
top.mainloop()

vote_instance.get_connection().close()
