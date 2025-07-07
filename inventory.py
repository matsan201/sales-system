
import tkinter as tk
from tkinter import Label, Button, messagebox

class Inventory(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.config(bg="#C6D9E3")
        self.create_interface()
        
    def create_interface(self):
        """Crea la interfaz para el módulo de inventario"""
        # Título
        title_label = Label(
            self,
            text="GESTIÓN DE INVENTARIO",
            font=("Arial", 18, "bold"),
            bg="#C6D9E3",
            fg="#2C3E50"
        )
        title_label.pack(pady=20)
        
        # Mensaje informativo
        info_label = Label(
            self,
            text="Esta sección estará disponible próximamente.\nAquí podrás gestionar productos, stock y precios.",
            font=("Arial", 12),
            bg="#C6D9E3",
            fg="#7F8C8D",
            justify=tk.CENTER
        )
        info_label.pack(pady=30)
        
        # Botones de ejemplo
        buttons_frame = tk.Frame(self, bg="#C6D9E3")
        buttons_frame.pack(pady=20)
        
        add_button = Button(
            buttons_frame,
            text="Agregar Producto",
            command=self.example_add,
            font=("Arial", 12, "bold"),
            bg="#3498DB",
            fg="white",
            width=15,
            height=2,
            cursor="hand2"
        )
        add_button.pack(side=tk.LEFT, padx=10)
        
        view_button = Button(
            buttons_frame,
            text="Ver Inventario",
            command=self.example_view,
            font=("Arial", 12, "bold"),
            bg="#9B59B6",
            fg="white",
            width=15,
            height=2,
            cursor="hand2"
        )
        view_button.pack(side=tk.LEFT, padx=10)
        
    def example_add(self):
        """Función de ejemplo para agregar productos"""
        messagebox.showinfo("Inventario", "¡Funcionalidad de inventario en desarrollo!\n\nPróximamente podrás:\n• Agregar nuevos productos\n• Editar información de productos\n• Controlar stock\n• Gestionar precios")
        
    def example_view(self):
        """Función de ejemplo para ver inventario"""
        messagebox.showinfo("Inventario", "Lista de productos:\n\n• Esta funcionalidad mostrará todos los productos\n• Con información de stock y precios\n• Opciones de búsqueda y filtrado")