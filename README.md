# Sistema de Ventas en Python

## 📋 Descripción
Sistema de punto de venta desarrollado en Python con interfaz gráfica Tkinter. Incluye sistema de autenticación, gestión de ventas e inventario.

## 🚀 Características
- ✅ Sistema de login con autenticación
- ✅ Interfaz gráfica moderna y amigable
- ✅ Múltiples usuarios con diferentes roles
- ✅ Módulo de ventas (en desarrollo)
- ✅ Gestión de inventario (en desarrollo)
- ✅ Seguridad con hash de contraseñas

## 👥 Usuarios de Prueba
| Usuario | Contraseña | Rol |
|---------|------------|-----|
| admin | admin123 | Administrador |
| cajero | cajero123 | Cajero |
| gerente | gerente123 | Gerente |

## 🛠️ Instalación y Uso

### Requisitos
- Python 3.7 o superior
- Tkinter (incluido con Python)

### Ejecutar la aplicación
```bash
python index.py
```

## 📁 Estructura del Proyecto
```
sales-system/
├── index.py          # Punto de entrada de la aplicación
├── login.py           # Sistema de autenticación
├── manager.py         # Gestor principal de la aplicación
├── container.py       # Contenedor principal de la UI
├── sales.py           # Módulo de ventas
├── inventory.py       # Módulo de inventario
└── README.md          # Documentación
```

## 🔧 Funcionalidades por Implementar
- [ ] Base de datos para persistencia
- [ ] CRUD completo de productos
- [ ] Sistema de ventas funcional
- [ ] Generación de reportes
- [ ] Impresión de tickets
- [ ] Gestión de clientes
- [ ] Control de stock automático

## 🎨 Capturas de Pantalla
El sistema cuenta con:
- Pantalla de login elegante y segura
- Interfaz principal con botones de navegación
- Módulos separados para ventas e inventario
- Barra de usuario con información de sesión

## 👨‍💻 Desarrollador
Sistema desarrollado como proyecto educativo para aprender desarrollo de aplicaciones de escritorio con Python y Tkinter.

## 📝 Notas
- Las contraseñas se almacenan hasheadas con SHA-256
- La aplicación está diseñada para ser fácilmente extensible
- Los módulos están separados para facilitar el mantenimiento