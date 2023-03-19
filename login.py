from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

def login():

    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'Fields cannot be empty')
    elif usernameEntry.get() == 'Admin' and passwordEntry.get() == '12345':
        messagebox.showinfo('Success', 'Welcome')
        window.destroy()
        import student

    else:
        messagebox.showerror('Error','Please enter correct credentials')

window = Tk()

window.geometry('1525x782+0+0')
window.title('Login System of Daisy Language Classes')

window.resizable(False, False)
backgroundImage = ImageTk.PhotoImage(file='bg.jpg')

bgLabel = Label(window, image=backgroundImage)
bgLabel.place(x=0, y=-100)

loginFrame = Frame(window)
loginFrame.place(x=475, y=360)

logoImage = PhotoImage(file='admin.png')
logoLabel = Label(loginFrame, image=logoImage)
logoLabel.grid(row=0, column=0, columnspan=2, pady=5)

usernameImage = PhotoImage(file='user.png')
usernameLabel = Label(loginFrame, image=usernameImage, text='  Username ', compound=LEFT
                     , font=('times new roman', 25, 'bold'),bg= 'light grey')

usernameLabel.grid(row=1, column=0, pady=10, padx= 10)

usernameEntry = Entry(loginFrame, font=('times new roman', 25, 'bold'),bd=5, fg='dark green')
usernameEntry.grid(row=1, column=1, pady=10, padx= 10)

passwordImage = PhotoImage(file='lock.png')
passwordLabel = Label(loginFrame, image=passwordImage, text='  Password  ', compound=LEFT
                     , font=('times new roman', 25, 'bold'), bg= 'light grey')
passwordLabel.grid(row=7, column=0, pady=10, padx= 10)
passwordEntry = Entry(loginFrame, font=('times new roman', 25, 'bold'),bd=5, fg='dark green')
passwordEntry.grid(row=7, column=1, pady=10, padx= 10)

loginButton=Button(loginFrame,text='Login', font=('times new roman', 15, 'bold'), bg= 'Red',fg='white',width=10,
                   cursor='hand2', command=login)
loginButton.grid(row=9,column=1, pady=10, padx= 10)









window.mainloop()

