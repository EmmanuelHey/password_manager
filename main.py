from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))

    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    # password = ""
    # for char in password_list:
    #     password += char

    password = "".join(password_list)
    pass_entry.insert(0, password)

    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    passw = pass_entry.get()
    new_data = {
        website: {
        "email": email,
        "password": passw,
        }
    }

    if website == "" or passw == "":
        messagebox.showerror("Oops", message="Please don't leave any fields empty")
    else:
        # is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email: {email}\n Password: {passw}\n "
        #                                           f"Is it ok to save?")
        # if is_ok:
        try:
            with open("data.json", "r") as data_file:
                # data.write(f"{website} | {email} | {passw}\n")
                #json.dump(new_data, data, indent=4)
                data = json.load(data_file)
                for x in data.keys():
                    print(x)
                #print(data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        website_entry.delete(0, END)
        pass_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        for x in data.keys():
            if website == x:
                messagebox.showinfo(title=website,
                                    message=f"Email: {data[x]['email']}\nPassword: {data[x]['password']}")
            else:
                messagebox.showerror(title="Error", message=f"No details for the {website} exists")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
pass_logo = PhotoImage(file="logo.png") #imports the file into a variable that can be used by the canvas
canvas.create_image(100, 100, image=pass_logo)
#canvas.grid()
canvas.grid(column=1, row=0)

#websit
website_text = Label(text="Website:")
website_text.grid(column=0, row=1)

website_entry = Entry(width=20)
website_entry.grid(column=1, row=1, )
website_entry.focus()

#search
search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)


#email/username
email_text = Label(text="Email/Username:")
email_text.grid(column=0, row=2)

email_entry = Entry(width=38)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "folafako05@gmail.com")

#password
pass_text = Label(text="Password:")
pass_text.grid(column=0, row=3)

pass_entry = Entry(width=20)
pass_entry.grid(column=1, row=3)

generate_pass = Button(text="Generate Password", command=password_generator)
generate_pass.grid(column=2, row=3)

#add
add_button = Button(text="Add", width=33, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()