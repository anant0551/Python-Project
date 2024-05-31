from tkinter import *
from PIL import Image, ImageTk

def adwindow():
    import admin

main_window=Tk()
main_window.title('ONLINE EXAMINATION SYSTEM🖥️📲')
main_window.geometry('700x467')
main_window.config(bg='black')
main_window.maxsize(700,467)
main_window.resizable(0,0)

def close():
    main_window.destroy()


render=ImageTk.PhotoImage(file=r'F:\main project\photo\image1d.jpg')
img=Label(main_window,image=render)
 
img.place(x=0,y=0)

i1=PhotoImage(file= r'F:\main project\photo\admin.png')
b1=Button(main_window,text='administrator login',background='BLACK',image=i1,command=lambda:[close(),adwindow()])
b1.place(x=20,y=350)


i2=PhotoImage(file= r'F:\main project\photo\student1.png') 
b2=Button(main_window,text='CANDIDATE login',background='BLACK',image=i2)
b2.place(x=580,y=350)

main_window.mainloop()
