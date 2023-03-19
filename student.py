from tkinter import *
from PIL import ImageTk
import time
import pymysql
import ttkthemes
from tkinter import ttk,messagebox

def exit_page():
    result=messagebox.askyesno('confirm','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass


def show_student():
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    student_table.delete(*student_table.get_children())
    for data in fetched_data:
        student_table.insert('', END, values=data)


def delete_student():
    indexing=student_table.focus()
    print(indexing)
    content=student_table.item(indexing)
    content_id=content['values'][0]
    query='delete from student where id=%s'
    mycursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo('Deleted',f'ID {content_id} is deleted successfully')

    query= 'select * from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    student_table.delete(*student_table.get_children())
    for data in fetched_data:
        student_table.insert('',END,values=data)



def add_student():
    def add_data():
        if idEntry.get() == '' or nameEntry.get() == '' or phoneEntry.get()=='' or languageEntry.get() == '' or AgeEntry.get() == '':
            messagebox.showerror('Error','All fields are required',parent=addWindow)

        else:
            query = 'insert into student values(%s,%s,%s,%s,%s)'
            mycursor.execute(query,(idEntry.get(),nameEntry.get(),phoneEntry.get(),languageEntry.get(),AgeEntry.get()))
            con.commit()
            result=messagebox.askyesno('Confirmation','Data added successfully. Do you want to clean the form?',
                                       parent=addWindow)
            if result:
                idEntry.delete(0,END)
                nameEntry.delete(0,END)
                phoneEntry.delete(0, END)
                languageEntry.delete(0, END)
                AgeEntry.delete(0, END)
            else:
                pass

            query='select *from student'
            mycursor.execute(query)
            fetched_data=mycursor.fetchall()
            student_table.delete(*student_table.get_children())
            for data in fetched_data:
                datalist=list(data)
                student_table.insert('',END,values=datalist)



    addWindow=Toplevel()
    addWindow.grab_set()
    addWindow.resizable(False,False)
    idLabel=Label(addWindow,text='ID',font=('times new roman',20,'bold'))
    idLabel.grid(row=0,column=0,padx=25,pady=30)
    idEntry=Entry(addWindow,font=('times new roman',20,'bold'))
    idEntry.grid(row=0,column=1,padx=25,pady=30)


    nameLabel = Label(addWindow, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=25, pady=30)
    nameEntry = Entry(addWindow, font=('times new roman', 20, 'bold'))
    nameEntry.grid(row=1, column=1, padx=25, pady=30)

    phoneLabel = Label(addWindow, text='Phone', font=('times new roman', 20, 'bold'))
    phoneLabel.grid(row=2, column=0, padx=25, pady=30)
    phoneEntry = Entry(addWindow, font=('times new roman', 20, 'bold'))
    phoneEntry.grid(row=2, column=1, padx=25, pady=30)

    languageLabel = Label(addWindow, text='Language', font=('times new roman', 20, 'bold'))
    languageLabel.grid(row=3, column=0, padx=25, pady=30)
    languageEntry = Entry(addWindow, font=('times new roman', 20, 'bold'))
    languageEntry.grid(row=3, column=1, padx=25, pady=30)

    AgeLabel = Label(addWindow, text='Age', font=('times new roman', 20, 'bold'))
    AgeLabel.grid(row=4, column=0, padx=25, pady=30)
    AgeEntry = Entry(addWindow, font=('times new roman', 20, 'bold'))
    AgeEntry.grid(row=4, column=1, padx=25, pady=30)

    addButton=Button(addWindow,text='Add',font=('Arial', 14, 'bold'), bg='red',fg='white',command=add_data)
    addButton.grid(row=7,columnspan=2, padx=25, pady=30)







def connect_database():
    def connect():
        global mycursor,con
        try:
            #con=pymysql.connect(host=hostnameEntry.get(), user=usernameEntry.get())
            con = pymysql.connect(host='localhost', user='root')
            mycursor=con.cursor()

        except:
            messagebox.showerror('Error','Invalid Details',parent=connectWindow)
            return
        try:
            query='create database studentmanagementsystem'
            mycursor.execute(query)
            query='use studentmanagementsystem'
            mycursor.execute(query)
            query='create table student(id int not null primary key, name varchar(50),mobile varchar(10),' \
              'language varchar(20),age varchar(10))'
            mycursor.execute(query)
        except:
            query='use studentmanagementsystem'
            mycursor.execute(query)
        messagebox.showinfo('Success', 'Database connection is successful', parent=connectWindow)
        connectWindow.destroy()
        add_studentButton.config(state=NORMAL)
        update_studentButton.config(state=NORMAL)
        show_studentButton.config(state=NORMAL)
        delete_studentButton.config(state=NORMAL)


    connectWindow=Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x270+730+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0, 0)

    hostnameLabel=Label(connectWindow,text='  Host Name',font=('Arial',14,'bold'))
    hostnameLabel.grid(row=0,column=0, padx=30)
    hostnameEntry=Entry(connectWindow,font=('roman',14,'bold'),bd=2)
    hostnameEntry.grid(row=0,column=1,padx=30,pady=30)

    usernameLabel = Label(connectWindow, text='  User Name', font=('Arial', 14, 'bold'))
    usernameLabel.grid(row=1, column=0, padx=30)
    usernameEntry = Entry(connectWindow, font=('roman', 14, 'bold'), bd=2)
    usernameEntry.grid(row=1, column=1, padx=30, pady=30)

    '''passwordLabel = Label(connectWindow, text='  Password', font=('Arial', 14, 'bold'))
    passwordLabel.grid(row=2, column=0, padx=30)
    passwordEntry = Entry(connectWindow, font=('roman', 14, 'bold'), bd=2)
    passwordEntry.grid(row=2, column=1, padx=30, pady=28)'''

    connectButton=Button(connectWindow,text='Connect', font=('Arial', 14, 'bold'), bg='red',fg='white',command=connect)
    connectButton.grid(row=3, column=1,pady=30)



count = 0
text = ''


def slider():
    global text, count
    if count == len(s):
        count = 0
        text = ''
    text = text+s[count]
    headingLabel.config(text=text)
    count += 1
    headingLabel.after(350, slider)


def clock():
    date = time.strftime('%d/%m/%Y')
    currenttime = time.strftime('%H:%H:%S')
    datetimeLabel.config(text=f'    Date: {date}\nTime: {currenttime}')
    datetimeLabel.after(1000, clock)

def size_2():
   text.config(font=('Helvetica bold',60,'bold'))



root = Tk()

'''root.get_themes()

root.set_theme('elegance')'''

root.geometry('1525x782+0+0')
root.resizable(0, 0)
root.title('Student Management System')

backgroundImage = ImageTk.PhotoImage(file='wall.jpg')

bgLabel = Label(root, image=backgroundImage)
bgLabel.place(x=0, y=-100)
datetimeLabel = Label(root, text='hello', font=('times new roman', 18, 'bold'),bg= 'Dark Green',fg='white')
datetimeLabel.place(x=5, y=5)
clock()


s = 'Daisy Language Classes'
headingLabel = Label(root, text=s, font=('bookman old style', 40, 'bold'),bg='light green', width=30)
headingLabel.place(x=230, y=0)
slider()

connectButton=Button(root,text='Connect to Database', font=('times new roman', 15, 'bold'), bg= 'Dark Green',fg='white',
                    cursor='hand2',command= connect_database)

connectButton.place(x=1300, y=5)

leftFrame=Frame(root)
leftFrame.place(x=60, y=80, width = 300, height=650)

icon_image = PhotoImage(file='classes.png')
icon_Label = Label(leftFrame, image=icon_image)
icon_Label.grid(row=0, column=0)

add_studentButton = Button(leftFrame,text='Add Student',font=('times new roman', 17, 'bold'),width=20, bg= 'violet',
                         fg='white', cursor='hand2',command=add_student)
add_studentButton.grid(row=1, column =0, pady=17)

update_studentButton = Button(leftFrame,text='Update Student',font=('times new roman', 17, 'bold'),width=20,
                             bg= 'violet', fg='white', cursor='hand2')
update_studentButton.grid(row=2,column =0, pady=17)

delete_studentButton = Button(leftFrame,text='Delete Student',font=('times new roman', 17, 'bold'),width=20,
                              bg='violet', fg='white', cursor='hand2',command= delete_student)
delete_studentButton.grid(row=3,column =0, pady=17)

show_studentButton = Button(leftFrame,text='Show Student',font=('times new roman', 17, 'bold'),width=20,
                              bg='violet', fg='white', cursor='hand2',command=show_student)
show_studentButton.grid(row=4,column =0, pady=17)

exit_Button = Button(leftFrame,text='Exit',font=('times new roman', 17, 'bold'),width=20,
                              bg='violet', fg='white', cursor='hand2',command=exit_page)
exit_Button.grid(row=5, column=0, pady=17)

rightFrame = Frame(root)
rightFrame.place(x=450, y=80, width=1050, height=650)

student_table = ttk.Treeview(rightFrame, columns=('ID', 'Name', 'Phone', 'Language','Age'))
student_table.pack(fill=BOTH, expand=1)

student_table.heading('ID', text='ID',command=size_2)


student_table.heading('Name', text='Name',command=size_2)

student_table.heading('Phone', text='Phone',command=size_2)

student_table.heading('Language', text='Language',command=size_2)

student_table.heading('Age', text='Age',command=size_2)

student_table.config(show='headings')







root.mainloop()