import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from src.aes_module import AESModule
from src.rsa_module import RSAModule
from src.sha_module import SHAModule


class CryptoGUI:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "Cryptography Toolkit"
        )

        self.root.geometry(
            "1000x700"
        )

        self.root.configure(
            bg="#0f172a"
        )

        self.private_key = None
        self.public_key = None

        self.build_ui()

    def build_ui(self):

        title = tk.Label(
            self.root,
            text="CRYPTOGRAPHY TOOLKIT",
            font=("Consolas", 22, "bold"),
            bg="#0f172a",
            fg="#22c55e"
        )

        title.pack(pady=15)

        self.algorithm = tk.StringVar(
            value="AES"
        )

        algo_frame = tk.Frame(
            self.root,
            bg="#0f172a"
        )

        algo_frame.pack()

        ttk.Radiobutton(
            algo_frame,
            text="AES",
            variable=self.algorithm,
            value="AES"
        ).pack(side="left", padx=10)

        ttk.Radiobutton(
            algo_frame,
            text="RSA",
            variable=self.algorithm,
            value="RSA"
        ).pack(side="left", padx=10)

        ttk.Radiobutton(
            algo_frame,
            text="SHA-256",
            variable=self.algorithm,
            value="SHA"
        ).pack(side="left", padx=10)

        tk.Label(
            self.root,
            text="Input",
            bg="#0f172a",
            fg="white"
        ).pack(pady=(20, 5))

        self.input_box = tk.Text(
            self.root,
            height=8,
            bg="#111827",
            fg="white"
        )

        self.input_box.pack(
            fill="x",
            padx=20
        )

        tk.Label(
            self.root,
            text="Password / Key",
            bg="#0f172a",
            fg="white"
        ).pack(pady=(15, 5))

        self.key_entry = tk.Entry(
            self.root,
            width=80
        )

        self.key_entry.pack(
            padx=20
        )

        button_frame = tk.Frame(
            self.root,
            bg="#0f172a"
        )

        button_frame.pack(
            pady=20
        )

        tk.Button(
            button_frame,
            text="Encrypt",
            command=self.encrypt,
            bg="#22c55e"
        ).pack(
            side="left",
            padx=5
        )

        tk.Button(
            button_frame,
            text="Decrypt",
            command=self.decrypt,
            bg="#f59e0b"
        ).pack(
            side="left",
            padx=5
        )

        tk.Button(
            button_frame,
            text="Hash",
            command=self.hash_text,
            bg="#3b82f6"
        ).pack(
            side="left",
            padx=5
        )

        tk.Button(
            button_frame,
            text="Generate RSA Keys",
            command=self.generate_rsa_keys,
            bg="#ef4444"
        ).pack(
            side="left",
            padx=5
        )

        tk.Label(
            self.root,
            text="Output",
            bg="#0f172a",
            fg="white"
        ).pack(pady=(10, 5))

        self.output_box = tk.Text(
            self.root,
            height=12,
            bg="#111827",
            fg="#22c55e"
        )

        self.output_box.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

    def encrypt(self):

        try:

            text = self.input_box.get(
                "1.0",
                tk.END
            ).strip()

            algo = self.algorithm.get()

            if algo == "AES":

                password = (
                    self.key_entry.get()
                )

                result = AESModule.encrypt(
                    text,
                    password
                )

            elif algo == "RSA":

                if not self.public_key:

                    messagebox.showerror(
                        "Error",
                        "Generate RSA Keys First"
                    )

                    return

                result = RSAModule.encrypt(
                    text,
                    self.public_key
                )

            else:

                return

            self.output_box.delete(
                "1.0",
                tk.END
            )

            self.output_box.insert(
                tk.END,
                result
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    def decrypt(self):

        try:

            text = self.input_box.get(
                "1.0",
                tk.END
            ).strip()

            algo = self.algorithm.get()

            if algo == "AES":

                password = (
                    self.key_entry.get()
                )

                result = AESModule.decrypt(
                    text,
                    password
                )

            elif algo == "RSA":

                if not self.private_key:

                    messagebox.showerror(
                        "Error",
                        "Generate RSA Keys First"
                    )

                    return

                result = RSAModule.decrypt(
                    text,
                    self.private_key
                )

            else:

                return

            self.output_box.delete(
                "1.0",
                tk.END
            )

            self.output_box.insert(
                tk.END,
                result
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    def hash_text(self):

        try:

            text = self.input_box.get(
                "1.0",
                tk.END
            ).strip()

            result = (
                SHAModule.sha256_hash(
                    text
                )
            )

            self.output_box.delete(
                "1.0",
                tk.END
            )

            self.output_box.insert(
                tk.END,
                result
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    def generate_rsa_keys(self):

        try:

            (
                self.private_key,
                self.public_key
            ) = RSAModule.generate_keys()

            self.output_box.delete(
                "1.0",
                tk.END
            )

            self.output_box.insert(
                tk.END,
                "RSA Keys Generated Successfully"
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )