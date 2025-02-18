from tkinter import *
from tkinter import ttk
import encrypt
import decrypt

class ImageEncryptDecryptApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Encryption & Decryption")
        self.root.geometry("500x300")
        self.root.configure(bg="#F4F4F4")

        self.style = ttk.Style()
        self.style.configure("TButton", font=("Arial", 12), padding=5)
        self.style.configure("TLabel", font=("Arial", 12))

        ttk.Label(root, text="Select an option:", font=("Arial", 14)).pack(pady=20)

        self.btnEncrypt = ttk.Button(root, text="Encrypt Image", command=encrypt.encrypt_image)
        self.btnEncrypt.pack(pady=10)

        self.btnDecrypt = ttk.Button(root, text="Decrypt Image", command=decrypt.decrypt_image)
        self.btnDecrypt.pack(pady=10)

if __name__ == "__main__":
    root = Tk()
    app = ImageEncryptDecryptApp(root)
    root.mainloop()
