# INTRODUCCIÓN
Este proyecto está basado con conocimientos básicos que se exponen en el repositorio de _**project-django**_ y de **crud-auth**.
Se va a mencionar conceptos que fueron mencionados en ese repositorio y se va a ir complementando con respecto para hacer un REST API.

# 1. Buenas prácticas
Recordar que las buenas prácticas consiste en:
1. Crear carpeta del proyecto.
```bash
  mkdir carpeta
```
2. Inicializar git.
```bash
  git init
```

3. Crear entorno virtual.
```python
python3 -m venv venv
```

4. Activar entorno virtual.
```bash
source ./venv/bin/activate
```
5. Hacer un documento txt en donde esten las dependencias que utilicemos.
```python
pip freeze > requirements.txt
```

6. Instalar dependencias:
```python
pip install -r requirements.txt
```
Es importante recordar que a lo largo de la vida del proyecto hay que estar guardando las dependencias si se instala algo más.

7. Instalar django y djangorestframework
```python
pip install django
```

```python
pip instal djangorestframework
```

NOTA: Si usas vscode puedes hacer clic a la barra buscadora de hasta arriba y escribir ">python: Select interpret ", la das enter. Después seleccionas el entorno virtual que creaste.
Esto te ayuda para que cuando abras una nueva terminal no tengas que activar el entorno a cada rato.

# 2. Configuración del proyecto

# 2.1) Iniciar el proyecto de django
```python
django-admin startproject drtcrud .
```
El proyecto se va a llamar drtcrud

## 2.2) Arrancar el servidor
```python
py manage.py runserver
```

## 2.3) Crear app
```python
py manage.py startapp project
```
El proyecto se llama _project_

Se va a añadir la nueva app y el módulo al proyecto, recordando que es ir al archivo de settings.py del proyecto y agregarlo en _INSTALLED_APP_ para que quede de la siguiente forma:
```python
...   
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'project',
    'rest_framework',
]
...
```
# 3. Modelos
Recordando que el modelo hace referencia a la tabla de la base de datos, entonces hay que continuar creando la tabla:
## 3.1) Crear tabla
```python
from django.db import models

# Tabla Project
class Project(models.Model):
    #Campos
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
```

## 3.2) Ejecutar las compilaciones
Esto compila las tablas
```python
py manage.py makemigrations
```

## 3.3) Crear las tablas compiladas
```python
py manage.py migrate
```