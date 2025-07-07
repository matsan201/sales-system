
import tkinter as tk
from tkinter import Label, Button, messagebox

class Sales(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.config(bg="#C6D9E3")
        self.create_interface()
        
    def create_interface(self):
        """Crea la interfaz para el módulo de ventas"""
        # Título
        title_label = Label(
            self,
            text="MÓDULO DE VENTAS",
            font=("Arial", 18, "bold"),
            bg="#C6D9E3",
            fg="#2C3E50"
        )
        title_label.pack(pady=20)
        
        # Mensaje informativo
        info_label = Label(
            self,
            text="Esta sección estará disponible próximamente.\nAquí podrás registrar ventas, calcular totales y generar tickets.",
            font=("Arial", 12),
            bg="#C6D9E3",
            fg="#7F8C8D",
            justify=tk.CENTER
        )
        info_label.pack(pady=30)
        
        # Botón de ejemplo
        example_button = Button(
            self,
            text="Ejemplo: Nueva Venta",
            command=self.example_sale,
            font=("Arial", 12, "bold"),
            bg="#27AE60",
            fg="white",
            width=20,
            height=2,
            cursor="hand2"
        )
        example_button.pack(pady=20)
        
    def example_sale(self):
        """Función de ejemplo para mostrar funcionalidad"""
        messagebox.showinfo("Ventas", "¡Funcionalidad de ventas en desarrollo!\n\nPróximamente podrás:\n• Registrar productos\n• Calcular totales\n• Generar tickets\n• Procesar pagos")
