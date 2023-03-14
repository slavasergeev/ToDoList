'''from tkinter import *
root = Tk()

my_entry = Entry(root, width=50)
my_entry.pack()
my_entry.insert(0, "Place Holder")
my_entry.configure(state=DISABLED)

def on_click(event):
    my_entry.configure(state=NORMAL)
    my_entry.delete(0, END)

    # make the callback only work once
    my_entry.unbind('<Button-1>', on_click_id)

on_click_id = my_entry.bind('<Button-1>', on_click)

root.mainloop()'''

import tkinter as tk

class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey'):
        super().__init__(master)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()

if __name__ == "__main__":
    root = tk.Tk()
    username = EntryWithPlaceholder(root, "username")
    password = EntryWithPlaceholder(root, "password", 'blue')
    username.pack()
    password.pack()
    root.mainloop()
