import cv2
from tkinter import filedialog, messagebox

def decrypt_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if not file_path:
        messagebox.showwarning("Warning", "Please select an encrypted image.")
        return

    password = input("Enter the passcode: ")
    if not password:
        messagebox.showwarning("Warning", "Passcode cannot be empty.")
        return

    img = cv2.imread(file_path)
    if img is None:
        messagebox.showerror("Error", "Error loading the image.")
        return

    # Read message length from the first pixel
    msg_length = img[0, 0, 0]

    # Retrieve encrypted bytes
    encrypted_bytes = bytearray([img[i, 0, 0] for i in range(1, msg_length + 1)])

    # Decrypt using XOR
    password_bytes = password.encode('utf-8')
    decrypted_bytes = bytearray([encrypted_bytes[i] ^ password_bytes[i % len(password_bytes)] for i in range(len(encrypted_bytes))])

    decrypted_message = decrypted_bytes.decode('utf-8')
    messagebox.showinfo("Decrypted Message", f"Message: {decrypted_message}")
