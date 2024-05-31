import tkinter as tk
import sqlite3
from tkinter import *
from PIL import Image, ImageTk
import adminex

        
def clmain():
    import MAIN

def adclose():
    admin.destroy()

class calad():
    def _clad(self):
        import admin

def submitact():
     
    user = Username.get()
    passw = password.get()
    print(f"The name entered by you is {user} {passw}")
    logintodb(user, passw)
  
 
def logintodb(user, passw):
     
    # If password is enetered by the
    # user
    con=sqlite3.connect('database\school.db')
    cur = con.cursor() 
   
    try:
        cur.execute('select * from user_id where USERNAME="'+user+'" and PASSWORD="'+passw+'"')
        rec=cur.fetchall()
        
        if len(rec)==0:
            print('Invalid user or password!')
        else:
            adclose()
            admin1()
            
    except :
        print('Username not found try another Username')


def admin1():
    admin12=tk.Tk()
    admin12.geometry('700x400')
    admin12.title("Welcome User")
    admin12.resizable(0,0)
    admin1img=ImageTk.PhotoImage(file=r'F:\main project\photo\teacher.jpg')
    teac=tk.Label(admin12,image=admin1img)
    teac.place(x=0,y=0)
  
    win1=tk.Label(admin12,text='Welcome To The Online Examination System',font=('elephant','20'),
                    justify= CENTER,fg='red')
    win1.place(x=10,y=50)
    examsec=tk.Button(admin12,text='>>EXAMINATIONS SECTION<<',font=('elephant'),
                        justify=CENTER,bg="black",fg="white",command=lambda:[admin12.destroy(),adminex.exam1()])
    examsec.place(x=100 ,y=200 )
    cansec=tk.Button(admin12,text='>>CANDIDATES SECTION<<',font=('elephant'),
                        justify=CENTER,bg="black",fg="white",command=lambda:[admin12.destroy(),adminex.cand()])
    cansec.place(x=100 ,y=250 )
    ussec=tk.Button(admin12,text='>>USER SECTION<<',font=('elephant'),
                        justify=CENTER,bg="black",fg="white",command=lambda:[admin12.destroy(),adminex.user()])
    ussec.place(x=100 ,y=300 )
    ret=tk.Button(admin12,text='GO BACK',font=('impact','8'),
                justify=CENTER,fg='red',command=lambda:[admin12.destroy(),calad._clad(calad)])
    ret.place(x=550,y=350)
    admin12.mainloop()
            

 
admin = tk.Tk()
admin.geometry("300x300")
admin.title("Login")
admin.resizable(0,0)
admin.minsize(626,417)
adminimg=ImageTk.PhotoImage(file=r'F:\main project\photo\chemistryimage.jpg')
img1=tk.Label(admin,image=adminimg)
img1.place(x=0,y=0)
  
 
# Defining the first row
lblfrstrow = tk.Label(admin, text ="Username -", font=("Monotype Corsiva",'18'),
                justify=CENTER, fg="blue" )
lblfrstrow.place(x = 100, y = 40)
 
Username = tk.Entry(admin, width = 50,font=('Monotype Corsiva','14'))
Username.place(x = 300, y = 40, width = 180)
  
lblsecrow = tk.Label(admin, text ="Password - ",font=("Monotype Corsiva",'18'),
                justify=CENTER, fg="blue")
lblsecrow.place(x = 100, y = 100)
 
password = tk.Entry(admin, width = 50,font=('Monotype Corsiva','14'))
password.place(x = 300, y = 100, width = 180)
 
submitbtn = tk.Button(admin, text ="Login",font='elephant',
                      bg ='blue', command = submitact)
submitbtn.place(x = 300, y = 200, width = 55)
ret=tk.Button(admin,text='GO BACK',font=('impact','8'),
                justify=CENTER,fg='red',command=lambda:[adclose(),clmain()])
ret.place(x=550,y=350)
admin.mainloop()