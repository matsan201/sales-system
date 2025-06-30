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
        self.widgets()

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

    def widgets(self):
        frame1 = tk.Frame(self, bg="#C6D9E3")
        frame1.pack()
        frame1.place(x=0, y=0, width=800, height=400)

        btn_sales = Button(frame1, bg="green", fg="black", text="Ir a ventas", command=self.sales)
        btn_sales.place(x=500, y=30, width=240, height=60)

        btn_inventory = Button(frame1, bg="green", fg="white", text="Ir a Inventario", command=self.inventory)
        btn_inventory.place(x=500, y=130, width=240, height=60)

