import tkinter as tk
from tkinter import Button, Label
from sales import Sales
from inventory import Inventory

class Container(tk.Frame):
    def __init__(self, father, controller):
        super().__init__(father)
        self.controller = controller
        self.pack()
        self.place(x=0, y=0, width=800, height=370)  # Ajustado por la barra de usuario
        self.config(bg="#C6D9E3")
        
        # Crear la interfaz principal
        self.create_main_interface()
        
    def create_main_interface(self):
        """Crea la interfaz principal con botones de navegación"""
        # Título principal
        title_label = Label(
            self,
            text="SISTEMA DE PUNTO DE VENTA",
            font=("Arial", 20, "bold"),
            bg="#C6D9E3",
            fg="#2C3E50"
        )
        title_label.pack(pady=30)
        
        # Frame para los botones principales
        buttons_frame = tk.Frame(self, bg="#C6D9E3")
        buttons_frame.pack(expand=True)
        
        # Botón de Ventas
        sales_button = Button(
            buttons_frame,
            text="💰 REALIZAR VENTA",
            command=self.sales,
            font=("Arial", 14, "bold"),
            bg="#27AE60",
            fg="white",
            width=20,
            height=3,
            relief="raised",
            bd=3,
            cursor="hand2"
        )
        sales_button.pack(pady=15)
        
        # Botón de Inventario
        inventory_button = Button(
            buttons_frame,
            text="📦 GESTIONAR INVENTARIO",
            command=self.inventory,
            font=("Arial", 14, "bold"),
            bg="#3498DB",
            fg="white",
            width=20,
            height=3,
            relief="raised",
            bd=3,
            cursor="hand2"
        )
        inventory_button.pack(pady=15)
        
        # Información del usuario actual
        user_info = f"Sesión iniciada como: {getattr(self.controller, 'current_user', 'Usuario')}"
        user_label = Label(
            self,
            text=user_info,
            font=("Arial", 10),
            bg="#C6D9E3",
            fg="#7F8C8D"
        )
        user_label.pack(side="bottom", pady=10)

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