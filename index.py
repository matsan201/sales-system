from manager import Manager
from login import Login
import sys

def main():
    """Función principal que maneja el flujo de login y aplicación"""
    # Crear y mostrar ventana de login
    login_window = Login()
    login_window.mainloop()
    
    # Verificar si el login fue exitoso
    if login_window.login_successful:
        current_user = login_window.get_current_user()
        # Crear y mostrar la aplicación principal
        app = Manager(current_user=current_user)
        app.mainloop()
    else:
        # Si el login fue cancelado, terminar la aplicación
        print("Login cancelado. Cerrando aplicación...")
        sys.exit()

if __name__ == "__main__":
    main()