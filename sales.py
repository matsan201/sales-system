from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox

class Sales(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.widgets()

    def widgets(self):
        frame1 = tk.Frame(self, bg="#dddddd", highlightbackground="gray", highlightthickness=1)
        frame1.pack()
        frame1.place(x=0, y=0, width=1100, height=100)

        title = tk.Label(self, text="Ventas", bg="#dddddd", font="sans 30 bold")
        title.pack()
        title.place(x=5, y=0, width=1090, height=90)

        frame2 = tk.Frame(self, bg="#C6D9E3", highlightbackground="gray", highlightthickness=1)
        frame2.place(x=0, y=100, width=1100, height=550)

        lbl_frame = LabelFrame(frame2, text="Informacion de la venta", bg="#C6D8E3", font="sans 16 bold")
        lbl_frame.place(x=10, y=10, width=1060, height=80)

        label_invoice_number = tk.Label(lbl_frame, text="Numero de \nfactura: ", bg="#C6D9E3", font="sans 10 bold")
        label_invoice_number.place(x=10, y=5)
        self.invoice_number = tk.StringVar()
        self.entry_invoice_number = ttk.Entry(lbl_frame, textvariable=self.invoice_number, state="readonly", font="sans 10 bold")
        self.entry_invoice_number.place(x=100, y=5, width=80)

        label_name = tk.Label(lbl_frame, text="Productos: ", bg="#C6D9E3", font="sans 10 bold")
        label_name.place(x=200, y=12)
        self.entry_name = ttk.Entry(lbl_frame, font="sans 10 bold")
        self.entry_name.place(x=280, y=10, width=180)

        label_value = tk.Label(lbl_frame, text="Precio: ", bg="#C6D9E3", font="sans 10 bold")
        label_value.place(x=470,y=12)
        self.entry_value = ttk.Entry(lbl_frame, font="sans 10 bold", state="readonly")
        self.entry_value.place(x=540, y=10, width=180)

        label_amount = tk.Label(lbl_frame, text="Cantidad: ", bg="#C6D9E3", font="sans 10 bold")
        label_amount.place(x=730, y=12)
        self.entry_amount = ttk.Entry(lbl_frame, font="sans 10 bold")
        self.entry_amount.place(x=820, y=10)

        treFrame = tk.Frame(frame2, bg="#C6D9E3")
        treFrame.place(x=150, y=120, width=800, height=200)

        scroll_y = ttk.Scrollbar(treFrame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x = ttk.Scrollbar(treFrame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)

        self.tree = ttk.Treeview(treFrame, columns=("Producto", "Precio", "Cantidad", "Subtotal"), show="headings", height=10, yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_y.config(command=self.tree.yview)
        scroll_x.config(command=self.tree.xview)

        self.tree.heading("#1", text="Producto")
        self.tree.heading("#2", text="Precio")
        self.tree.heading("#3", text="Cantidad")
        self.tree.heading("#4", text="Subtotal")

        self.tree.column("Producto", anchor="center")
        self.tree.column("Precio", anchor="center")
        self.tree.column("Cantidad", anchor="center")
        self.tree.column("Subtotal", anchor="center")

        self.tree.pack(expand=True, fill=BOTH)

        lbl_frame1 = LabelFrame(frame2, text="Opciones",  bg="#C6D9E3", font="sans 10 bold")
        lbl_frame1.place(x=10, y=380, width=1060, height=100)

        button_add = tk.Button(lbl_frame1, text="Agregar Articulo", bg="#C6D9E3", font="sans 16 bold")
        button_add.place(x=50, y=10, width=240, height=50)

        button_pay = tk.Button(lbl_frame1, text="Pagar", bg="#C6D9E3", font="sans 16 bold")
        button_pay.place(x=400, y=10, width=240, height=50)

        button_show_invoice = tk.Button(lbl_frame1, text="Ver factura", bg="#C6D9E3", font="sans 16 bold")
        button_show_invoice.place(x=750, y=10, width=240, height=50)


