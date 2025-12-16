from tkinter import * #type:ignore
from tkinter import messagebox
import random
import pyperclip
import json

# ===== WINDOW / CONTAINER =====
ROOT_BG   = "#0B0F14"   # window background (very dark, soft)
CANVAS_BG = "#121826"   # main card / canvas background

# ===== TEXT =====
TEXT_PRIMARY   = "#E5E7EB"   # main text
TEXT_SECONDARY = "#44474B"   # labels / hints

# ===== INPUT FIELDS =====
ENTRY_BG = "#0B1020"         # entry background
ENTRY_FG = "#F9FAFB"         # entry text

# ===== BUTTONS =====
BTN_PRIMARY = "#7C83FD"      # generate password
BTN_SUCCESS = "#2DD4BF"      # save
BTN_MUTED   = "#64748B"      # search
BTN_DANGER  = "#F87171"      # clear / delete




# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_genrated():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2 , 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_letters )

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    
def clear():
    email_entry.delete(0, END)
def find_password():
    website = website_entry.get()
    if len(website) == 0:
        messagebox.showinfo(title="Oops", message="required feild is empty.\nplease check your website input")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                messagebox.showinfo(title=f"{website} credentials", message=f"Email/Username: {data[website]["email"]}\nPassword: {data[website]["password"]}")
        except KeyError:
            if website.title() != "All": 
                messagebox.showinfo(title="unknown app", message= "The website you have entered is not saved please input 'All' " \
                "to see all your websites credentials one by one in sequence")
            elif website.title() == "All":
                with open("data.json") as data_file:
                    data = json.load(data_file)

                    for i in data:
                        messagebox.showinfo(title=i, message=f"Email/Username: {data[i]["email"]}\nPassword: {data[i]["password"]}")
        except FileNotFoundError:
            messagebox.showinfo(title="oops", message="you have not saved anything. in order to search you atleast need one credential saved")
        except json.JSONDecodeError:
            messagebox.showinfo(title="oops", message="you have not saved anything. in order to search you atleast need one credential saved")
    
        
    

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    is_ok = True
    new_data = {
         website: {
              "email": email,
              "password": password
         }
        }

    if len(email) == 0:
         email = None
    if len(website) == 0 or len(password) == 0:
            messagebox.showinfo(title="Oops", message="required feild is empty.\nplease check your inputs")
            is_ok = False
    
    elif is_ok:
        
        is_ok = messagebox.askokcancel(title=website, message=f"these are the details entered:" 
                           f"\nWebsite: {website}\nEmail: {email} \nPassword: {password} \n do you wanna save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    
                    data = json.load(data_file)

            except:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:    
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.title("Password Manager")

window.config(padx=50, pady=50, bg=ROOT_BG, highlightthickness=0,)

canvas = Canvas(width=200, height=200,bg=CANVAS_BG, highlightthickness=0)
logo = PhotoImage(file="logo.png")

canvas.create_image(100, 100, image=logo, )
canvas.grid(row=0, column=1)

# labels
website_label = Label(text="Website:", width=13, fg=TEXT_PRIMARY, bg=TEXT_SECONDARY)
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", fg=TEXT_PRIMARY, bg=TEXT_SECONDARY)
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", width=13, fg=TEXT_PRIMARY, bg=TEXT_SECONDARY)
password_label.grid(row=3, column=0)



# entries 
website_entry = Entry(width=26, bg=ENTRY_BG, fg=ENTRY_FG, insertbackground=TEXT_PRIMARY)
website_entry.grid(row=1, column=1, )
website_entry.focus()

email_entry = Entry(width=26, bg=ENTRY_BG,  fg=ENTRY_FG, insertbackground=TEXT_PRIMARY)
email_entry.grid(row=2, column=1, columnspan=1)
email_entry.insert(0, "") # insert in the strings default email/username to save everything

password_entry = Entry(width=26, bg=ENTRY_BG, fg=ENTRY_FG, insertbackground=TEXT_PRIMARY)
password_entry.grid(row=3, column=1,)




add_button = Button(text="Save", width=40, command=save, bg=BTN_SUCCESS)
add_button.grid(row=4, column=1,columnspan=2 )
generate_button = Button(text="Generate Pass", command=password_genrated, bg=BTN_PRIMARY)
generate_button.grid(row=3, column=2,)
search_button = Button(text="search", width=11, command=find_password, bg=BTN_MUTED)
search_button.grid(row=1, column=2,)
clear_button = Button(text="clear", width=11, command=clear, bg=BTN_DANGER)
clear_button.grid(row=2, column=2)
window.mainloop()