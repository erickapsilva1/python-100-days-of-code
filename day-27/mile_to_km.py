from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=120)

window.columnconfigure(0, weight=3)
window.columnconfigure(1, weight=3)
window.columnconfigure(2, weight=3)

my_font = ("Arial", 10, "normal")

miles = Entry(width=10, font=my_font)
text2 = Label(text="Miles", font=my_font)
text3 = Label(text="is equal to", font=my_font)
text4 = Label(text="0", font=my_font)
text5 = Label(text="Km", font=my_font)


def convert():
    converted_value = str(float(miles.get()) * 1.609)
    text4.config(text=converted_value)


button = Button(text="Calculate", command=convert, font=my_font)


miles.grid(column=1,row=0, sticky="ew", padx=5, pady=5)
text2.grid(column=2,row=0, sticky="ew", padx=5, pady=5)
text3.grid(column=0,row=1, sticky="ew", padx=5, pady=5)
text4.grid(column=1,row=1, sticky="ew", padx=5, pady=5)
text5.grid(column=2,row=1, sticky="ew", padx=5, pady=5)
button.grid(column=1, row=2, sticky="ew", padx=5, pady=5)

window.mainloop()