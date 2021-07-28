from tkinter import *

window = Tk()
window.title('Weight Converter')

def convert():
    gram = float(e1_value.get()) * 1000
    pound = float(e1_value.get()) * 2.20462
    ounce = float(e1_value.get()) * 35.274
    #Empty the text boxes if they had text from the previous one    
    t1.delete("1.0", END) #delete the content of the text box from the start to END
    t1.insert(END, gram)
    t2.delete("1.0", END)
    t2.insert(END, pound)
    t3.delete("1.0", END)
    t3.insert(END, ounce)  

b1=Button(window, text="Convert", command=convert)
b1.grid(row=0,column=2)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)
#Create a label widget with "Kg" as label
e2=Label(window, text="Kg")
e2.grid(row=0,column=0)
#gram label
e3=Label(window, text="Grams")
e3.grid(row=1,column=0)
#pound label
e4=Label(window, text="Pounds")
e4.grid(row=1,column=2)
#ounce label
e5=Label(window, text="Ounces")
e5.grid(row=1,column=4)

t1=Text(window,height=1, width=20, bg='light cyan')
t1.grid(row=1,column=1)
t2=Text(window,height=1, width=20, bg='light cyan')
t2.grid(row=1,column=3)
t3=Text(window,height=1, width=20, bg='light cyan')
t3.grid(row=1,column=5)


window.mainloop()