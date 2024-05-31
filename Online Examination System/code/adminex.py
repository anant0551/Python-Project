from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
def cladmin():
    import admin 
def ex():
    import ex
def mod():
    import modex

def exam1():
    exam=tk.Tk()
    exam.geometry('600x372')
    exam.title('EXAMINATIONS SECTION')
    exam.resizable(0,0)
    examimg=ImageTk.PhotoImage(file=r'F:\main project\photo\exam.jpg')
    exm=tk.Label(exam,image=examimg)
    exm.place(x=0,y=20)
    ex1=tk.Label(exam,text='Welcome To Examination Section',font=('elephant','20'),
                    justify= CENTER,fg='black')
    ex1.place(x=10,y=50)
    exam1=tk.Button(exam,text='**NEW EXAM**',font=('impact'),
                    justify=CENTER,fg='white',bg="black",command=lambda:[exam.destroy(),ex()])
    exam1.place(x=100,y=100)
    exam4=tk.Button(exam,text='**EXAM MODIFICATION**',font=('impact'),
                    justify=CENTER,fg='white',bg="black",command=lambda:[exam.destroy(),mod()])
    exam4.place(x=100,y=150)
    exam2=tk.Button(exam,text='**SCHEDULES OF EXAM**',font=('impact'),
                    justify=CENTER,fg='white',bg="black")
    exam2.place(x=100,y=200)
    exam3=tk.Button(exam,text='**PREVIOUS EXAM RECORDS',font=('impact'),
                    justify=CENTER,fg='white',bg="black")
    exam3.place(x=100,y=250)   
    ret1=tk.Button(exam,text='GO BACK',font=('impact','8'),
                justify=CENTER,fg='red',command=lambda:[exam.destroy(),cladmin()])
    ret1.place(x=540,y=330)
    exam.mainloop()
def cand():
    cand=tk.Tk()
    cand.geometry('768x599')
    cand.title('CANDIDATE SECTION')
    cand.resizable(0,0)
    canimg=ImageTk.PhotoImage(file=r'F:\main project\code\cand.jpg')
    cnd=tk.Label(cand,image=canimg)
    cnd.place(x=0,y=20)
    ca1=tk.Label(cand,text='Welcome To Candidate Section',font=('elephant','20'),
                    justify= CENTER,fg='black')
    ca1.place(x=10,y=50)
    cand1=tk.Button(cand,text='**NEW CANDIDATE UPLOAD**',font=('impact'),
                    justify=CENTER,fg='white',bg="black")
    cand1.place(x=100,y=200)
    cand2=tk.Button(cand,text='**CANDIDATE MODIFICATION**',font=('impact'),
                    justify=CENTER,fg='white',bg="black")
    cand2.place(x=100,y=250)
    cand3=tk.Button(cand,text='**CANDIDATE RECORDS**',font=('impact'),
                    justify=CENTER,fg='white',bg="black")
    cand3.place(x=100,y=300)
    ret2=tk.Button(cand,text='GO BACK',font=('impact','8'),
                justify=CENTER,fg='red',command=lambda:[cand.destroy(),cladmin()])
    ret2.place(x=700,y=530)
    cand.mainloop()
def user():
    
    user1=tk.Tk()
    user1.geometry('513x400')
    user1.title('USER SECTION')
    user1.resizable(0,0)
    userimg=ImageTk.PhotoImage(file=r'F:\main project\code\users.png')
    usr=tk.Label(user1,image=userimg)
    usr.place(x=0,y=20)
    usr1=tk.Label(user1,text='Welcome To User Section',font=('elephant','20'),
                    justify= CENTER,fg='black')
    usr1.place(x=10,y=50)
    usrb1=tk.Button(user1,text=('**USER','Chr(39)','S DETAILS**'),font=('impact'),
                    justify=CENTER,fg='white',bg="black")
    usrb1.place(x=100,y=200)
    usr2=tk.Button(user1,text='**USER MODIFICATION**',font=('impact'),
                    justify=CENTER,fg='white',bg="black")
    usr2.place(x=100,y=250)
    ret3=tk.Button(user1,text='GO BACK',font=('impact','8'),
                justify=CENTER,fg='red',command=lambda:[user1.destroy(),cladmin()])
    ret3.place(x=460,y=360)
    user1.mainloop()
