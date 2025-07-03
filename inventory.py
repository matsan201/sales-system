import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import  ttk, messagebox



class Inventory(tk.Frame):
    db_name = "salessystem.db"

    def __init__(self, father):
        super().__init__(father)
        self.pack()
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
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

        button_add = tk.Button(label_frame, text="Ingresar", font="sans 12 bold", bg="#dddddd", command=self.register)
        button_add.place(x=80, y=340, width=240, height=40)

        button_edit = tk.Button(label_frame, text="Editar", font="sans 12 bold", bg="#dddddd", command=self.edit_product)
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

        self.show()

        btn_update = Button(frame2, text="Actualizar Inventario", font="sans 14 bold", command=self.update_inventory)
        btn_update.place(x=440, y=480, width=260, height=50)


    def execute_query(self, query, paremeters=()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, paremeters)
            conn.commit()
        return result

    def validation(self, name, supplier, price, cost, stock):
        if not (name and supplier and price and cost and stock):
            return False
        try:
            float(price)
            float(cost)
            int(stock)
        except ValueError:
            return False
        return True

    def show(self):
        query = "SELECT id, name, supplier, price, cost, stock FROM inventory ORDER BY id DESC"
        result = self.execute_query(query)
        for element in result:
            try:
                price_ars = "{:,.0f} ARS".format(float(element[3])) if element[3] else ""
                cost_ars = "{:,.0f} ARS".format(float(element[4])) if element[4] else ""
            except ValueError:
                price_ars = element[3]
                cost_ars = element[4]
            self.tre.insert("", 0, text=element[0], values=(element[0], element[1], element[2], price_ars, cost_ars, element[5]))

    def update_inventory(self):
        for item in self.tre.get_children():
            self.tre.delete(item)

        self.show()

        messagebox.showinfo("Actualizacion", "El inventario ha sido actualizado correctamente")

    def register(self):
        result = self.tre.get_children()
        for index in result:
            self.tre.delete(index)
        name = self.name.get()
        supplier = self.supplier.get()
        price = self.price.get()
        cost = self.cost.get()
        stock = self.stock.get()
        if  self.validation(name, supplier, price, cost, stock):
            try:
                query = "INSERT INTO inventory VALUES(?,?,?,?,?,?)"
                paremeters = (None, name, supplier, price, cost, stock)
                self.execute_query(query, paremeters)
                self.show()
                self.name.delete(0, END)
                self.supplier.delete(0, END)
                self.price.delete(0, END)
                self.cost.delete(0, END)
                self.stock.delete(0, END)
            except Exception as e:
                messagebox.showwarning("Error", message=f"Error al registrar el producto: {e}")
        else:
            messagebox.showwarning("Error", "Rellene todos los campos correctamente")
            self.show()

    def edit_product(self):
        selection = self.tre.selection()
        if not selection:
            messagebox.showwarning("Editar producto", "Seleccione un producto para editar")
            return

        item_id = self.tre.item(selection)["text"]
        item_values = self.tre.item(selection)["values"]

        edit_window = Toplevel(self)
        edit_window.title("Editar producto")
        edit_window.geometry("400x400")
        edit_window.config(bg="#C6D9E3")

        lbl_name = Label(edit_window, text="Nombre: ", font="sans 12 bold", bg="#C6D9E3")
        lbl_name.grid(row=0, column=0, padx=10, pady=10)
        entry_name = Entry(edit_window, font="sans 12 bold")
        entry_name.grid(row=0, column=1, padx=10, pady=10)
        entry_name.insert(0, item_values[1])

        lbl_supplier = Label(edit_window, text="Proveedor: ", font="sans 12 bold", bg="#C6D9E3")
        lbl_supplier.grid(row=1, column=0, padx=10, pady=10)
        entry_supplier = Entry(edit_window, font="sans 12 bold")
        entry_supplier.grid(row=1, column=1, padx=10, pady=10)
        entry_supplier.insert(0, item_values[2])

        lbl_price = Label(edit_window, text="Precio: ", font="sans 12 bold", bg="#C6D9E3")
        lbl_price.grid(row=2, column=0, padx=10, pady=10)
        entry_price = Entry(edit_window, font="sans 12 bold")
        entry_price.grid(row=2, column=1, padx=10, pady=10)
        entry_price.insert(0, item_values[3].split()[0].replace(",", ""))

        lbl_cost = Label(edit_window, text="Costo: ", font="sans 12 bold", bg="#C6D9E3")
        lbl_cost.grid(row=3, column=0, padx=10, pady=10)
        entry_cost = Entry(edit_window, font="sans 12 bold")
        entry_cost.grid(row=3, column=1, padx=10, pady=10)
        entry_cost.insert(0, item_values[4].split()[0].replace(",", ""))

        lbl_stock = Label(edit_window, text="Stock: ", font="sans 12 bold", bg="#C6D9E3")
        lbl_stock.grid(row=4, column=0, padx=10, pady=10)
        entry_stock = Entry(edit_window, font="sans 12 bold")
        entry_stock.grid(row=4, column=1, padx=10, pady=10)
        entry_stock.insert(0, item_values[5])

        def save_changes():
            name = entry_name.get()
            supplier = entry_supplier.get()
            price = entry_price.get()
            cost = entry_cost.get()
            stock = entry_stock.get()

            if not (name and supplier and price and cost and stock):
                messagebox.showwarning("Guardar cambios", "Rellene todos los campos.")
                return
            try:
                price = float(price.replace(",", ""))
                cost= float(cost.replace(",", ""))
            except ValueError:
                messagebox.showwarning("Guardar cambios", "Ingrese valores numericos validos para precio y costo.")
                return
            query = "UPDATE inventory SET name = ?, supplier = ?, price = ?, cost = ?, stock = ? WHERE id = ?"
            paremeters = (name, supplier, price, cost, stock, item_id)
            self.execute_query(query, paremeters)

            self.update_inventory()

            edit_window.destroy()

        btn_save = Button(edit_window, text="Guardar cambios", font="sans 12 bold", command=save_changes)
        btn_save.place(x=80, y=250, width=240, height=40)



