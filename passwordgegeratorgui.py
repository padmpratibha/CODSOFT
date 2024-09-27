import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    length = int(length_entry.get())
    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation
    
    all_characters = letters + digits + punctuation
    
    password = ''.join(random.choice(all_characters) for i in range(length))
    password_entry.delete(0, tk.END)  # Clear previous password
    password_entry.insert(0, password)  # Insert new password

# Function to copy password to clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")

# Create a label and entry for password length
length_label = tk.Label(root, text="Password Length:")
length_label.pack(pady=10)

length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Create a button to generate password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Create an entry to display the generated password
password_entry = tk.Entry(root, width=40)
password_entry.pack(pady=5)

# Create a button to copy password to clipboard
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=10)

# Run the application
root.mainloop()
