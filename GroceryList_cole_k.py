import tkinter as tk
from tkinter import *
import csv
from tkinter import colorchooser
global Price
Price = 0
#made by Cole Kleinebekel, kleinebekelc@gmail.com, have a good day and stay kind!
with open('C:\\Users\\molet\\OneDrive\\Desktop\\code\\list.csv', 'r') as read_obj: # read csv file as a list of lists
    csv_reader = csv.reader(read_obj) # pass the file object to reader() to get the reader object
    list_of_rows = list(csv_reader) # Pass reader object to list() to get a list of lists
cole = []

# Top level window
frame = tk.Tk()
frame.title("Grocery List by Cole K")
frame.geometry('400x600')
#frame.configure(bg='black')

# Function for getting Input
# at label widget
my_list = []

class Doodad:
    def __init__(self, name, quan, price):
        self.name = name
        self.quan = quan
        self.price = price
        
#for i in range(len(list_of_rows)):
#    person = Doodad(list_of_rows[i][0], 1, list_of_rows[i][1])
#    my_list.append(person)
    
my_list.append(Doodad('Coffee', 1, 2.99))
my_list.append(Doodad('Cole', 1, 1.99))


# TextBox Creation
lblN = tk.Label(frame, text = "Item Name")
lblN.pack()
inputtxtN = tk.Text(frame,
				height = 1,
				width = 20)

inputtxtN.pack()

# TextBox Creation
lblP = tk.Label(frame, text = "Item Price")
lblP.pack()
inputtxtP = tk.Text(frame,
				height = 1,
				width = 20)

inputtxtP.pack()

# label 
lblQ = tk.Label(frame, text = "Item Quantity")
lblQ.pack()

# txt box
inputtxtQ = tk.Text(frame,
				height = 1,
				width = 20)

inputtxtQ.pack()

def choose_color():
 
    # variable to store hexadecimal code of color
    color_code = colorchooser.askcolor(title ="Choose color")
    print(type(color_code))
    frame.config(bg= color_code[1])
    
button = Button(frame, text = "Select bg color",
                   command = choose_color)
button.pack()
button.place(x=300, y=550)
    

def popupKeep():
    inpN = inputtxtN.get(1.0, "end-1c")
    inpP = inputtxtP.get(1.0, "end-1c")
    inpQ = inputtxtQ.get(1.0, "end-1c")
    person1 = Doodad(inpN, inpQ, list_of_rows[Price][1])
    txt_output.delete("1.0","end")
    cole = False
    for i in range(len(my_list)):
        if my_list[i].name == inpN:
            my_list[i].quan = int(my_list[i].quan) + int(inpQ)
            cole = True
    if not cole:
        my_list.append(person1)
    for i in range(len(my_list)):
        txt_output.insert(END, my_list[i].name + " , " + str(my_list[i].quan) + " , " + str(my_list[i].price) + "\n")
        
    updateDataButton.place(x=-100, y=-100)
    setPriceDataButton.place(x=-100, y=-100)
    lbl3.place(x=-100, y=-100)

def popupUpdate():
    inpN = inputtxtN.get(1.0, "end-1c")
    inpP = inputtxtP.get(1.0, "end-1c")
    inpQ = inputtxtQ.get(1.0, "end-1c")
    person1 = Doodad(inpN, inpQ, inpP)
    list_of_rows[Price][1] = inpP
    lbl.configure(text= inpN + " is now " + inpP + " in the database")
    txt_output.delete("1.0","end")
    cole = False
    for i in range(len(my_list)):
        if my_list[i].name == inpN:
            my_list[i].quan = int(my_list[i].quan) + int(inpQ)
            cole = True
    if not cole:
        my_list.append(person1)
    for i in range(len(my_list)):
        txt_output.insert(END, my_list[i].name + " , " + str(my_list[i].quan) + " , " + str(my_list[i].price) + "\n")
        
    updateDataButton.place(x=-100, y=-100)
    setPriceDataButton.place(x=-100, y=-100)
    lbl3.place(x=-100, y=-100)


def printInput():
    inpN = inputtxtN.get(1.0, "end-1c")
    inpP = inputtxtP.get(1.0, "end-1c")
    inpQ = inputtxtQ.get(1.0, "end-1c")
    person1 = Doodad(inpN, inpQ, inpP)
    txt_output.delete("1.0","end")
    cole = False
    for i in range(len(my_list)):
        if my_list[i].name == inpN:
            my_list[i].quan = int(my_list[i].quan) + int(inpQ)
            cole = True
    if not cole:
        my_list.append(person1)
    for i in range(len(my_list)):
        txt_output.insert(END, my_list[i].name + " , " + str(my_list[i].quan) + " , " + str(my_list[i].price) + "\n")
            
    for i in range(len(list_of_rows)):
        if list_of_rows[i][0] == inpN and str(list_of_rows[i][1]) != inpP:
            Price = i
            lbl.configure(text="Database says that " + list_of_rows[i][0] + " costs " + list_of_rows[i][1])
            updateDataButton.place(x=10, y=45)
            setPriceDataButton.place(x=7, y=75)
            lbl3.place(x=10, y=5)
            my_list.pop()
            txt_output.delete("1.0","end")
            for i in range(len(my_list)):
                txt_output.insert(END, my_list[i].name + " , " + str(my_list[i].quan) + " , " + str(my_list[i].price) + "\n")
            
def removeInput():
    inpN = inputtxtN.get(1.0, "end-1c")
    inpP = inputtxtP.get(1.0, "end-1c")
    inpQ = inputtxtQ.get(1.0, "end-1c")
    for i in range(len(my_list)):
        if my_list[i].name == inpN:
            if int(my_list[i].quan) > int(inpQ):
                my_list[i].quan = int(my_list[i].quan) - int(inpQ)
            else:
                my_list.remove(my_list[i])
    txt_output.delete("1.0","end")
    for i in range(len(my_list)):
        txt_output.insert(END, my_list[i].name + " , " + str(my_list[i].quan) + " , " + str(my_list[i].price) + "\n")
        
def printPrice():
    price = 0
    for i in range(len(my_list)):
        price = price + float(my_list[i].price)*int(my_list[i].quan)
    lbl2.configure(text="Your Total Cost Is: " + str(price))
        
# Button Creation
printButton = tk.Button(frame,
						text = "add",
						command = printInput)
printButton.pack()
printButton.place(x=310, y=25)

# Button Creation
updateDataButton = tk.Button(frame,
						text = "Price entered",
						command = popupUpdate)
updateDataButton.pack()
updateDataButton.place(x=-100, y=-100)

# Button Creation
setPriceDataButton = tk.Button(frame,
						text = "Database Price",
						command = popupKeep)
setPriceDataButton.pack()
setPriceDataButton.place(x=-100, y=-100)

# Button Creation
remooveButton = tk.Button(frame,
						text = "remove",
						command = removeInput)
remooveButton.pack()
remooveButton.place(x=300, y=55)
# Button Creation
printPriceButton = tk.Button(frame,
						text = "price",
						command = printPrice)
printPriceButton.pack()
printPriceButton.place(x=307, y=85)

# Label Creation
lbl = tk.Label(frame, text = "Grocery List")
lbl.pack()
lbl2 = tk.Label(frame, text = "")
lbl2.pack()
lbl3 = tk.Label(frame, text = "Select Correct \n Price")
lbl3.pack()
lbl3.place(x=-100, y=-100)
#the box that shows
txt_output = tk.Text(frame, height=20, width=30)
txt_output.pack()

for i in range(len(my_list)):
    txt_output.insert(END, my_list[i].name + " , " + str(my_list[i].quan) + " , " + str(my_list[i].price) + "\n")

frame.mainloop()