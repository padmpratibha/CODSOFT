#using tkinker
from tkinter import *
import tkinter.messagebox

def entertask():
    input_text = ""
    def add():
        input_text = entry_task.get(1.0,"end-1c")
        if input_text =="":
            tkinter.messagebox.showwarning(title="Warning !",message="Please enter some text")
        else:
            listbox_task.insert(END,input_text)

            root1.destroy()

    root1=Tk()
    root1.title("add task..")
    entry_task = Text(root1,width= 40,height= 4)
    entry_task.pack()
    button_temp = Button(root1,text="add tsk",command=add)
    button_temp.pack()
    root1.mainloop()


def deletetask():
    selected = listbox_task.curselection()
    listbox_task.delete(selected[0])

def markcompleted():
    marked = listbox_task.curselection()
    temp = marked[0]
    temp_marked= listbox_task.get(marked)
    temp_marked =temp_marked+" ✔"
    listbox_task.delete(temp)
    listbox_task.insert(temp,temp_marked)
        


window = Tk()   #top widget
window.title("TODO APP") #title to wediget
# window.mainloop()

frame_task = Frame(window)
frame_task.pack()

listbox_task = Listbox(frame_task,bg="black",fg="white",height=15,width=50,font="Helvetica")
listbox_task.pack(side=tkinter.LEFT)

Scrollbar_task = Scrollbar(frame_task)
Scrollbar_task.pack(side=tkinter.RIGHT,fill=tkinter.Y)
listbox_task.config(yscrollcommand=Scrollbar_task.set)
Scrollbar_task.config(command=listbox_task.yview)


entry_button = Button(window,text="add task",width=50,command=entertask)
entry_button.pack(pady=3)

delete_button = Button(window,text="delete task",width=50,command=deletetask)
delete_button.pack(pady=3)

mark_button = Button(window,text="mark task",width=50,command=markcompleted)
mark_button.pack(pady=3)

window.mainloop()# main event loop  run and display everything written





