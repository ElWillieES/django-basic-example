# Django Basic Example

![Docker](https://img.shields.io/badge/Docker-2496ED?&style=flat&logo=docker&logoColor=ffffff)&nbsp;
![Python](https://img.shields.io/badge/Python-14354C?style=flat&logo=python&logoColor=white)&nbsp;
![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white)&nbsp;
![NGINX](https://img.shields.io/badge/Nginx-009639?style=flat&logo=nginx&logoColor=white)&nbsp;

## Introducción

Este repo tiene un fin principalmente didáctico, como un ejemplo básico de proyecto Python con el framework Django y el IDE de PyCharm, gestión de paquetes o librerías (Virtual Environments), ejecución y depuración de código, dockerización y ejecución en local con Docker y Docker Compose, utilización de Gunicorn como servidor Web y NGINX como Proxy Inverso, etc.

Se ha creado para complementar varios Post del Blog [El Willie - The Geeks invaders](https://elwillie.es), cada Post tiene el código en un tag de git.

El Post [Python – Ejemplo de un proyecto básico con Python, Django y PyCharm](https://elwillie.es/2023/05/25/ejemplo-de-un-proyecto-basico-con-python-django-y-pycharm/) tiene como objetivo ver los siguientes puntos:

* Cómo utilizar Plantillas (Templates) para crear páginas Web con Django, incluido la utilización de una plantilla base donde reutilizar la cabezará y pie de nuestras páginas.
* Cómo crear un Modelo y utilizar el ORM de Django para crear las tablas de base de datos, en este caso, sobre SQLite.
* Cómo utilizar el Panel de Administración de Django Admin, para tener una zona privada donde poder hacer tareas de alta/baja/modificación de nuestro modelo de datos.
* Cómo utilizar Vistas basadas en Clases.
* Cómo crear Pruebas Unitarias en Django, incluyendo la forma de generar un informe de cobertura y de subirlo a Sonar.
* Cómo dockerizar nuestra aplicación con un NGINX y Gunicorn como servidor de aplicaciones, teniendo en cuenta, que en este caso tenemos que generar los estáticos de Django (ej: css, js, etc.) para que sean servidos por el NGINX.

El Post [Python – Ejemplo de un proyecto básico con Python, Django y PyCharm - II]() tiene como objetivo ver los siguientes puntos:

* Cómo generar páginas dinámicas desde el modelo de base de datos
* Cómo entregar las páginas con estilos (ej: css, fuentes, imágenes, etc) y cómo realizar la gestión de dichos archivos estáticos.
* Cómo crear páginas de formularios, que permitan a los usuarios no admins realizar operaciones CRUD (Create, Read, Update, Delete), mediante la auto-generación de formularios Django (ej: form.as_p, form.as_table, form.as_ul) y la extensión de vistas genéricas (ej: CreateView, UpdateView, DeleteView).
* Cómo configurar la autenticación de usuarios (ej: log in, log out, sign up), mediante la auto-generación de formularios Django (ej: form.as_p, form.as_table, form.as_ul) y vistas genéricas (ej: LoginView, SignUpView), así como proteger los enlaces a los formularios para que sean accedidos sólo por usuarios autenticados.

**Puedes apoyar mi trabajo haciendo "☆ Star" en el repo o nominarme a "GitHub Star"**. Muchas gracias :-) 

[![GitHub Star](https://img.shields.io/badge/GitHub-Nominar_a_star-yellow?style=for-the-badge&logo=github&logoColor=white&labelColor=101010)](https://stars.github.com/nominate/)


## Arquitectura de la Solución

Se trata de un Proyecto Python que contiene:

* Un Proyecto Django, llamado basic_example.
* Una Aplicación Django, llamada basic_example_pages, que responde en la ruta por defecto de http://localhost:8000/
* Se puede ejecutar dockerizado, para lo que incluye un fichero Dockerfile y un Docker Compose, y levanta un servidor Web Gunicorn junto con un NGINX. Además, se realiza la generación de estáticos en el arranque del contenedor Djando, sobre un volumen compartido con el NGINX, para que los pueda servir el propio NGINX.
 
Podemos ejecutarlo en local, arrancando el servidor Web de Django ejecutando un comando como el siguiente:

```
python manage.py runserver
```


## Otros detalles de interés

Si te interesa aprender Python, tienes disponibles los siguientes [cursos gratuitos de Python en Edube - OpenEDG](https://edube.org/):

* Python Essentials 1
* Python Essentials 2
* Python Advanced 1 – OOP
* Python Advanced 2 – Best Practices and Standardization
* Python Advanced 3 – GUI Programming
* Python Advanced 4 – RESTful APIs
* Python Advanced 5 – File Processing

Otro recurso muy interesante es [Real Python](https://realpython.com/), donde podrás encontrar tutoriales, baterías de preguntas para ponerte a prueba (quizzes), etc.

En mi Blog personal ([El Willie - The Geeks invaders](https://elwillie.es)) y en mi perfil de GitHub, encontrarás más información sobre mi, y sobre los contenidos de tecnología que comparto con la comunidad.

[![Web](https://img.shields.io/badge/GitHub-ElWillieES-14a1f0?style=for-the-badge&logo=github&logoColor=white&labelColor=101010)](https://github.com/ElWillieES)

# Git

## Repositorio

Este repo se puede clonar desde GitHub utilizando este [enlace HTTP](https://github.com/ElWillieES/django-basic-example.git). 

A continuación se muestra el comando git clone usando SSH en lugar de HTTP.

```sh
git clone git@github.com:ElWillieES/django-basic-example.git
```


# Docker - Ejecución en local

## Con Docker

Se puede ejecutar la aplicación en local con Docker. 

Los siguientes comandos ejecutados en la raíz del Proyecto, muestran:
* Cómo **crear una imagen** en local con docker build.
* Cómo listar las imágenes que tenemos disponibles en local. Deberá aparecer la que acabamos de crear.
* **Cómo ejecutar un contenedor con nuestra imagen**.
* Cómo parar el contenedor, cuando acabemos nuestras pruebas.

```shell
docker build -t django-basic-example .
docker images
docker run -it --rm -d -p 8000:8000 --name django-basic-example django-basic-example
docker stop django-basic-example
```

Podemos arrancar una sesión interativa de Bash sobre un Contendor con nuestra imagen Docker, para de este modo, analizar mejor incidencias y problemas que nos puedan surgir, depurar, etc. Suele ser bastante útil.

En el siguiente ejemplo, arrancamos una sesión bash sobre un contenedor con nuestra imagen, arrancamos manualmente la aplicación con gunicorn, y finalmente salimos.

```shell
docker run -it --rm -p 8000:8000 --name django-basic-example django-basic-example /bin/bash
gunicorn basic_example.wsgi:application --bind 0.0.0.0:8000
exit
```


## Con Docker Compose

El siguiente comando ejecutado en la raíz del Proyecto, muestra cómo compilar (es decir, construir la imagen Docker) y ejecutar django-basic-example con Docker Compose, así como la forma de poder comprobar los logs de su ejecución.

Si observamos el fichero **docker-compose.yml**, podemos ver que incluye un contenedor para la aplicación y otro para un NGINX que actúa como Proxy Inverso en el puerto tcp-80, además de un volumen compartido donde Django generará los estáticos, para que el NGINX los pueda servir. 

```shell
docker-compose up --build -d
docker-compose logs
```

