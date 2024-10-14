from tkinter import *
from tkinter import messagebox
import string

root = Tk()
root.geometry("700x500")
root.title("contact book")
root.resizable(0,0)
root.config(bg= '#9370DB')

contactlist = [
    ['bhavna pradhan', 9213456789,'bhavana@gmail.com','ram nagar pune'],
    ['kavya pradhan', 9213456799,'kavya@gmail.com','ram nagar  pune'],
    ['bhushan pradhan', 9213456779,'bhushan@gmail.com','ram nagar pune'],
    ['sidharth gehlot', 9213452289,'sidharth@gmail.com','ram nagar pune'],
    ['nimesh gandhi', 9212256789,'nimesh@gmail.com','ram nagar pune'],
    ['madhura singh', 9213356789,'madhura@gmail.com','ram nagarpune'],
    ['bhuvan dhan', 9213455589,'bhuvan@gmail.com','ram nagar, pune']
]

Name = StringVar()
Number = StringVar()
Mail = StringVar()
Adress = StringVar()

frame = Frame(root)
frame.pack(side=RIGHT)

scroll = Scrollbar(frame,orient=VERTICAL)
select = Listbox(frame,yscrollcommand=scroll.set,font=('Times New Roman', 16),bg='#FFA500',width=20,height=20,borderwidth=2,relief="groove")
scroll.config(command=select.yview)
scroll.pack(side=RIGHT,fill=Y)
select.pack(side=LEFT,fill=BOTH,expand=1)

def selected():
    print("hello",len(select.curselection()))
    if len(select.curselection())==0:
        messagebox.showerror("Error", "Please Select the Name")
    else:
        return int(select.curselection()[0])
                
    
def AddContact():
    if Name.get()!="" and Number.get()!= "" :
        contactlist.append([Name.get(),Number.get(),Mail.get(),Adress.get()])
        print(contactlist)
        selected_set()
        Resetcontact()
        messagebox.showinfo("confirmantion","contact added successfully..")
    else:
        messagebox.showerror("error","plese fill the information..")


def EditContact():    
    if Name.get() and Number.get() :
        contactlist[selected()]= [Name.get(),Number.get(),Mail.get(),Adress.get()]
        messagebox.showinfo("confirmation","contact updated successfully..")
        Resetcontact()
        selected_set()
        # ResetContact()
    elif not(Name.get()) and not(Number.get()) and not(len(select.curselection())==0):
        messagebox.showerror("error","please fill the information..")
    else:
        if len(select.curselection())==0:
            messagebox.showerror("error","please select name and \n press load button")
        else:
            message1 = """To load all inforamation of \n 
            selected row press load button\n"""

            messagebox.showerror("error",message1)


def Resetcontact():
    Name.set('')
    Number.set('')
    Mail.set('')
    Adress.set('')


def DeleteContact():
    if len(select.curselection())!= 0 :
        result = messagebox.askyesno("confirmation",'you want to delete contact \n which you selected')
        if result == True:
            del contactlist[selected()]
            selected_set()
        else:
            messagebox.showerror("error","please select contact...")

def ViewContact():
    NAME, PHONNO, MAIL, ADRESS = contactlist[selected()]
    Name.set(NAME)
    Number.set(PHONNO)
    Mail.set(MAIL)
    Adress.set(ADRESS)

def Exit():
    root.destroy()

def selected_set():
    contactlist.sort()
    select.delete(0,END)
    for name,phone,mailid,city in contactlist:
        select.insert(END,name)

selected_set()

Label(root,text="Name").place(x=30,y=80)
Entry(root,textvariable=Name,width=30).place(x=200,y=80)

Label(root,text="Contact Number").place(x=30,y=130)
Entry(root,textvariable=Number,width=30).place(x=200,y=130)

Label(root,text="Email Id").place(x=30,y=180)
Entry(root,textvariable=Mail,width=30).place(x=200,y=180)

Label(root,text="Address").place(x=30,y=230)
Entry(root,textvariable=Adress,width=30).place(x=200,y=230)


Button(root,text="Add",height=1,width=10,command=AddContact).place(x=100,y=320)
Button(root,text="Edit",height=1,width=10,command=EditContact).place(x=200,y=320)
Button(root,text="Delete",height=1,width=10,command=DeleteContact).place(x=300,y=320)

Button(root,text="View",height=1,width=10,command=ViewContact).place(x=100,y=370)
Button(root,text="Reset",height=1,width=10,command=Resetcontact).place(x=200,y=370)
Button(root,text="Exit",height=1,width=10,command=Exit).place(x=300,y=370)


root.mainloop()