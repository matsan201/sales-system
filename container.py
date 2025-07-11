from tkinter import  *
import  tkinter as tk
from sales import Sales
from inventory import Inventory

class Container(tk.Frame):
    def __init__(self, father, controller):
        super().__init__(father)
        self.controller = controller
        self.pack()
        self.place(x=0, y=0, width=800, height=400)
        self.config(bg="#C6D9E3")

    def show_frames(self, container):
        top_level = tk.Toplevel(self)
        frame = container(top_level)
        frame.config(bg="#C6D9E3")
        frame.pack(fill="both", expand=True)
        top_level.geometry("1100x650+120+20")
        top_level.resizable(False, False)

    def sales(self):
        self.show_frames(Sales)

    def inventory(self):
        self.show_frames(Inventory)