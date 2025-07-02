import sqlite3

from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox

class Sales(tk.Frame):
    db_name = "salessystem.db"

    def __init__(self, parent):
        super().__init__(parent)
        self.invoice_number_current = self.get_current_invoice_number()
        self.widgets()
        self.show_invoice_number()

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
        self.entry_name = ttk.Combobox(lbl_frame, font="sans 10 bold", state="readonly")
        self.entry_name.place(x=280, y=10, width=180)

        self.upload_product()

        label_value = tk.Label(lbl_frame, text="Precio: ", bg="#C6D9E3", font="sans 10 bold")
        label_value.place(x=470,y=12)
        self.entry_value = ttk.Entry(lbl_frame, font="sans 10 bold", state="readonly")
        self.entry_value.place(x=540, y=10, width=180)

        self.entry_name.bind("<<ComboboxSelected>>", self.update_price)

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

        button_add = tk.Button(lbl_frame1, text="Agregar Articulo", bg="#C6D9E3", font="sans 16 bold", command=self.register)
        button_add.place(x=50, y=10, width=240, height=50)

        button_pay = tk.Button(lbl_frame1, text="Pagar", bg="#C6D9E3", font="sans 16 bold", command=self.open_payment_window)
        button_pay.place(x=400, y=10, width=240, height=50)

        button_show_invoice = tk.Button(lbl_frame1, text="Ver factura", bg="#C6D9E3", font="sans 16 bold", command=self.open_bill_window)
        button_show_invoice.place(x=750, y=10, width=240, height=50)

        self.label_total_sum = tk.Label(frame2, text="Total a pagar: ARS 0", bg="#C6D9E3", font="sans 25 bold")
        self.label_total_sum.place(x=360, y=335)

    def upload_product(self):
        try:
            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()
            c.execute("SELECT name FROM inventory")
            products = c.fetchall()
            self.entry_name["values"] = [product[0] for product in products]
            if not products:
                print("No se encontraron productos en la base de datos.")
            conn.close()
        except sqlite3.Error as e:
            print("Error al cargar productos desde la base de datos: ", e)

    def update_price(self, event):
        name_product = self.entry_name.get()
        try:
            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()
            c.execute("SELECT price FROM inventory WHERE name = ?", (name_product,))
            price = c.fetchone()
            if (price):
                self.entry_value.config(state="normal")
                self.entry_value.delete(0, tk.END)
                self.entry_value.insert(0, price[0])
                self.entry_value.config(state="readonly")
            else:
                self.entry_value.config(state="normal")
                self.entry_value.delete(0, tk.END)
                self.entry_value.insert(0, "Precio no disponible")
                self.entry_value.config(state="readonly")
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al obtener el precio: {e}")
        finally:
            conn.close()

    def update_total(self):
        total = 0.0
        for child in self.tree.get_children():
            subtotal = float(self.tree.item(child, "values") [3])
            total += subtotal
        self.label_total_sum.config(text=f"Total a pagar: ARS {total:.0f}")

    def register(self):
        product = self.entry_name.get()
        price = self.entry_value.get()
        amount = self.entry_amount.get()

        if product and price and amount:
            try:
                amount = int(amount)
                if not self.check_stock(product, amount):
                    messagebox.showerror("Error", "Stock insuficiente para el producto selecionado")
                    return
                price = float(price)
                subtotal = amount * price

                self.tree.insert("", "end", values=(product, f"{price:.0f}", amount, f"{subtotal:.0f}"))

                self.entry_name.set("")
                self.entry_value.config(state="normal")
                self.entry_value.delete(0, tk.END)
                self.entry_value.config(state="readonly")
                self.entry_amount.delete(0, tk.END)

                self.update_total()
            except ValueError:
                messagebox.showerror("Error", "Cantidad o precio no validos")
        else:
            messagebox.showerror("Error", "Debe completar todos los campos")

    def check_stock(self, name_product, amount):
        try:
            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()
            c.execute("SELECT stock FROM inventory WHERE name = ?", (name_product,))
            stock = c.fetchone()
            if stock and stock[0] >= amount:
                return True
            return False
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al verificar el stock: {e}")
            return False
        finally:
            conn.close()

    def get_total(self):
        total = 0.0
        for child in self.tree.get_children():
            subtotal = float(self.tree.item(child, "values") [3])
            total += subtotal
        return total

    def open_payment_window(self):
        if not self.tree.get_children():
            messagebox.showerror("Error", "No hay articulos para pagar")
            return

        payment_window = Toplevel(self)
        payment_window.title("Realizar Pago")
        payment_window.geometry("400x400")
        payment_window.config(bg="#C6D9E3")
        payment_window.resizable(False, False)

        label_total = tk.Label(payment_window, bg="#C6D9E3", text=f"Total a pagar: ARS {self.get_total():.0f}", font="sans 16 bold")
        label_total.place(x=70, y=20)

        label_amount_paid = tk.Label(payment_window, bg="#C6D9E3", text="Cantidad pagada", font="sans 14 bold")
        label_amount_paid.place(x=100, y=90)
        entry_amount_paid = ttk.Entry(payment_window, font="sans 14 bold")
        entry_amount_paid.place(x=100, y=130)

        label_change = tk.Label(payment_window, bg="#C6D9E3", text="", font="sans 14 bold")
        label_change.place(x=100, y=190)

        def calculate_change():
            try:
                amount_paid = float(entry_amount_paid.get())
                total = self.get_total()
                change = amount_paid - total
                if change < 0:
                    messagebox.showerror("Error", "La cantidad pagada es insuficiente")
                    return
                label_change.config(text=f"Vuelto: ARS {change:.0f}")
            except ValueError:
                messagebox.showerror("Error", "Cantidad pagada no valida")

        button_calculate = tk.Button(payment_window, text="Calcular vuelto", bg="white", font="sans 12 bold", command=calculate_change)
        button_calculate.place(x=100, y=240, width=240, height=40)

        button_pay = tk.Button(payment_window, text="Pagar", bg="white", font="sans 12 bold", command=lambda: self.pay(payment_window, entry_amount_paid, label_change))
        button_pay.place(x=100, y=300, width=240, height=40)

    def pay(self, payment_window, entry_amount_paid, label_change):
        try:
            amount_paid = float(entry_amount_paid.get())
            total = self.get_total()
            change = amount_paid - total
            if change <0 :
                messagebox.showerror("Error", "La cantidad pagada es insuficiente")
                return

            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()
            try:
                for child in self.tree.get_children():
                    item = self.tree.item(child, "values")
                    name_product = item[0]
                    quantity_sold = int(item[2])
                    if not self.check_stock(name_product, quantity_sold):
                        messagebox.showerror("Error", f"Stock insuficiente para el producto: {name_product}")
                        return
                    c.execute("INSERT INTO sales (bill, name_article, value_article, amount, subtotal) VALUES(?,?,?,?,?)"
                              , (self.invoice_number_current, name_product, float(item[1]), quantity_sold, float(item[3])))
                    c.execute("UPDATE inventory SET stock = stock - ? WHERE name = ?", (quantity_sold, name_product,))

                conn.commit()
                messagebox.showinfo("Exito", "Venta registrada exitosamente")

                self.invoice_number_current += 1
                self.show_invoice_number()

                for child in self.tree.get_children():
                    self.tree.delete(child)
                self.label_total_sum.config(text="Total a pagar: ARS 0")

                payment_window.destroy()
            except sqlite3.Error as e:
                conn.rollback()
                messagebox.showerror("Error", f"Error al registrar la venta: {e}")
            finally:
                conn.close()
        except ValueError:
            messagebox.showerror("Error", "Cantidad pagada no valida")

    def get_current_invoice_number(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        try:
            c.execute("SELECT MAX(bill) FROM sales")
            max_invoice = c.fetchone()[0]
            if max_invoice:
                return max_invoice + 1
            else:
                return 1
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al obtener el numero de factura: {e}")
            return 1
        finally:
            conn.close()

    def show_invoice_number(self):
        self.invoice_number.set(self.invoice_number_current)

    def open_bill_window(self):
        bill_window = Toplevel(self)
        bill_window.title("Factura")
        bill_window.geometry("800x500")
        bill_window.config(bg="#C6D8E3")
        bill_window.resizable(False, False)

        bills = Label(bill_window, bg="#C6D8E3", text="facturas registradas", font="sans 36 bold")
        bills.place(x=150, y=15)

        treFrame = tk.Frame(bill_window, bg="#C6D8E3")
        treFrame.place(x=10, y=100, width=780, height=380)

        scroll_y = ttk.Scrollbar(treFrame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x = ttk.Scrollbar(treFrame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)

        tree_invoices = ttk.Treeview(treFrame, columns=("ID", "Factura", "Producto", "Precio", "Cantidad", "Subtotal"), show="headings", height=10, yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        scroll_y.config(command=self.tree.yview)
        scroll_x.config(command=self.tree.xview)

        tree_invoices.heading("#1", text="ID")
        tree_invoices.heading("#2", text="Factura")
        tree_invoices.heading("#3", text="Producto")
        tree_invoices.heading("#4", text="Precio")
        tree_invoices.heading("#5", text="Cantidad")
        tree_invoices.heading("#6", text="Subtotal")

        tree_invoices.column("ID", width=70, anchor="center")
        tree_invoices.column("Factura", width=100, anchor="center")
        tree_invoices.column("Producto", width=200, anchor="center")
        tree_invoices.column("Precio", width=130, anchor="center")
        tree_invoices.column("Cantidad", width=130, anchor="center")
        tree_invoices.column("Subtotal", width=130, anchor="center")

        tree_invoices.pack(expand=True, fill=BOTH)

        self.upload_invoices(tree_invoices)

    def upload_invoices(self, tree):
        try:
            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()
            c.execute("SELECT id, bill, name_article, value_article, amount, subtotal FROM sales")
            invoices = c.fetchall()
            for invoice in invoices:
                tree.insert("", "end", values=invoice)
            conn.close()
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al cargar las facturas: {e}")


