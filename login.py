import tkinter as tk
from tkinter import messagebox, ttk
import hashlib

class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Ventas - Login")
        self.geometry("400x300+500+200")
        self.resizable(False, False)
        self.configure(bg="#2C3E50")
        
        # Centrar la ventana
        self.center_window()
        
        # Variables
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()
        
        # Usuario y contraseña por defecto (en un proyecto real usarías una base de datos)
        self.users = {
            "admin": self.hash_password("admin123"),
            "cajero": self.hash_password("cajero123"),
            "gerente": self.hash_password("gerente123")
        }
        
        self.create_widgets()
        self.login_successful = False
        
    def center_window(self):
        """Centra la ventana en la pantalla"""
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")
        
    def hash_password(self, password):
        """Hashea la contraseña para mayor seguridad"""
        return hashlib.sha256(password.encode()).hexdigest()
        
    def create_widgets(self):
        """Crea los elementos de la interfaz de login"""
        # Frame principal
        main_frame = tk.Frame(self, bg="#2C3E50")
        main_frame.pack(expand=True, fill="both", padx=40, pady=40)
        
        # Título
        title_label = tk.Label(
            main_frame, 
            text="SISTEMA DE VENTAS", 
            font=("Arial", 18, "bold"),
            fg="#ECF0F1",
            bg="#2C3E50"
        )
        title_label.pack(pady=(0, 30))
        
        # Subtítulo
        subtitle_label = tk.Label(
            main_frame, 
            text="Iniciar Sesión", 
            font=("Arial", 12),
            fg="#BDC3C7",
            bg="#2C3E50"
        )
        subtitle_label.pack(pady=(0, 20))
        
        # Frame para los campos
        fields_frame = tk.Frame(main_frame, bg="#2C3E50")
        fields_frame.pack(pady=10)
        
        # Campo Usuario
        user_label = tk.Label(
            fields_frame, 
            text="Usuario:", 
            font=("Arial", 10, "bold"),
            fg="#ECF0F1",
            bg="#2C3E50"
        )
        user_label.grid(row=0, column=0, sticky="w", pady=(0, 5))
        
        self.user_entry = tk.Entry(
            fields_frame,
            textvariable=self.username_var,
            font=("Arial", 11),
            width=25,
            relief="flat",
            bd=5
        )
        self.user_entry.grid(row=1, column=0, pady=(0, 15))
        self.user_entry.focus()
        
        # Campo Contraseña
        pass_label = tk.Label(
            fields_frame, 
            text="Contraseña:", 
            font=("Arial", 10, "bold"),
            fg="#ECF0F1",
            bg="#2C3E50"
        )
        pass_label.grid(row=2, column=0, sticky="w", pady=(0, 5))
        
        self.pass_entry = tk.Entry(
            fields_frame,
            textvariable=self.password_var,
            font=("Arial", 11),
            width=25,
            show="*",
            relief="flat",
            bd=5
        )
        self.pass_entry.grid(row=3, column=0, pady=(0, 20))
        
        # Botones
        buttons_frame = tk.Frame(main_frame, bg="#2C3E50")
        buttons_frame.pack(pady=20)
        
        login_button = tk.Button(
            buttons_frame,
            text="INGRESAR",
            command=self.authenticate,
            font=("Arial", 11, "bold"),
            bg="#27AE60",
            fg="white",
            width=15,
            height=2,
            relief="flat",
            cursor="hand2"
        )
        login_button.pack(side=tk.LEFT, padx=(0, 10))
        
        cancel_button = tk.Button(
            buttons_frame,
            text="CANCELAR",
            command=self.cancel_login,
            font=("Arial", 11, "bold"),
            bg="#E74C3C",
            fg="white",
            width=15,
            height=2,
            relief="flat",
            cursor="hand2"
        )
        cancel_button.pack(side=tk.LEFT)
        
        # Información de usuarios de prueba
        info_frame = tk.Frame(main_frame, bg="#2C3E50")
        info_frame.pack(side=tk.BOTTOM, pady=(20, 0))
        
        info_label = tk.Label(
            info_frame,
            text="Usuarios de prueba:\nadmin/admin123 | cajero/cajero123 | gerente/gerente123",
            font=("Arial", 8),
            fg="#95A5A6",
            bg="#2C3E50",
            justify=tk.CENTER
        )
        info_label.pack()
        
        # Bind Enter key para login
        self.bind('<Return>', lambda event: self.authenticate())
        
    def authenticate(self):
        """Autentica al usuario"""
        username = self.username_var.get().strip()
        password = self.password_var.get().strip()
        
        if not username or not password:
            messagebox.showerror("Error", "Por favor, ingrese usuario y contraseña")
            return
            
        # Verificar credenciales
        if username in self.users and self.users[username] == self.hash_password(password):
            self.login_successful = True
            self.current_user = username
            messagebox.showinfo("Éxito", f"Bienvenido, {username}!")
            self.destroy()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
            self.password_var.set("")  # Limpiar contraseña
            self.pass_entry.focus()
            
    def cancel_login(self):
        """Cancela el login y cierra la aplicación"""
        self.login_successful = False
        self.destroy()
        
    def get_current_user(self):
        """Retorna el usuario actual autenticado"""
        return getattr(self, 'current_user', None)
