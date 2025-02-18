import cv2
import os
from tkinter import filedialog, messagebox

def encrypt_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if not file_path:
        messagebox.showwarning("Warning", "Please select an image.")
        return

    msg = input("Enter the secret message: ")
    password = input("Enter the passcode: ")

    if not msg or not password:
        messagebox.showwarning("Warning", "Message and passcode cannot be empty.")
        return

    img = cv2.imread(file_path)
    if img is None:
        messagebox.showerror("Error", "Error loading the image.")
        return

    # Convert message to binary using XOR encryption
    message_bytes = msg.encode('utf-8')
    password_bytes = password.encode('utf-8')
    encrypted_bytes = bytearray([message_bytes[i] ^ password_bytes[i % len(password_bytes)] for i in range(len(message_bytes))])

    # Embed message length in the first pixel
    img[0, 0, :3] = [len(encrypted_bytes), 0, 0]

    # Embed message in the image
    index = 0
    for i in range(1, len(encrypted_bytes) + 1):
        img[i, 0, 0] = encrypted_bytes[index]
        index += 1

    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if save_path:
        cv2.imwrite(save_path, img)
        messagebox.showinfo("Success", f"Image encrypted and saved as {save_path}")
