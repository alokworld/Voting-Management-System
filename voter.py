from tkinter import *
from tkinter import messagebox
import tkinter as tk
import time as tt

top=Tk()
voter=Tk()
mystring=tk.StringVar(top)
mystring2=tk.StringVar(voter)
radio=IntVar()
s=""
a=0
b=0
c=0

def result():
    global s
    while s!="alok":
        print("For Accessing The Result Enter Passkey:")
        s=input()
    print("----------------------- Results -----------------------")
    print("Candidate Name \t\tVotes")
    print("S Tendulkar: \t\t"+str(a))
    print("V Kohli:  \t\t"+str(b))
    print("MS Dhoni:\t\t"+str(c))
    print("-------------------------------------------------------")
    

def voteclose():
    if mystring2.get()=="alok":
        voter.destroy()
        result()
    else:
        messagebox.showwarning("Warning!", "Wrong Passkey")

def selection1():
    global a
    messagebox.showinfo("VVPAT", "You Voted For Sachin Tendulkar")
    a=a+1
    messagebox.showwarning("Wait!", "Wait for Three Seconds")
    tt.sleep(3)


def selection2():
    global b
    messagebox.showinfo("VVPAT", "You Voted For Virat Kohli")
    b=b+1
    messagebox.showwarning("Wait!", "Wait for Three Seconds")
    tt.sleep(3)

def selection3():
    global c
    messagebox.showinfo("VVPAT", "You Voted For Mahendra Singh Dhoni")
    c=c+1
    messagebox.showwarning("Wait!", "Wait for Three Seconds")
    tt.sleep(3)

def vote():
    top.destroy()
    
    voter.title("Voting Window")
    voter.geometry("500x500")
    auth=Label(voter,text="Choose Your Candidate").place(x=100,y=50)
    submitbtn=Button(voter,text="Sachin Tendulkar",activebackground="Red",command=selection1).place(x=100,y=120)
    submitbtn2=Button(voter,text="Virat Kohli",activebackground="Red",command=selection2).place(x=100,y=180)
    submitbtn3=Button(voter,text="Mahendra Singh Dhoni",activebackground="Red",command=selection3).place(x=100,y=240)

    auth=Label(voter,text="For Authority Use Only").place(x=100,y=320)
    e1=Entry(voter,text="Authority Only",textvariable=mystring2,show='*').place(x=100,y=340)
    submitbtn=Button(voter,text="Submit",activebackground="Red",command=voteclose).place(x=100,y=360)
    voter.mainloop()

def get_value():
    if(mystring.get()=="alok"):
        print("Let's Go")
        vote()
    else:
        messagebox.showwarning("Warning!", "Wrong Passkey")

top.title("Welcome To Vote Management System by Alok Tripathi")
top.geometry("500x400")
auth=Label(top,text="Enter Passkey for Authority Access").place(x=180,y=100)
e1=Entry(top,textvariable=mystring,show='*').place(x=200,y=150)
submitbtn=Button(top,text="Submit",activebackground="Red",command=get_value).place(x=240,y=200)
top.mainloop()
