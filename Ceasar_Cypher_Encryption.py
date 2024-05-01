
import tkinter as tk
from tkinter import messagebox

# Function for encrypting a message using Caesar Cipher with a given shift value
def caesar_cipher_encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

# Function for decrypting an encrypted message using Caesar Cipher with a given shift value
def caesar_cipher_decrypt(encrypted_message, shift):
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message

# Function for encrypting the mes0sage when the "Encrypt" button is clicked
def encrypt_message():
    message = message_entry.get()
    shift = int(shift_entry.get())
    encrypted_message = caesar_cipher_encrypt(message, shift)
    encrypted_message_label.config(text=encrypted_message)

# Function for decrypting the encrypted message when the "Decrypt" button is clicked
def decrypt_message():
    encrypted_message = encrypted_message_entry.get()
    shift = int(shift_entry.get())
    decrypted_message = caesar_cipher_decrypt(encrypted_message, shift)
    decrypted_message_label.config(text=decrypted_message)

# Create the main application window
app = tk.Tk()
app.title("Caesar Cipher")

# Create a label and input field for the message
message_label = tk.Label(app, text="Message:")
message_label.grid(row=0, column=0)
message_entry = tk.Entry(app)
message_entry.grid(row=0, column=1)

# Create a label and input field for the shift value
shift_label = tk.Label(app, text="Shift:")
shift_label.grid(row=1, column=0)
shift_entry = tk.Entry(app)
shift_entry.grid(row=1, column=1)

# Create a button for encrypting the message
encrypt_button = tk.Button(app, text="Encrypt", command=encrypt_message)
encrypt_button.grid(row=2, column=0)

# Create a label for displaying the encrypted message
encrypted_message_label = tk.Label(app, text="")
encrypted_message_label.grid(row=2, column=1)

# Create a label for displaying the decrypted message
decrypted_message_label = tk.Label(app, text="")
decrypted_message_label.grid(row=3, column=1)

# Create a button for decrypting the encrypted message
decrypt_button = tk.Button(app, text="Decrypt", command=decrypt_message)
decrypt_button.grid(row=4, column=0)

# Create an input field for the encrypted message
encrypted_message_entry = tk.Entry(app)
encrypted_message_entry.grid(row=4, column=1)

# Start the main event loop
app.mainloop()