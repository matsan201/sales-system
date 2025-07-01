from tkinter import *
import tkinter as tk
from tkinter import  ttk, messagebox



class Inventory(tk.Frame):
    def __init__(self, father):
        super().__init__(father)
        self.pack()
        self.widgets()


    def widgets(self):
        frame1 = tk.Frame(self, bg="#dddddd", highlightbackground="gray", highlightthickness=1)
        frame1.pack()
        frame1.place(x=0, y=0, width=1100, height=100)

        title = tk.Label(self, text="Inventarios", bg="#dddddd",  font="sans 30 bold", anchor="center")
        title.pack()
        title.place(x=5, y=0, width=1090, height=90)

        frame2 = tk.Frame(self, bg="#C6D9E3", highlightbackground="gray", highlightthickness=1)
        frame2.place(x=0, y=100, width=1100, height=550)

        label_frame = LabelFrame(frame2, text="Productos", font="sans 20 bold", bg="#C6D9E3")
        label_frame.place(x=20, y=30, width=400, height=500)

        lbl_name = Label(label_frame, text="Nombre: ", font="sans 12 bold", bg="#C6D9E3")
        lbl_name.place(x=10, y=20)
        self.name = ttk.Entry(label_frame, font="sans 12 bold")
        self.name.place(x=140, y=20, width=240, height=40)

        lbl_supplier = Label(label_frame, text="Proveedor: ", font="sans 12 bold", bg="#C6D9E3")
        lbl_supplier.place(x=10, y=80)
        self.supplier = ttk.Entry(label_frame, font="sans 12 bold")
        self.supplier.place(x=140, y=80, width=240, height=40)

        lbl_price = Label(label_frame, text="Precio: ", font="sans 12 bold", bg="#C6D9E3")
        lbl_price.place(x=10, y=140)
        self.price = ttk.Entry(label_frame, font="sans 12 bold")
        self.price.place(x=140, y=140, width=240, height=40)

        lbl_cost = Label(label_frame, text="Costo: ", font="sans 12 bold", bg="#C6D9E3")
        lbl_cost.place(x=10, y=200)
        self.cost = ttk.Entry(label_frame, font="sans 12 bold")
        self.cost.place(x=140, y=200, width=240, height=40)

        lbl_stock = Label(label_frame, text="Stock: ", font="sans 12 bold", bg="#C6D9E3")
        lbl_stock.place(x=10, y=260)
        self.stock = ttk.Entry(label_frame, font="sans 12 bold")
        self.stock.place(x=140, y=260, width=240, height=40)

        button_add = tk.Button(label_frame, text="Ingresar", font="sans 12 bold", bg="#dddddd")
        button_add.place(x=80, y=340, width=240, height=40)

        button_edit = tk.Button(label_frame, text="Editar", font="sans 12 bold", bg="#dddddd")
        button_edit.place(x=80, y=400, width=240, height=40)

        #Tabla
        treFrame = Frame(frame2, bg="white")
        treFrame.place(x=440, y=50, width=620, height=400)

        scroll_y = ttk.Scrollbar(treFrame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x = ttk.Scrollbar(treFrame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)

        self.tre = ttk.Treeview(treFrame,yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set, height=40, columns=("ID", "PRODUCTO", "PROVEEDOR", "PRECIO", "COSTO", "STOCK"), show="headings")
        self.tre.pack(expand=True, fill=BOTH)

        scroll_y.config(command=self.tre.yview)
        scroll_x.config(command=self.tre.xview)

        self.tre.heading("ID", text="Id")
        self.tre.heading("PRODUCTO", text="Producto")
        self.tre.heading("PROVEEDOR", text="Proveedor")
        self.tre.heading("PRECIO", text="Precio")
        self.tre.heading("COSTO", text="Costo")
        self.tre.heading("STOCK", text="Stock")

        self.tre.column("ID", width=70, anchor="center")
        self.tre.column("PRODUCTO", width=70, anchor="center")
        self.tre.column("PROVEEDOR", width=70, anchor="center")
        self.tre.column("PRECIO", width=70, anchor="center")
        self.tre.column("COSTO", width=70, anchor="center")
        self.tre.column("STOCK", width=70, anchor="center")
