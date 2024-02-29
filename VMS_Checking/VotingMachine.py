from tkinter import *
from tkinter import messagebox
import tkinter as tk
import sqlite3
from CentralBody.Passkey import Passkey


ob = Passkey()
l=[]

class MainSetUp:
    def __init__(self):

        self.key = ob._Passkey__pass
        self.conn = sqlite3.connect('test.db')
        self.conn_voters = sqlite3.connect('voters.db')

        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT Name,id FROM Election")

        for row in self.cursor:
            l.append(row[0])
            l.append(row[1])

top=Tk()
voting=Tk()
mystring=tk.StringVar(top)
mystring2=tk.StringVar(voting)
radio=IntVar()
    

def voteclose():
    if mystring2.get()==vote_instance.key:
        voting.destroy()
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
    eligibility()


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

def vote():
    
    voting.title("Voting Window")
    voting.geometry("500x500")
    auth=Label(voting,text="Choose Your Candidate").place(x=100,y=50)


    submitbtn=Button(voting,text=l[0],activebackground="Red",command=lambda: selection1(vote_instance.conn)).place(x=100,y=120)
    submitbt2=Button(voting,text=l[2],activebackground="Red",command=lambda: selection2(vote_instance.conn)).place(x=100,y=180)
    submitbtn3=Button(voting,text=l[4],activebackground="Red",command=lambda: selection3(vote_instance.conn)).place(x=100,y=240)

    auth=Label(voting,text="For Authority Use Only").place(x=100,y=320)
    e1=Entry(voting,text="Authority Only",textvariable=mystring2,show='*').place(x=100,y=340)
    submitbtn=Button(voting,text="Submit",activebackground="Red",command=voteclose).place(x=100,y=360)
    voting.mainloop()

def eligibility():
        print("Entire Voter ID")
        id_to_check=int(input())

# Execute the SQL query
        can_vote=vote_instance.conn_voters.execute("SELECT voted FROM VoterList WHERE id = ? AND voted = FALSE", (id_to_check,))

# Fetch the result
        can_vote1 = can_vote.fetchone()

# Check if a matching record was found
        if can_vote1:
            vote()
            vote_instance.conn_voters.execute('''
            UPDATE VoterList
            SET voted = TRUE
            WHERE id = ?;
        ''',(id_to_check,))
        else:
            print("Voter Not Eligible")
def get_value():
    if(mystring.get()==vote_instance.key):
        top.destroy()
        eligibility()
        
    else:
        messagebox.showwarning("Warning!", "Wrong Passkey")

vote_instance=MainSetUp()
top.title("Welcome To Vote Management System by Alok Tripathi")
top.geometry("500x400")
auth=Label(top,text="Enter Passkey for Authority Access").place(x=180,y=100)
e1=Entry(top,textvariable=mystring,show='*').place(x=200,y=150)
submitbtn=Button(top,text="Submit",activebackground="Red",command=get_value).place(x=240,y=200)
top.mainloop()

vote_instance.conn.close()
vote_instance.conn_voters.close()