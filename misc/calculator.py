from tkinter import *
class Calculator(Frame):
    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.pack()
        self.display = ''
        self.symbols = '789/456*123-0.=+'
        self.entry = Entry(self)
        self.entry.grid(columnspan=4)
        for i in range(4):
            for j in range(4):
                self.create_button(self.symbols[j+(4*i)]).grid(row=i+1, column=j)
        self.clear = Button(self)
        self.clear['text'] = 'C'
        self.clear['command'] = lambda: self.__clear()
        self.clear.grid(row=5,column=0)
    def __clear(self):
        self.display=''
        self.entry.delete(0, END)
        self.entry.insert(0, self.display)
    def create_button(self, symbol):
        self.button = Button(self)
        self.button['text'] = symbol
        self.button['command'] = lambda: self.__eq__() if symbol is '=' else self.__update(symbol)
        return self.button
    def __eq__(self):
        self.display = eval(self.display)
        self.entry.delete(0, END)
        self.entry.insert(0, self.display)
    def __update(self, symbol):
        self.entry.delete(0, END)
        self.display += symbol
        self.entry.insert(0, self.display)
app = Calculator(master=Tk())
app.mainloop()
