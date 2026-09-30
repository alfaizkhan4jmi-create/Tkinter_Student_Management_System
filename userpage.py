#--------------------USERPAGE--------------------------------
from tkinter import *
from tkinter import messagebox
import pymysql


# ============================================================
# MAIN WINDOW
# ============================================================

user = Tk()

user.title("User Login")
user.geometry("700x500")
user.config(bg="lightblue")


# ============================================================
# HEADING
# ============================================================

Label(
    user,
    text="USER LOGIN",
    font=("Arial", 28, "bold"),
    bg="darkblue",
    fg="white"
).pack(fill=X, pady=20)


# ============================================================
# NAME
# ============================================================

Label(
    user,
    text="Name",
    font=("Arial", 18, "bold"),
    bg="lightblue"
).place(x=130, y=130)

name_entry = Entry(
    user,
    font=("Arial", 18)
)

name_entry.place(x=280, y=130)


# ============================================================
# PASSWORD
# ============================================================

Label(
    user,
    text="Password",
    font=("Arial", 18, "bold"),
    bg="lightblue"
).place(x=100, y=190)

password_entry = Entry(
    user,
    show="*",
    font=("Arial", 18)
)

password_entry.place(x=280, y=190)


# ============================================================
# LOGIN FUNCTION
# ============================================================

def login():

    name = name_entry.get()
    password = password_entry.get()

    if name == "" or password == "":
        messagebox.showwarning(
            "Warning",
            "Please enter Name and Password"
        )
        return

    try:

        # Database connection

        db = pymysql.connect(
            host="localhost",
            user="root",
            password="india123",
            database="hamza"
        )

        cur = db.cursor()

        # Check user

        sql = """
        SELECT * FROM india01
        WHERE Name=%s AND Password=%s
        """

        cur.execute(
            sql,
            (name, password)
        )

        result = cur.fetchone()

        cur.close()
        db.close()

        # ====================================================
        # LOGIN SUCCESS
        # ====================================================

        if result:

            messagebox.showinfo(
                "Login",
                "Login Successful"
            )

            show_profile(result)

        else:

            messagebox.showerror(
                "Login Failed",
                "Invalid Name or Password"
            )

    except Exception as error:

        messagebox.showerror(
            "Database Error",
            str(error)
        )


# ============================================================
# SHOW USER PROFILE
# ============================================================

def show_profile(data):

    # Remove login widgets

    for widget in user.winfo_children():
        widget.destroy()

    user.config(bg="white")

    Label(
        user,
        text="USER PROFILE",
        font=("Arial", 28, "bold"),
        bg="darkblue",
        fg="white"
    ).pack(fill=X, pady=20)

    # Data from MySQL

    name = data[0]
    father_name = data[1]
    city = data[2]
    gender = data[3]
    course = data[4]

    Label(
        user,
        text=f"Name : {name}",
        font=("Arial", 18, "bold"),
        bg="white"
    ).pack(pady=10)

    Label(
        user,
        text=f"Father Name : {father_name}",
        font=("Arial", 18, "bold"),
        bg="white"
    ).pack(pady=10)

    Label(
        user,
        text=f"City : {city}",
        font=("Arial", 18, "bold"),
        bg="white"
    ).pack(pady=10)

    Label(
        user,
        text=f"Gender : {gender}",
        font=("Arial", 18, "bold"),
        bg="white"
    ).pack(pady=10)

    Label(
        user,
        text=f"Course : {course}",
        font=("Arial", 18, "bold"),
        bg="white"
    ).pack(pady=10)


# ============================================================
# LOGIN BUTTON
# ============================================================

login_btn = Button(
    user,
    text="Login",
    font=("Arial", 18, "bold"),
    bg="green",
    fg="white",
    command=login
)

login_btn.place(
    x=290,
    y=270
)


# ============================================================
# BACK FUNCTION
# ============================================================

def back():

    user.destroy()

    import firstproject01


# ============================================================
# BACK BUTTON
# ============================================================

back_btn = Button(
    user,
    text="Back",
    font=("Arial", 14, "bold"),
    command=back
)

back_btn.place(
    x=295,
    y=350
)


# ============================================================
# MAIN LOOP
# ============================================================

user.mainloop()

