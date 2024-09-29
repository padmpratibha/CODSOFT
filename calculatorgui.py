from tkinter import *


window = Tk()
window.geometry("312x324")
window.resizable(0,0)
window.title("Calcultor")



def btn_click(item):
    global exp 
    exp = exp + str(item)
    input_text.set(exp)

def btn_clear():
    global exp 
    exp = ""
    input_text.set("")

def btn_equal():
    global exp 
    result = str(eval(exp))
    input_text.set(result)
    exp = ""


exp = " "
input_text = StringVar()

input_frame = Frame(window,width=312,height=50,highlightbackground="black",highlightcolor="black")
input_frame.pack(side=TOP)

input_field = Entry(input_frame,textvariable= input_text,width=50)
input_field.grid(row=0,column=0)
input_field.pack(ipady=10)


btn_frame = Frame(window,width=312,height=272.5,bg="gray")
btn_frame.pack()

# clear = Button(btn_frame,text="c",width=32,height=3,command=btn_clear).place()
# divide = Button(btn_frame,text="/",width=10,height=3)


seven = Button(btn_frame,text="7",width=10,height=3,command=lambda : btn_click(7)).grid(row=1,column=0)
eight = Button(btn_frame,text="8",width=10,height=3,command=lambda : btn_click(8)).grid(row=1,column=1)
nine = Button(btn_frame,text="9",width=10,height=3,command=lambda : btn_click(9)).grid(row=1,column=2)
divide = Button(btn_frame,text="/",width=10,height=3,command=lambda : btn_click("/")).grid(row=1,column=3)

four = Button(btn_frame,text="4",width=10,height=3,command=lambda : btn_click(4)).grid(row=2,column=0)
five = Button(btn_frame,text="5",width=10,height=3,command=lambda : btn_click(5)).grid(row=2,column=1)
six = Button(btn_frame,text="6",width=10,height=3,command=lambda : btn_click(6)).grid(row=2,column=2)
multiply = Button(btn_frame,text="*",width=10,height=3,command=lambda : btn_click("*")).grid(row=2,column=3)

one = Button(btn_frame,text="1",width=10,height=3,command=lambda : btn_click(1)).grid(row=3,column=0)
two = Button(btn_frame,text="2",width=10,height=3,command=lambda : btn_click(2)).grid(row=3,column=1)
three = Button(btn_frame,text="3",width=10,height=3,command=lambda : btn_click(3)).grid(row=3,column=2)
minus = Button(btn_frame,text="-",width=10,heigh=3,command=lambda : btn_click("-")).grid(row=3,column=3)


clear = Button(btn_frame,text="ac",width=10,height=3,command=lambda : btn_clear()).grid(row=4,column=0)
zero = Button(btn_frame,text="0",width=10,height=3,command=lambda : btn_click(0)).grid(row=4,column=1)
point = Button(btn_frame,text=" .",width=10,height=3,command=lambda : btn_click(".")).grid(row=4,column=2)
plus = Button(btn_frame,text="+",width=10,height=3,command=lambda : btn_click("+")).grid(row=4,column=3)


equals = Button(btn_frame,text="=",width=30,height=3,command=lambda : btn_equal()).grid(columnspan=4)

# point = Button(btn_frame,text=" .",width=10,height=3,command=lambda : btn_click(" .")).grid(row=4,column=3)
# equals = Button(btn_frame,text="=",width=10,height=3,command=lambda : btn_click("=")).grid(row=5,column=1)




window.mainloop()


    


    


