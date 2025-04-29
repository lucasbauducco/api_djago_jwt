# API REST con Django, JWT y Swagger

Este proyecto es una API RESTful construida con Django y Django REST Framework, que implementa autenticación basada en tokens JWT y documentación automática usando Swagger (drf-yasg).

## 📌 Características

- Autenticación segura mediante JWT (JSON Web Tokens)
- Documentación de la API con Swagger y Redoc
- Configuración para conectar con cualquier base de datos (por defecto usa SQLite)
- Estructura de proyecto limpia y escalable
- Permite registrar, listar, actualizar y eliminar productos
- Protección de rutas con permisos (JWT requerido)
- Documentación pública

---

## 🚀 Instalación

Sigue estos pasos para ejecutar el proyecto en tu entorno local.

### 1. Clonar el repositorio

```bash
git clone https://github.com/lucasbauducco/api_djago_jwt.git
cd api_djago_jwt
```
### 2. Crear entorno virtual
```bash
python -m venv env
source env/bin/activate      # Linux/macOS
env\Scripts\activate         # Windows
```
### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```
### 4. Aplicar migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```
### 5. Crear superusuario (opcional, para acceder al admin)
```bash
python manage.py runserver
```
## 🔐 Autenticación

**Obtener token:**

```bash http
POST /api/token/
```
**Renovar token:**
```bash http
POST /api/token/refresh/
```
**Incluir el token en el header para acceder a rutas protegidas:**
```bash http
Authorization: Bearer <tu_token>
```
## 🧭 Documentación API
```bash 
Swagger UI: http://localhost:8000/swagger/

Redoc: http://localhost:8000/redoc/
```
## 🗃️ Base de datos
Por defecto se usa SQLite para facilitar la instalación, pero podés modificar la configuración en settings.py para usar PostgreSQL, MySQL u otra base de datos.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
## 🗃️ Base de datos PostgreSQL
Para usar PostgreSQL u otra base de datos con configuración desde un archivo .env:
**1. Instalar python-decouple:**
```bash 
pip install python-decouple
```
**2. Agregar esto en tu settings.py:**
```
from decouple import config

DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE', default='django.db.backends.postgresql'),
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
    }
}

```
**3. Crear un archivo .env en la raíz del proyecto con tus credenciales:**
``` bash
DB_ENGINE=django.db.backends.postgresql
DB_NAME=nombre_de_tu_base
DB_USER=usuario
DB_PASSWORD=contraseña
DB_HOST=localhost
DB_PORT=5432
```
## 🛠️ Requisitos
Python 3.8+

## 📂 Estructura del proyecto
``` bash
api_djago_jwt/
├── core/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── api_djago_jwt/
│   └── settings.py
├── manage.py
├── .env
└── requirements.txt
```
## 📄 Licencia
Este proyecto es de código abierto bajo licencia MIT.
## 🙋‍♂️ Autor
**Lucas Bauducco**  
[https://github.com/lucasbauducco](https://github.com/lucasbauducco)
