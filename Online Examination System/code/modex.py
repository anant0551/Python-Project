from optparse import Values
import sqlite3
from tkinter import *  
from tkinter import ttk
modex=Tk()  
#App Title  
modex.title("EXAM MODIFICATION ")
modex.geometry('1920x1080')  
 
#add some style
style=ttk.Style()
#Pick a theme
style.theme_use('default')
#configure the treeview colors
style.configure("treeview",
        background="#D3D3D3",
        foreground="black",
        rowheight=50,
        fieldbckground="#D3D3D3")
# Change selected Color
style.map("Treeview",
    background=[('selected',"#347083")])
#create a treeview frame
tree_frame=Frame(modex)
tree_frame.pack(pady=10,expand=1)

#create a treeview scrollbar 
tree_scroll=Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT,fill=Y)

# create the treeview
my_tree=ttk.Treeview(tree_frame,yscrollcommand=tree_scroll.set,selectmode="extended",)
my_tree.pack(anchor=W,fill=Y)


# configure the scrollbar
tree_scroll.configure(command=my_tree.yview)

#define our columns
my_tree['column']=("Question Paper Code","Subject","Standard","Question no.","Question","Option 1","Option 2","Option 3","Option 4","Correct Option","Mark","Negative Mark")

# Format our columns
my_tree.column("#0",width=0,stretch=NO)
my_tree.column("Question Paper Code",anchor=W,width=140)
my_tree.column("Subject",anchor=W,width=100)
my_tree.column("Standard",anchor=W,width=100)
my_tree.column("Question no.",anchor=W,width=50)
my_tree.column("Question",anchor=W,width=200)
my_tree.column("Option 1",anchor=W,width=140)
my_tree.column("Option 2",anchor=W,width=140)
my_tree.column("Option 3",anchor=W,width=140)
my_tree.column("Option 4",anchor=W,width=140)
my_tree.column("Correct Option",anchor=CENTER,width=40)
my_tree.column("Mark",anchor=CENTER,width=40)
my_tree.column("Negative Mark",anchor=CENTER,width=40)
# craete heading
my_tree.heading("#0",text="",anchor=W)
my_tree.heading("Question Paper Code",text="Question Paper Code",anchor=W)
my_tree.heading("Subject",text="Subject",anchor=W)
my_tree.heading("Standard" ,text="Standard",anchor=W)
my_tree.heading("Question no." ,text="Question no.",anchor=W)
my_tree.heading("Question",text="Question",anchor=W)
my_tree.heading("Option 1",text="Option 1",anchor=CENTER)
my_tree.heading("Option 2",text="Option 2",anchor=CENTER)
my_tree.heading("Option 3",text="Option 3",anchor=CENTER)
my_tree.heading("Option 4",text="Option 4",anchor=CENTER)
my_tree.heading("Correct Option",text="Correct Option",anchor=CENTER)
my_tree.heading("Mark",text="Mark",anchor=CENTER)
my_tree.heading("Negative Mark",text="Negative Mark",anchor=CENTER)

#create the table
non=ttk.Label(modex,text='',font=('Monotype Corsiva','18'),
                justify=LEFT)
non.place(x=500,y=0)
conn = sqlite3.connect("database\School.db")
cur = conn.cursor()

try:
    cur.execute("""CREATE TABLE if not exists ant (
        Qpaperno VARCHAR (10)  NOT NULL,
        Subj     VARCHAR (40)  NOT NULL,
        Standard VARCHAR (40)  NOT NULL,
        Quesno   VARCHAR (4)   NOT NULL,
        Ques     VARCHAR (200) NOT NULL,
        Option1  VARCHAR (100) NOT NULL,
        Option2  VARCHAR (100) NOT NULL,
        Option3  VARCHAR (100) NOT NULL,
        Option4  VARCHAR (100) NOT NULL,
        Ansop    INTEGER (2)   NOT NULL,
        Mark     INTEGER (5)   NOT NULL,
        Negmark  INTEGER (3))
        """)
   
    
except:
    non.config(text='Something went wrong ')
    pass

# Add data
def query_database():
    non=ttk.Label(modex,text='',font=('Monotype Corsiva','18'),
                    justify=LEFT)
    non.place(x=300,y=50)
    conn = sqlite3.connect("database\School.db")
    cur = conn.cursor()
    
    try:
        cur.execute("SELECT * FROM ant ")
        list1=cur.fetchall()
        
    except:
        non.config(text='INVALID INPUT PLEASE CHECK')
        pass
    # add our data to the screen
    global count
    count=0
    for record in list1:
        if count % 2 == 1:
            my_tree.insert(parent="",index='end',iid=count,text='', values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11]),tags=('oddrow',))
        else:
            my_tree.insert(parent="",index='end',iid=count ,text='', values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6],record[7],record[8],record[9],record[10],record[11]),tags=('evenrow',))
        #increment counter
        count+=1

# Create striped row tags
my_tree.tag_configure('oddrow',background="white")
my_tree.tag_configure('evenrow',background="lightblue")



# Add record entry boxes
data_frame=LabelFrame(modex,text="Record")
data_frame.pack(fill="x",expand="yes",padx=20)

qp_label=Label(data_frame,text='Question Paper Code ')
qp_label.grid(row=0,column=0,padx=10,pady=10)
qp_entry=Entry(data_frame)
qp_entry.grid(row=0,column=1,padx=10,pady=10)
sub_label=Label(data_frame,text='Subject ',justify=RIGHT)
sub_label.grid(row=0,column=2,padx=10,pady=10)
sub_entry=Entry(data_frame)
sub_entry.grid(row=0,column=3,pady=10)
st_label=Label(data_frame,text='Standard')
st_label.grid(row=0,column=4,padx=10,pady=10)
st_entry=Entry(data_frame)
st_entry.grid(row=0,column=5,padx=10,pady=10)
qpn_label=Label(data_frame,text='Question No. ')
qpn_label.grid(row=1,column=0,padx=10,pady=10)
qpn_entry=Entry(data_frame)
qpn_entry.grid(row=1,column=1,padx=10,pady=10)
q_label=Label(data_frame,text='Question ')
q_label.grid(row=2,column=1,padx=10,pady=10)
q_entry=Text(data_frame, width=80,height=5)
q_entry.grid(row=2,column=2)
op1_label=Label(data_frame,text='Option 1 ')
op1_label.grid(row=3,column=1,padx=10,pady=10)
op1_entry=Text(data_frame, width=50,height=3)
op1_entry.grid(row=3,column=2)
op2_label=Label(data_frame,text='OPtion 2 ')
op2_label.grid(row=4,column=1,padx=10,pady=10)
op2_entry=Text(data_frame, width=50,height=3)
op2_entry.grid(row=4,column=2)
op3_label=Label(data_frame,text='Option 3 ')
op3_label.grid(row=5,column=1,padx=10,pady=10)
op3_entry=Text(data_frame, width=50,height=3)
op3_entry.grid(row=5,column=2)
op4_label=Label(data_frame,text='Option 4 ')
op4_label.grid(row=6,column=1,padx=10,pady=10)
op4_entry=Text(data_frame, width=50,height=3)
op4_entry.grid(row=6,column=2)
ans_label=Label(data_frame,text='Correct Option no. ')
ans_label.grid(row=7,column=0,padx=10,pady=10)
ans_entry=Entry(data_frame)
ans_entry.grid(row=7,column=1,padx=10,pady=10)
m_label=Label(data_frame,text='Mark',justify=RIGHT)
m_label.grid(row=8,column=0,padx=10,pady=10)
m_entry=Entry(data_frame)
m_entry.grid(row=8,column=1,pady=10)
nm_label=Label(data_frame,text='Negative Mark ')
nm_label.grid(row=8,column=3,padx=10,pady=10)
nm_entry=Entry(data_frame)
nm_entry.grid(row=8,column=4,padx=10,pady=10)

# Select record


# remove one data  
def remove_one():
    x=my_tree.selection()[0]
    my_tree.delete(x)    

# REmove many recoed
def remove_many():
    x=my_tree.selection()
    for record in x:
        my_tree.delete(record)
#Remove all remove data
def remove_all():
    for record in my_tree.get_children():
        my_tree.delete(record)
# Update record
def update_record():
    if len(qp_entry.get())==0:
        non.config(text='Please enter Question Paper Code')
    elif len(sub_entry.get())==0:
        non.config(text='')
        non.config(text='Please enter Subject                      ')
    elif len(st_entry.get())==0:
        non.config(text='')
        non.config(text='Please enter Standard or Class               ')
    elif len(qpn_entry.get())==0:
        non.config(text='')
        non.config(text='Please enter Question no.                     ')
    elif len(q_entry.get(1.0, "end-1c"))==0:
        non.config(text='')
        non.config(text='Please enter Question                          ')
    elif len(op1_entry.get(1.0, "end-1c"))==0:
        non.config(text='')
        non.config(text='Please enter Option 1                            ')
    elif len(op2_entry.get(1.0, "end-1c"))==0:
        non.config(text='')
        non.config(text='Please enter Option 2                             ')
    elif len(op3_entry.get(1.0, "end-1c"))==0:
        non.config(text='')
        non.config(text='Please enter Option 3                             ')
    elif len(op4_entry.get(1.0, "end-1c"))==0:
        non.config(text='')
        non.config(text='Please enter Option 4                             ')
    elif len(ans_entry.get())==0:
        non.config(text='')
        non.config(text='Please enter Correct Option no.                   ')
    elif len(m_entry.get())==0:
        non.config(text='')
        non.config(text='Please enter Marks                                  ')    
    else:
        non.config(text='                                                                    ')
    selected=my_tree.focus()
    #update record 
    my_tree.item(selected,text="", values=(qp_entry.get(),sub_entry.get(),st_entry.get(),qpn_entry.get(),q_entry.get(1.0, "end-1c"), op1_entry.get(1.0, "end-1c"),op2_entry.get(1.0, "end-1c"),op3_entry.get(1.0, "end-1c"),op4_entry.get(1.0, "end-1c"),ans_entry.get(),m_entry.get(),nm_entry.get(),))
    m=qp_entry.get()
    n=sub_entry.get()
    o=st_entry.get()
    p=qpn_entry.get()
    qe=q_entry.get(1.0, "end-1c")
    r=op1_entry.get(1.0, "end-1c")
    s=op2_entry.get(1.0, "end-1c")
    t=op3_entry.get(1.0, "end-1c")
    u=op4_entry.get(1.0, "end-1c")
    v=ans_entry.get()
    w=m_entry.get()
    x=nm_entry.get()   
    
    #Grab record number
    #selected=my_tree.focus()
    #Grab record  record
    values = my_tree.item(selected,'values')
    
   
    """a=values[0]
    b=values[1]
    c=values[2]
    d=values[3]"""
   
    
    conn = sqlite3.connect("database\School.db")
    cur = conn.cursor()
    '''sqlstr=""" UPDATE ant SET
        Ques = :q,
        Option1 = :op1,
        Option2  = :op2,
        Option3  = :op3,
        Option4 = :op4,
        Ansop = :ans,
        Mark = :ma,
        Negmark = :nm

        WHERE  Qpaperno = ""+m+"" and Subj=""+n+"" and Stabndard=""+o+"" and Quesno=""+p+""  """'''
    cur.execute(""" UPDATE ant SET
        Ques = :qe,
        Option1 = :op1,
        Option2  = :op2,
        Option3  = :op3,
        Option4 = :op4,
        Ansop = :ans,
        Mark = :ma,
        Negmark = :nm

        WHERE  Qpaperno = "'m'" and Subj="'n'" and Standard="'o'" and Quesno="'p'"  """,
            {
                'q':q,
                'op1':r,
                'op2':s,
                'op3':t,
                'op4':u,
                'ans':v,
                'ma':w,
                'nm':x,
             })
    conn.commit()
    conn.close()
    
    
    
    qp_entry.delete(0,END)
    sub_entry.delete(0,END)
    st_entry.delete(0,END)
    qpn_entry.delete(0,END)
    q_entry.delete(1.0, "end-1c")
    op1_entry.delete(1.0, "end-1c")
    op2_entry.delete(1.0, "end-1c")
    op3_entry.delete(1.0, "end-1c")
    op4_entry.delete(1.0, "end-1c")
    ans_entry.delete(0,END)
    m_entry.delete(0,END)
    nm_entry.delete(0,END)

def select_record(e):
    #Clear entry boxes
    qp_entry.delete(0,END)
    sub_entry.delete(0,END)
    st_entry.delete(0,END)
    qpn_entry.delete(0,END)
    q_entry.delete(1.0, "end-1c")
    op1_entry.delete(1.0, "end-1c")
    op2_entry.delete(1.0, "end-1c")
    op3_entry.delete(1.0, "end-1c")
    op4_entry.delete(1.0, "end-1c")
    ans_entry.delete(0,END)
    m_entry.delete(0,END)
    nm_entry.delete(0,END)
    #Grab record number
    selected=my_tree.focus()
    #Grab record  record
    values = my_tree.item(selected,'values')
    #Output to entry boxes
    qp_entry.insert(0,  values[0])
    sub_entry.insert(0,  values[1])
    st_entry.insert(0,  values[2])
    qpn_entry.insert(0,  values[3])
    q_entry.insert(END,  values[4])
    op1_entry.insert(END,  values[5])
    op2_entry.insert(END,  values[6])
    op3_entry.insert(END,  values[7])
    op4_entry.insert(END,  values[8])
    ans_entry.insert(0,  values[9])
    m_entry.insert(0,  values[10])
    nm_entry.insert(0, values[11])

# Clear entry boxes
def clear_entries():
# Clear entry boxes
    qp_entry.delete(0,END)
    sub_entry.delete(0,END)
    st_entry.delete(0,END)
    qpn_entry.delete(0,END)
    q_entry.delete(1.0, "end-1c")
    op1_entry.delete(1.0, "end-1c")
    op2_entry.delete(1.0, "end-1c")
    op3_entry.delete(1.0, "end-1c")
    op4_entry.delete(1.0, "end-1c")
    ans_entry.delete(0,END)
    m_entry.delete(0,END)
    nm_entry.delete(0,END)
	
# Add buttons 
button_frame = LabelFrame(modex, text="Commands")
button_frame.pack(fill="x", expand="yes", padx=20)

update_button = Button(button_frame, text="Update Record", command=update_record)
update_button.grid(row=0, column=0, padx=10, pady=10)

add_button = Button(button_frame, text="Add Record")
add_button.grid(row=0, column=1, padx=10, pady=10)

remove_all_button = Button(button_frame, text="Remove All Records", command=remove_all)
remove_all_button.grid(row=0, column=2, padx=10, pady=10)

remove_one_button = Button(button_frame, text="Remove One Selected", command=remove_one)
remove_one_button.grid(row=0, column=3, padx=10, pady=10)

remove_many_button = Button(button_frame, text="Remove Many Selected", command=remove_many)
remove_many_button.grid(row=0, column=4, padx=10, pady=10)

select_record_button = Button(button_frame, text="Clear Entry Boxes", command=clear_entries)
select_record_button.grid(row=0, column=7, padx=10, pady=10)

#bind the treeview
my_tree.bind("<ButtonRelease-1>",select_record) 
#run to database
query_database()
modex.mainloop()