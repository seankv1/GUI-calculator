import tkinter as tk #tkinter is a binding tool kit
from tkinter import * #tkinter is a binding tool kit

app = tk.Tk() #changing name of tkinter to app for easier use

#I have change the size of the calculator window
app.geometry("570x630")
app.title("python-calculator")
app.maxsize(570,630)
app.minsize(570,630)
ent = Entry(app, width=16, borderwidth=3, relief=RIDGE)
ent.grid(pady=10,row=0,sticky="w",padx=15)
#the abouve lines 6-11 are the specs of the calculator: (how big, title, ect)



def delete():
    a = ent.get()
    ent.delete(first=len(a) - 1, last="end")
def fresult():
    if ent.get() == "":
        pass
    elif ent.get()[0] == "0":
        ent.delete(0, "end")
    else:
        c_res = ent.get()
        c_res = eval(c_res)
        clearf()
        ent.insert("end", c_res)
def clearf():
    ent.delete(0, "end")
# lines 19-33 are the clear, delete, and equals buttons.
# This code is just for the function of the buttons and not what the buttons look like
#(Thats the code down below)









#I changed the color of the clear and equals button, I changed the size for the

clean = Button(app,text="C",width=10,command=clearf,bg="red",fg="yellow",relief=RIDGE)
clean.grid(row=0,sticky="w",padx=125)

Shwadhin = Button(app,text="Shwadhin Time!",width=20,command=print('Shwadhin Time!'),bg="red",fg="blue",relief=RIDGE)
Shwadhin.grid(row=10,sticky="w",padx=125)








Char_nine = Button(text="9",width=2,command=lambda : ent.insert("end","9"),borderwidth=3,relief=RIDGE)
Char_nine.grid(row=1,sticky="w",padx=15)
Char_eight = Button(text="8",width=2,command=lambda : ent.insert("end","8"),borderwidth=3,relief=RIDGE)
Char_eight.grid(row=1,sticky="w",padx=45)
Char_seven = Button(app,text="7",width=2,command=lambda : ent.insert("end","7"),borderwidth=3,relief=RIDGE)
Char_seven.grid(row=1,sticky="w",padx=75)
Char_plus = Button(app,text="+",width=2,command=lambda : ent.insert("end","+"),borderwidth=3,relief=RIDGE)
Char_plus.grid(row=1,sticky="e",padx=125)
Char_six = Button(text="6",width=2,command=lambda : ent.insert("end","6"),borderwidth=3,relief=RIDGE)
Char_six.grid(row=2,sticky="w",padx=15,pady=5)
Char_five = Button(text="5",width=2,command=lambda : ent.insert("end","5"),borderwidth=3,relief=RIDGE)
Char_five.grid(row=2,sticky="w",padx=45,pady=5)
Char_four = Button(app,text="4",width=2,command=lambda : ent.insert("end","4"),borderwidth=3,relief=RIDGE)
Char_four.grid(row=2,sticky="w",padx=75,pady=5)
Char_minus = Button(app,text="-",width=2,command=lambda : ent.insert("end","-"),borderwidth=3,relief=RIDGE)
Char_minus.grid(row=2,sticky="e",padx=125,pady=5)
Char_three = Button(text="3",width=2,command=lambda : ent.insert("end","3"),borderwidth=3,relief=RIDGE)
Char_three.grid(row=3,sticky="w",padx=15,pady=5)
Char_two = Button(text="2",width=2,command=lambda : ent.insert("end","2"),borderwidth=3,relief=RIDGE)
Char_two.grid(row=3,sticky="w",padx=45,pady=5)
Char_one = Button(app,text="1",width=2,command=lambda : ent.insert("end","1"),borderwidth=3,relief=RIDGE)
Char_one.grid(row=3,sticky="w",padx=75,pady=5)
Char_multiply = Button(app,text="*",width=2,command=lambda : ent.insert("end","*"),borderwidth=3,relief=RIDGE)
Char_multiply.grid(row=3,sticky="e",padx=125,pady=5)
Char_zero = Button(text="0",width=2,command=lambda : ent.insert("end","0"),borderwidth=3,relief=RIDGE)
Char_zero.grid(row=4,sticky="w",padx=15,pady=5)
Char_double_zero = Button(text="00",width=2,command=lambda : ent.insert("end","00"),borderwidth=3,relief=RIDGE)
Char_double_zero.grid(row=4,sticky="w",padx=45,pady=5)
Char_dot = Button(app,text=".",width=2,command=lambda : ent.insert("end","."),borderwidth=3,relief=RIDGE)
Char_dot.grid(row=4,sticky="w",padx=75,pady=5)
Char_divide = Button(app,text="/",width=2,command=lambda : ent.insert("end","/"),borderwidth=3,relief=RIDGE)
Char_divide.grid(row=4,sticky="e",padx=125,pady=5)
result = Button(app,text="=",width=10,command=fresult,bg="blue",fg="red",borderwidth=3,relief=RIDGE)
result.grid(row=5,sticky="w",padx=15,pady=5)
Char_modulus = Button(app,text="%",width=2,command=lambda : ent.insert("end","%"),borderwidth=3,relief=RIDGE)
Char_modulus.grid(row=5,sticky="e",padx=125,pady=5)
delete = Button(app,text="del",width=2,command=delete,borderwidth=3,relief=RIDGE)
delete.grid(row=5,sticky="w",padx=80,pady=5)
# lines 38-77 are for the face of the calculator. It says the names of the buttons (button 3 has a "3 on it")
#this also includes the size, placement, and color of the buttons.


app.mainloop() #waits for event like buttons to be clicked before acting.