from tkinter import *

root = Tk()
root.title("YardStick")

myTitle = Label(root, text="YardStick!", width=40, height=5, font=('Times New Roman', 15, 'bold')).grid(row=0, columnspan=2)
myDescription = Label(root, text="Enter your yards measurements for a free estimate!").grid(row=1)
widthLabel= Label(root, text="Enter the width of your yard: ").grid(row=2, column=0)
lengthLabel= Label(root, text="Enter the length of your yard: ").grid(row=3, column=0)

def button_click(number):
    ewidth= e1.get()
    elength= e2.get()
    area= ewidth * elength

e1 = Entry(root, width=30).grid(row=2, column=1)
e2 = Entry(root, width=30).grid(row=3, column=1)

button_1 = Button(root, text="Next", padx=20, pady=10, command= button_click)

button_1.grid(row=4, column=1)

root.mainloop()