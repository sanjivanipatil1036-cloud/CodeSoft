
import tkinter as tkr
from tkinter import messagebox
import random
import string

def gnrt_pswd():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Weak Password", "Length must be at least 4 characters!")
            return

        lts = string.ascii_letters
        dts = string.digits
        sym = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

        all_ch = lts + dts + sym
        passwd = "".join(random.sample(all_ch, length))

        result_entry.delete(0, tkr.END)
        result_entry.insert(0, passwd)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")

def copy():
    root.clipboard_clear()
    root.clipboard_append(result_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")
root = tkr.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.config(bg="#F5F5F5")

title_label = tkr.Label(root, text="Password Generator", font=("Arial", 16, "bold"), bg="#F5F5F5")
title_label.pack(pady=10)

length_label = tkr.Label(root, text="Enter password length:", font=("Arial", 12), bg="#F5F5F5")
length_label.pack(pady=5)

length_entry = tkr.Entry(root, font=("Arial", 12), width=10, justify="center")
length_entry.pack(pady=5)

generate_btn = tkr.Button(root, text="Generate", command=gnrt_pswd, bg="#4CAF50", fg="white", width=12)
generate_btn.pack(pady=8)

result_entry = tkr.Entry(root, font=("Arial", 12), width=30, justify="center")
result_entry.pack(pady=8)

copy_btn = tkr.Button(root, text="Copy", command=copy, bg="#2196F3", fg="white", width=12)
copy_btn.pack(pady=8)

footer_label = tkr.Label(root, text="Created by Sanjivani Patil | CODSOFT", font=("Arial", 8), bg="#F5F5F5", fg="gray")
footer_label.pack(side="bottom", pady=10)

root.mainloop()
