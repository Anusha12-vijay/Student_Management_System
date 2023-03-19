from tkinter import *
from PIL import ImageTk

def login1():
    anu.destroy()
    import login

anu=Tk()

anu.geometry('1525x782+0+0')
anu.title('Admin page of Daisy Language Classes')

anu.resizable(False, False)
backgroundImage = ImageTk.PhotoImage(file='space.jpg')

bgLabel = Label(anu, image=backgroundImage)
bgLabel.place(x=0, y=0)

s = 'Daisy Language Classes'
headingLabel1 = Label(anu, text=s, font=('bookman old style', 50, 'italic bold'),bg='white',fg='navy blue',width=30)
headingLabel1.place(x=50, y=0)

s1 = 'Welcome Admin !'
headingLabel2 = Label(anu, text=s1, font=('arial', 30, ' bold'),bg='white')
headingLabel2.place(x=25, y=250)

adminButton=Button(anu,text='To Login Page', font=('times new roman', 15, 'bold'), bg= 'Red',fg='white',width=25,
                   cursor='hand2', command=login1)
adminButton.place(x=35,y=500)







anu.mainloop()