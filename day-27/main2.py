import tkinter
from builtins import input

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack(side="left")

my_label["text"] = "New Text"
my_label.config(text="New Text")


# Button
def button_clicked():
    print("I got clicked")
    my_label.config(text="Button Got Clicked")


# Entry
input = tkinter.Entry(width=10)

def button_clicked2():
    my_label.config(text=input.get())


button = tkinter.Button(text="Click Me", command=button_clicked2)

my_label.grid(column=0, row=0)
button.grid(column=1, row=1)
input.grid(column=2, row=3)

window.mainloop()
