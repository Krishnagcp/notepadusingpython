# Creating a notepad by using tkinter which is a GUI library provided by python for creating GUI applications

# step 1 : importing necessary library and module
import tkinter as tk
from tkinter import filedialog


# step 2 : initiating class "Notepad" with arguments
class Notepad(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # step 3 : Set the title for the notepad
        self.title("Notepad")

        # step 4 : Create a text widget
        self.text = tk.Text(self, wrap="word")
        self.text.pack(side="top", fill="both", expand=True)

        # step 5 : Create a menu bar
        self.menu = tk.Menu(self)
        self.config(menu=self.menu)

        # step 6 : Create a file menu
        file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=file_menu)  # add_cascade method will create a hierarchical menu
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)

        # step 7 : Create an Edit menu
        edit_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Cut", command=self.cut)
        edit_menu.add_command(label="Copy", command=self.copy)
        edit_menu.add_command(label="Paste", command=self.paste)

    # step 8 :Defining new_file method
    def new_file(self):
        self.text.delete("1.0", "end")
        self.title("Notepad")

    # step 9 : defining the method open_file
    def open_file(self):
        file = filedialog.askopenfile(parent=self, mode="rb", title="Open a file")
        if file:
            contents = file.read
            self.text.delete("1.0", "end")
            self.text.insert("1.0", contents)
            file.close()
            self.title(file.name + "-Notepad")

    # step 10 : Defining the method save_file
    def save_file(self):
        file = filedialog.asksaveasfile(mode="w", defaultextension=".txt",
                                        filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
        if file:
            contents = self.text.get("1.0", "end")
            file.write(contents)
            file.close()
            self.title(file.name + "-Notepad")

    # step 11 : Defining the method cut
    def cut(self):
        self.text.event_generate("<<Cut>>")

    # step 12 : defining the method copy
    def copy(self):
        self.text.event_generate("<<Copy>>")

    # step 13 : Defining the method Paste
    def paste(self):
        self.text.event_generate("<<Paste>>")


if __name__ == "__main__":
    notepad = Notepad()
    notepad.mainloop()
