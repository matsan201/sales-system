from tkinter import Tk, Frame, Label
from container import Container

class Manager(Tk):
    def __init__(self, current_user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.current_user = current_user or "Usuario"
        self.title(f"Sistema de Ventas v 1.0 - Usuario: {self.current_user}")
        self.resizable(False, False)
        self.configure(bg="#C6D9E3")
        self.geometry("800x400+120+20")
        
        # Agregar barra de usuario
        self.create_user_bar()

        # Agregar barra de usuario
        self.create_user_bar()

        self.container = Frame(self, bg="#C6D9E3")
        self.container.pack(fill="both", expand=True)

        self.frames = {
            Container: None
        }

        self.load_frames()

        self.show_frame(Container)
        
    def create_user_bar(self):
        """Crea una barra superior con información del usuario"""
        user_frame = Frame(self, bg="#34495E", height=30)
        user_frame.pack(fill="x", side="top")
        user_frame.pack_propagate(False)
        
        user_label = Label(
            user_frame,
            text=f"👤 Usuario: {self.current_user} | Sistema de Ventas",
            bg="#34495E",
            fg="white",
            font=("Arial", 10, "bold")
        )
        user_label.pack(side="left", padx=10, pady=5)

    def load_frames(self):
        for FrameClass in self.frames.keys():
            frame = FrameClass(self.container, self)
            self.frames[FrameClass] = frame


    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()

def main():
    app = Manager()
    app.mainloop()

if __name__ == "__main__":
    main()
