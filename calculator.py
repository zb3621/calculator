
from tkinter import*
master = Tk()
display = Entry(master, width=11, justify='right', bd=0, bg='green')
master.title('calculator')

class Calculator:
    def__init__(self):
        self.var1=""
        self.var2=""
        self.result=0
        self.current=0
        self.operator=0

    def numb_butt(self, index):
        if self.current is 0:
            self.var1=str(self.var1) + str(index)
            display.delete(0,end)
            display.insert(0, string=self.var1)
        else:
            self.var2=str(self.var2) + str(index)
            display.delete(0,end)
            display.insert(0, string=self.var2)
        
    def equate(self):
        if self.operator is 0:
            self.result = float(self.var1) + float(self.var2)
        elif self.operator is 1:
            self.result = float(self.var1) - float(self.var2)
        elif self.operator is 2:
            self.result = float(self.var1) * float(self.var2)
        elif self.operator is 3:
            self.result = float(self.var1) / float(self.var2)
        display.delete  (0, END)
        display.insert(0, string=self.result)

    def set_op(self, op):
        self.operator = op
        display.delete(0, END)
        if self.current is 0:
            self.current = 1
        else:
            self.equate()
            self.var2 = ""
    def clear(self):
        self.__init__()
        display.delete(0,END)

calc = calculator()
b0 = button(master, text="0", command=lamda: calc.numb_butt(0))
b0 = button(master, text="1", command=lamda: calc.numb_butt(1))
b0 = button(master, text="2", command=lamda: calc.numb_butt(2))
b0 = button(master, text="3", command=lamda: calc.numb_butt(3))
b0 = button(master, text="4", command=lamda: calc.numb_butt(4))
b0 = button(master, text="5", command=lamda: calc.numb_butt(5))
b0 = button(master, text="6", command=lamda: calc.numb_butt(6))
b0 = button(master, text="7", command=lamda: calc.numb_butt(7))
b0 = button(master, text="8", command=lamda: calc.numb_butt(8))
b0 = button(master, text="9", command=lamda: calc.numb_butt(9))
b_dot = button(master, text=",", command=lamda: calc.numb_butt(","))

plus = button(master, text="+", command=lamda: calc.set_op(0))
minus = button(master, text="-", command=lamda: calc.set_op(1))
times = button(master, text="*", command=lamda: calc.set_op(2))
divide = button(master, text="/", command=lamda: calc.set_op(3))

equals = button(master, text="=", command=calc.equal)
clear = button(master, text "c", command=calc.clear)


display.place(x=0, y=2)
b7.grid(row=1, column=0)
b8.grid(row=1, column=1)
b9.grid(row=1, column=2)
b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)
b0.grid(row=4, column=0)
b_dot.grid(row=4, cloumn=1)
clean.grid(row=4, column=2)
plus.grid(row=0, column=3)
minus.grid(row=1, column=3)
times.grid(row=1, column=3)
divide.grid(row=1, column=3)
equals.grid(row=4, column=3)
master.mainloop()

