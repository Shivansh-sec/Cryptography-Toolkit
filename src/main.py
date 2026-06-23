import tkinter as tk

from src.gui import CryptoGUI


def main():

    root = tk.Tk()

    CryptoGUI(root)

    root.mainloop()


if __name__ == "__main__":
    main()