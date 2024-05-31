from tkinter import *
import sqlite3
import tkinter as tk
import adminex
conn = sqlite3.connect("database\School.db")
cur = conn.cursor()

l1=[]
newex=tk.Tk()
newex.geometry('1000x800')
newex.title("Welcome User")
newex.config(bg='black')
#newex.resizable(0,0)
def upload():
    col()
    non=tk.Label(newex,text='',font=('Monotype Corsiva','18'),
                    justify=LEFT,fg='yellow',bg='black')
    non.place(x=300,y=50)
    cur=conn.cursor()
    try:
        cur.executemany("INSERT INTO ant VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",l1)
        conn.commit()
        newex.destroy()
        adminex.exam1()
    except:
        non.config(text='INVALID INPUT PLEASE CHECK')
        pass

    #cur.execute("SELECT * FROM a")
    

def col():#collect the data
    non=tk.Label(newex,text='',font=('Monotype Corsiva','18'),
                    justify=LEFT,fg='yellow',bg='black')
    non.place(x=300,y=50)
    tu=()   
    if len(Eqpaper.get())==0:
        non.config(text='Please enter Question Paper Code')
    elif len(Esub.get())==0:
        non.config(text='')
        non.config(text='Please enter Subject                      ')
    elif len(Esdcl.get())==0:
        non.config(text='')
        non.config(text='Please enter Standard or Class               ')
    elif len(Eqn.get())==0:
        non.config(text='')
        non.config(text='Please enter Question no.                     ')
    elif len(Eque.get(1.0, "end-1c"))==0:
        non.config(text='')
        non.config(text='Please enter Question                          ')
    elif len(Eop1.get(1.0, "end-1c"))==0:
        non.config(text='')
        non.config(text='Please enter Option 1                            ')
    elif len(Eop2.get(1.0, "end-1c"))==0:
        non.config(text='')
        non.config(text='Please enter Option 2                             ')
    elif len(Eop3.get(1.0, "end-1c"))==0:
        non.config(text='')
        non.config(text='Please enter Option 3                             ')
    elif len(Eop4.get(1.0, "end-1c"))==0:
        non.config(text='')
        non.config(text='Please enter Option 4                             ')
    elif len(Eans.get())==0:
        non.config(text='')
        non.config(text='Please enter Correct Option no.                   ')
    elif len(Emar.get())==0:
        non.config(text='')
        non.config(text='Please enter Marks                                  ')    
    else:
        non.config(text='                                                                    ')
        tu=tu+(Eqpaper.get(),)
        tu=tu+(Esub.get(),)
        tu=tu+(Esdcl.get(),)
        tu=tu+(Eqn.get(),)
        tu=tu+(Eque.get(1.0, "end-1c"),)
        tu=tu+(Eop1.get(1.0, "end-1c"),)
        tu=tu+(Eop2.get(1.0, "end-1c"),)
        tu=tu+(Eop3.get(1.0, "end-1c"),)
        tu=tu+(Eop4.get(1.0, "end-1c"),)
        tu=tu+(Eans.get(),)
        tu=tu+(Emar.get(),)
        tu=tu+(Enmar.get(),)
        l1.append(tu)
        Eqn.delete(0,END)
        Eque.delete(1.0, "end-1c")
        Eop1.delete(1.0, "end-1c")
        Eop2.delete(1.0, "end-1c")
        Eop3.delete(1.0, "end-1c")
        Eop4.delete(1.0, "end-1c")
        Eans.delete(0,END)
        Emar.delete(0,END)
        Enmar.delete(0,END)
    return (tu)

#creating label

qpaper=tk.Label(newex,text='Question Paper Code :-',font=('cooper black','10'),#question papaer no.
                justify=LEFT,fg='white',bg='black')
qpaper.place(x=0,y=100)


sub=tk.Label(newex,text='Subject :-',font=('cooper black','10'),#subject 
                justify=LEFT,fg='white',bg='black')
sub.place(x=0,y=120)

sdcl=tk.Label(newex,text='Standard or Class :-',font=('cooper black','10'),#standard or class
                justify=LEFT,fg='white',bg='black')
sdcl.place(x=350,y=120)

qn=tk.Label(newex,text='Question No. :-',font=('cooper black','10'),#question no.
                justify=LEFT,fg='white',bg='black')
qn.place(x=0,y=140)

que=tk.Label(newex,text='Question :-',font=('cooper black','10'),#question
                justify=LEFT,fg='white',bg='black')
que.place(x=150,y=160)

op1=tk.Label(newex,text='Option 1 :-',font=('cooper black','10'),#option 1
                justify=LEFT,fg='white',bg='black')
op1.place(x=300,y=250)

op2=tk.Label(newex,text='Option 2 :-',font=('cooper black','10'),#option 2
                justify=LEFT,fg='white',bg='black')
op2.place(x=300,y=300)

op3=tk.Label(newex,text='Option 3 :-',font=('cooper black','10'),#option 3
                justify=LEFT,fg='white',bg='black')
op3.place(x=300,y=350)

op4=tk.Label(newex,text='Option 4 :-',font=('cooper black','10'),#option 4
                justify=LEFT,fg='white',bg='black')
op4.place(x=300,y=400)

ans=tk.Label(newex,text='Correct Option no. :-',font=('cooper black','10'),#answer option no.
                justify=LEFT,fg='white',bg='black')
ans.place(x=150,y=450)

mar=tk.Label(newex,text='Mark :-',font=('cooper black','10'),#marks
                justify=LEFT,fg='white',bg='black')
mar.place(x=400,y=450)

nmar=tk.Label(newex,text='Negative Mark :-',font=('cooper black','10'),#negative marks
                justify=LEFT,fg='white',bg='black')
nmar.place(x=600,y=450)


#creating entry
Eqpaper=tk.Entry(newex,text='Code', #question papaer no.
                 fg='black',bg='white')
Eqpaper.place(x=150,y=100)

Esub=tk.Entry(newex,text='Subj', #subject 
                 fg='black',bg='white')
Esub.place(x=150,y=120)

Esdcl=tk.Entry(newex,text='Standard', #standard or class
                 fg='black',bg='white')
Esdcl.place(x=550,y=120)

Eqn=tk.Entry(newex,text='No.', #question no.
                fg='black',bg='white')
Eqn.place(x=150,y=140)

Eque=tk.Text(newex,width=80 #question
                ,height=5,fg='black',bg='white')
Eque.place(x=300,y=160)

Eop1=tk.Text(newex,width=50, #option 1
                height=2,fg='black',bg='white')
Eop1.place(x=400,y=250)

Eop2=tk.Text(newex,width=50, #option 2
                height=2,fg='black',bg='white')
Eop2.place(x=400,y=300)

Eop3=tk.Text(newex,width=50, #option 3
                height=2,fg='black',bg='white')
Eop3.place(x=400,y=350)

Eop4=tk.Text(newex,width=50, #option 4
                height=2,fg='black',bg='white')
Eop4.place(x=400,y=400)

Eans=tk.Entry(newex,text='ans', #answer option no.
                fg='black',bg='white')
Eans.place(x=300,y=450,width=20)  

Emar=tk.Entry(newex,text='mark', #marks
                fg='black',bg='white')
Emar.place(x=500,y=450,width=20)

Enmar=tk.Entry(newex,text='negative mark', #negative marks
                fg='black',bg='white')
Enmar.place(x=700,y=450,width=20)


nxt=tk.Button(newex,text='NEXT',font=('elephant','16'),
                justify=CENTER,fg='red',bg='black',command=col)
nxt.place(x=600,y=550,width=100)

uploadbt=tk.Button(newex,text='>>UPLOAD QUESTION PAPER<<',font=('elephant','18'),
                justify=CENTER,fg='AQUA',bg='black',command=upload)
uploadbt.place(x=400,y=650,width=400)

newex.mainloop()
