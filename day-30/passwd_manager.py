from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_passwd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    passwd_letters = [random.choice(letters) for _ in range(nr_letters)]
    passwd_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    passwd_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    passwd_list = passwd_letters + passwd_symbols + passwd_numbers

    random.shuffle(passwd_list)

    password = "".join(passwd_list)

    entry_password.delete(0, END)
    entry_password.insert(0, string=password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = entry_website.get()
    email = entry_email_uname.get()
    password = entry_password.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if website != "" and email != "" and password != "":

        try:
            with open("data.json", mode="r") as file:
                # Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", mode="w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)



    else:
        messagebox.showinfo(title="Ops", message="Please don't leave any field empty!")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def find_password():
    website = entry_website.get()
    found = False

    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showerror(title="Oops", message="No Data File Found.")
    else:
        for key, value in data.items():
            if key.lower() == website.lower():
                messagebox.showinfo(title=f"Password Data - {website}",
                                    message=f"Email: {value['email']}\n"
                                            f"Password: {value['password']}")
                found = True

        if not found:
            messagebox.showinfo(title="Oops", message="No details for the website exists.")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

def generate_password():
    pass


label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

entry_website = Entry()
entry_website.grid(column=1, row=1, columnspan=2, sticky="EW")
entry_website.focus()

search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky="EW")

label_email_uname = Label(text="Email/Username:")
label_email_uname.grid(column=0, row=2)

entry_email_uname = Entry()
entry_email_uname.grid(column=1, row=2, columnspan=2, sticky="EW")
entry_email_uname.insert(END, "user.email@mail.com")

label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

entry_password = Entry()
entry_password.grid(column=1, row=3, sticky="EW")

generate_btn = Button(text="Generate Password", command=generate_passwd)
generate_btn.grid(column=2, row=3, sticky="EW")

add_btn = Button(text="Add", width=35, command=add)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()