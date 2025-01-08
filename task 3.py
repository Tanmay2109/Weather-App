import tkinter as tk
import random
import string
import pyperclip

# Function to generate a password based on selected criteria
def generate_password():
    password_length = int(entry_length.get())
    use_uppercase = var_uppercase.get()
    use_numbers = var_numbers.get()
    use_special = var_special.get()
    
    # Define the character sets
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    # Ensure the password meets the minimum complexity
    if password_length < 8:
        label_result.config(text="Password length must be at least 8 characters.")
        return
    
    # Generate the password
    password = ''.join(random.choice(characters) for i in range(password_length))

    # Ensure the password adheres to security rules
    if use_uppercase and not any(char.isupper() for char in password):
        password = random.choice(string.ascii_uppercase) + password[1:]
    if use_numbers and not any(char.isdigit() for char in password):
        password = random.choice(string.digits) + password[1:]
    if use_special and not any(char in string.punctuation for char in password):
        password = random.choice(string.punctuation) + password[1:]

    # Update the result label with the generated password
    label_result.config(text="Generated Password: " + password)

    # Store the generated password for clipboard copying
    global generated_password
    generated_password = password

# Function to copy the generated password to clipboard
def copy_to_clipboard():
    if generated_password:
        pyperclip.copy(generated_password)
        label_copy_status.config(text="Password copied to clipboard!")
    else:
        label_copy_status.config(text="No password generated yet!")

# Create the main application window
window = tk.Tk()
window.title("Advanced Password Generator")

# Initialize the generated password variable
generated_password = ""

# Label for password length
label_length = tk.Label(window, text="Password Length:")
label_length.grid(row=0, column=0, padx=10, pady=10, sticky="w")

entry_length = tk.Entry(window)
entry_length.grid(row=0, column=1, padx=10, pady=10)
entry_length.insert(0, "12")  # Default password length

# Checkboxes for password complexity options
var_uppercase = tk.BooleanVar()
check_uppercase = tk.Checkbutton(window, text="Include Uppercase Letters", variable=var_uppercase)
check_uppercase.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

var_numbers = tk.BooleanVar()
check_numbers = tk.Checkbutton(window, text="Include Numbers", variable=var_numbers)
check_numbers.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

var_special = tk.BooleanVar()
check_special = tk.Checkbutton(window, text="Include Special Characters", variable=var_special)
check_special.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

# Button to generate password
btn_generate = tk.Button(window, text="Generate Password", command=generate_password, bg="lightblue")
btn_generate.grid(row=4, column=0, columnspan=2, pady=10)

# Label to display the generated password
label_result = tk.Label(window, text="Generated Password: ", font=("Arial", 14))
label_result.grid(row=5, column=0, columnspan=2, pady=10)

# Button to copy the password to clipboard
btn_copy = tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard, bg="lightgreen")
btn_copy.grid(row=6, column=0, columnspan=2, pady=10)

# Label to show the clipboard status
label_copy_status = tk.Label(window, text="", font=("Arial", 10))
label_copy_status.grid(row=7, column=0, columnspan=2, pady=5)

# Run the Tkinter event loop
window.mainloop()
