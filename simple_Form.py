import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    message = text_message.get("1.0", tk.END)

    # Example validation (you can expand this)
    if not name.strip():
        messagebox.showerror("Error", "Name cannot be empty!")
        return
    if not email.strip() or '@' not in email:
        messagebox.showerror("Error", "Invalid email address!")
        return
    if not message.strip():
        messagebox.showerror("Error", "Message cannot be empty!")
        return

    # Process the form (e.g., save to a file, send via email, etc.)
    # Replace the following line with your actual form processing logic
    print(f"Name: {name}\nEmail: {email}\nMessage:\n{message}")

# Create main window
root = tk.Tk()
root.title("Form Builder")

# Create form components
label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

label_email = tk.Label(root, text="Email:")
label_email.grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1, padx=10, pady=5)

label_message = tk.Label(root, text="Message:")
label_message.grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
text_message = tk.Text(root, height=5, width=30)
text_message.grid(row=2, column=1, padx=10, pady=5)

submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=3, columnspan=2, padx=10, pady=10)

# Start the main tkinter loop
root.mainloop()
