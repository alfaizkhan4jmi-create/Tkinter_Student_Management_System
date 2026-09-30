# ============================================================
# ---------------- Tkinter Admin Registration ----------------
# Tkinter + MySQL + Treeview + Image
# ============================================================

from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import pymysql
from dotenv import load_dotenv
import os

load_dotenv()


# ============================================================
# MAIN WINDOW
# ============================================================

top = Tk()
top.title("Admin Registration")
top.geometry("1400x650")
top.resizable(False, False)


# ============================================================
# COURSE LIST
# ============================================================

courses = ["Python", "C++", "Java", "ML", "C", "DL"]


# ============================================================
# IMAGE
# ============================================================

try:
    img = Image.open(
        r"C:\Users\ALFAIZ KHAN\OneDrive\Desktop\Images_web\Ak01.jpg"
    )

    img = img.resize((1400, 650))
    img = ImageTk.PhotoImage(img)

    L6 = Label(top, image=img)
    L6.place(x=0, y=0)

except Exception:
    L6 = Label(
        top,
        text="Image Not Found",
        bg="red",
        fg="white",
        font=("Arial", 16, "bold")
    )
    L6.place(x=30, y=30)


# ============================================================
# HEADING
# ============================================================

L = Label(
    top,
    text="Admin Registration",
    bg="green",
    fg="white",
    font=("Arial", 20, "bold")
)
L.place(x=570, y=25)


# ============================================================
# NAME
# ============================================================

L2 = Label(
    top,
    text="Name",
    bg="green",
    fg="white",
    font=("Arial", 20, "bold")
)
L2.place(x=100, y=100)

e1 = Entry(
    top,
    font=("Arial", 20, "bold"),
    width=20
)
e1.place(x=300, y=100)


# ============================================================
# FATHER NAME
# ============================================================

L3 = Label(
    top,
    text="Father Name",
    bg="green",
    fg="white",
    font=("Arial", 20, "bold")
)
L3.place(x=100, y=180)

e2 = Entry(
    top,
    font=("Arial", 20, "bold"),
    width=20
)
e2.place(x=300, y=180)


# ============================================================
# CITY
# ============================================================

L4 = Label(
    top,
    text="City",
    bg="green",
    fg="white",
    font=("Arial", 20, "bold")
)
L4.place(x=100, y=260)

e3 = Entry(
    top,
    font=("Arial", 20, "bold"),
    width=20
)
e3.place(x=300, y=260)


# ============================================================
# GENDER
# ============================================================

L5 = Label(
    top,
    text="Gender",
    bg="green",
    fg="white",
    font=("Arial", 20, "bold")
)
L5.place(x=100, y=340)

e4 = Entry(
    top,
    font=("Arial", 20, "bold"),
    width=20
)
e4.place(x=300, y=340)


# ============================================================
# COURSE COMBOBOX
# ============================================================

L7 = Label(
    top,
    text="Course",
    bg="green",
    fg="white",
    font=("Arial", 20, "bold")
)
L7.place(x=100, y=420)

cb = ttk.Combobox(
    top,
    values=courses,
    font=("Arial", 20, "bold"),
    state="readonly",
    width=19
)
cb.place(x=300, y=420)


# ============================================================
# PASSWORD
# ============================================================

L8 = Label(
    top,
    text="Password",
    bg="green",
    fg="white",
    font=("Arial", 20, "bold")
)
L8.place(x=100, y=480)

e5 = Entry(
    top,
    show="*",
    font=("Arial", 20, "bold"),
    width=17
)
e5.place(x=300, y=480)


# ============================================================
# SHOW / HIDE PASSWORD
# ============================================================

def show_password():

    if e5.cget("show") == "*":
        e5.config(show="")
        password_btn.config(text="Hide")

    else:
        e5.config(show="*")
        password_btn.config(text="Show")


password_btn = Button(
    top,
    text="Show",
    font=("Arial", 12, "bold"),
    command=show_password
)
password_btn.place(x=610, y=485)


# ============================================================
# DATABASE CONNECTION SQL SE HOGA.....
def database_connection():

    db = pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    return db


# ============================================================
# INSERT FUNCTION
# ============================================================

def Insert():

    k1 = e1.get()
    k2 = e2.get()
    k3 = e3.get()
    k4 = e4.get()
    k5 = cb.get()
    k6 = e5.get()

    # ---------------- VALIDATION ----------------

    if k1 == "":
        messagebox.showwarning(
            "Warning",
            "Please enter Name"
        )
        return

    if k2 == "":
        messagebox.showwarning(
            "Warning",
            "Please enter Father Name"
        )
        return

    if k3 == "":
        messagebox.showwarning(
            "Warning",
            "Please enter City"
        )
        return

    if k4 == "":
        messagebox.showwarning(
            "Warning",
            "Please enter Gender"
        )
        return

    if k5 == "":
        messagebox.showwarning(
            "Warning",
            "Please select Course"
        )
        return

    if k6 == "":
        messagebox.showwarning(
            "Warning",
            "Please enter Password"
        )
        return

    # ---------------- DATABASE ----------------

    try:

        db = database_connection()
        cur = db.cursor()

        sql = """
        INSERT INTO india01
        (Name, FatherName, City, Gender, Course, Password)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (
            k1,
            k2,
            k3,
            k4,
            k5,
            k6
        )

        cur.execute(sql, values)
        db.commit()

        messagebox.showinfo(
            "Success",
            "Record inserted successfully"
        )

        # Clear fields

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        cb.set("")
        e5.delete(0, END)

        cur.close()
        db.close()

    except Exception as error:

        messagebox.showerror(
            "Database Error",
            str(error)
        )


# ============================================================
# SUBMIT BUTTON
# ============================================================

submit_btn = Button(
    top,
    text="Submit",
    font=("Arial", 18, "bold"),
    command=Insert
)

submit_btn.place(
    x=300,
    y=535
)


# ============================================================
# DELETE FUNCTION
# ============================================================

def delete():

    name = e1.get()

    if name == "":
        messagebox.showwarning(
            "Warning",
            "Enter Name to delete"
        )
        return

    try:

        db = database_connection()
        cur = db.cursor()

        sql = "DELETE FROM india01 WHERE Name = %s"

        cur.execute(
            sql,
            (name,)
        )

        result = cur.rowcount

        db.commit()

        if result > 0:

            messagebox.showinfo(
                "Success",
                "Record deleted successfully"
            )

        else:

            messagebox.showinfo(
                "Result",
                "Record not found"
            )

        cur.close()
        db.close()

    except Exception as error:

        messagebox.showerror(
            "Database Error",
            str(error)
        )


# ============================================================
# TREEVIEW
# ============================================================

tv = ttk.Treeview(
    top,
    show="headings"
)

tv["columns"] = (
    "Name",
    "FatherName",
    "City",
    "Gender",
    "Course",
    "Password"
)


# ============================================================
# TREEVIEW COLUMNS
# ============================================================

tv.column(
    "Name",
    anchor=CENTER,
    width=90,
    stretch=False
)

tv.column(
    "FatherName",
    anchor=CENTER,
    width=120,
    stretch=False
)

tv.column(
    "City",
    anchor=CENTER,
    width=80,
    stretch=False
)

tv.column(
    "Gender",
    anchor=CENTER,
    width=80,
    stretch=False
)

tv.column(
    "Course",
    anchor=CENTER,
    width=90,
    stretch=False
)

tv.column(
    "Password",
    anchor=CENTER,
    width=100,
    stretch=False
)


# ============================================================
# TREEVIEW HEADINGS
# ============================================================

tv.heading(
    "Name",
    text="Name"
)

tv.heading(
    "FatherName",
    text="Father Name"
)

tv.heading(
    "City",
    text="City"
)

tv.heading(
    "Gender",
    text="Gender"
)

tv.heading(
    "Course",
    text="Course"
)

tv.heading(
    "Password",
    text="Password"
)


# ============================================================
# TREEVIEW POSITION
# ============================================================

tv.place(
    x=730,
    y=100,
    width=600,
    height=350
)


# ============================================================
# SHOW FUNCTION
# ============================================================

def show():

    # Clear old data

    for item in tv.get_children():
        tv.delete(item)

    try:

        db = database_connection()
        cur = db.cursor()

        sql = "SELECT * FROM india01"

        cur.execute(sql)

        result = cur.fetchall()

        for col in result:

            Name = col[0]
            FatherName = col[1]
            City = col[2]
            Gender = col[3]
            Course = col[4]
            Password = col[5]

            tv.insert(
                "",
                "end",
                values=(
                    Name,
                    FatherName,
                    City,
                    Gender,
                    Course,
                    Password
                )
            )

        cur.close()
        db.close()

    except Exception as error:

        messagebox.showerror(
            "Database Error",
            str(error)
        )


# ============================================================
# SHOW BUTTON
# ============================================================

show_btn2 = Button(
    top,
    text="Show",
    font=("Arial", 18, "bold"),
    command=show
)

show_btn2.place(
    x=950,
    y=470
)


# ============================================================
# DELETE BUTTON
# ============================================================

delete_btn = Button(
    top,
    text="Delete",
    font=("Arial", 18, "bold"),
    command=delete
)

delete_btn.place(
    x=600,
    y=535
)


# ============================================================
# USER PAGE
# ============================================================

def userpage():

    top.destroy()

    import userpage


# ============================================================
# ADMIN PAGE
# ============================================================

def adminpage():

    top.destroy()

    import adminpage


# ============================================================
# USER PAGE BUTTON
# ============================================================

user_btn = Button(
    top,
    text="User Page",
    font=("Arial", 18, "bold"),
    command=userpage
)

user_btn.place(
    x=950,
    y=535
)


# ============================================================
# ADMIN PAGE BUTTON
# ============================================================

admin_btn = Button(
    top,
    text="Admin Page",
    font=("Arial", 18, "bold"),
    command=adminpage
)

admin_btn.place(
    x=1120,
    y=535
)


# ============================================================
# MAIN LOOP
# ============================================================

top.mainloop()