#--------------------ADMINPAGE--------------------
from tkinter import *
from tkinter import messagebox


# ================= MAIN WINDOW =================

admin = Tk()

admin.title("Admin Login")
admin.geometry("600x450")
admin.config(bg="lightblue")


# ================= HEADING =================

Label(
    admin,
    text="ADMIN LOGIN",
    font=("Arial", 28, "bold"),
    bg="darkblue",
    fg="white"
).pack(fill=X, pady=20)


# ================= USERNAME =================

Label(
    admin,
    text="Username",
    font=("Arial", 18, "bold"),
    bg="lightblue"
).place(x=100, y=130)

username = Entry(
    admin,
    font=("Arial", 18)
)

username.place(x=250, y=130)


# ================= PASSWORD =================

Label(
    admin,
    text="Password",
    font=("Arial", 18, "bold"),
    bg="lightblue"
).place(x=100, y=190)

password = Entry(
    admin,
    show="*",
    font=("Arial", 18)
)

password.place(x=250, y=190)


# ================= LOGIN FUNCTION =================

def login():

    user = username.get()
    pwd = password.get()

    # Admin login details
    if user == "admin" and pwd == "1234":

        messagebox.showinfo(
            "Login",
            "Admin Login Successful"
        )

    else:

        messagebox.showerror(
            "Login Failed",
            "Invalid Username or Password"
        )


# ================= LOGIN BUTTON =================

Button(
    admin,
    text="Login",
    font=("Arial", 18, "bold"),
    bg="green",
    fg="white",
    command=login
).place(
    x=250,
    y=260
)


# ================= BACK FUNCTION =================

def back():

    admin.destroy()

    import firstproject01


# ================= BACK BUTTON =================

Button(
    admin,
    text="Back",
    font=("Arial", 14, "bold"),
    command=back
).place(
    x=260,
    y=330
)


# ================= MAIN LOOP =================

admin.mainloop()
