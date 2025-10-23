#  Sistema de Administración de Equipos — Proyecto Django

Este proyecto implementa una aplicación web desarrollada con Django para gestionar el inventario de equipos tecnológicos (notebooks, proyectores, impresoras) en una organización. Incluye un panel de administración personalizado, modelos relacionales y una interfaz para registrar, editar y visualizar equipos.

---

##  Requisitos del entorno

- Python 3.11 o superior
- pip (gestor de paquetes de Python)
- Git
- Navegador web moderno
- Sistema operativo: Windows, Linux o macOS

---

##  Instalación paso a paso

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu_usuario/ev2_equipo_admin.git
cd ev2_equipo_admin
```
### 2. Crear y activar entorno virtual
```bash
python -m venv venv
venv\Scripts\activate   # En Windows
source venv/bin/activate   # En Linux/Mac
```
### 3. Instalar dependencias
```bash
pip install django
```
### 4. Migrar la base de datos
```bash
python manage.py makemigrations
python manage.py migrate
```
### 5. Crear superusuario para el panel de administración
```bash
python manage.py createsuperuser
```
Completa los campos solicitados (usuario, correo, contraseña).
### 6. Ejecutar el servidor
```bash
python manage.py runserver
```
Accede a la aplicación en tu navegador:
```bash
http://127.0.0.1:8000/admin/
```
## Modelo
El modelo se encuentra en equipos/models.py y contiene los siguientes campos:

nombre: Nombre del equipo

categoria: Tipo de equipo (Proyector, Notebook, Impresora)

estado: Estado actual (Operativo, En reparación, Dado de baja)

fecha_ingreso: Fecha de incorporación

ubicacion: Ubicación física del equipo

El modelo está registrado en equipos/admin.py para ser gestionado desde el panel de administración. Se utiliza list_display para mostrar los campos principales en la vista de tabla.

# Super Admin
Funcionalidades del panel de administración
- Visualización tabular de equipos
- Agregado, edición y eliminación de registros
- Visualización amigable con get_categoria_display() y get_estado_display()
- Panel accesible mediante superusuario
