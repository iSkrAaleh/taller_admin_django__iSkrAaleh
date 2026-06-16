# Taller: Implementación de ORM y Django Admin

Este repositorio contiene la configuración de un proyecto en Django para gestionar la información de **Museos, Guías de Museo y Exhibiciones**

Se configuró el panel de administración (`admin.py`) para presentar cálculos personalizados en tiempo real (Costo total de exhibiciones y el Guía con más experiencia), utilizando pura lógica de programación en los modelos (`models.py`)

---

## Escenarios de Base de Datos

Para demostrar la flexibilidad del ORM de Django al momento de cambiar de motor de base de datos, el proyecto fue probado en dos escenarios distintos:

### 1. SQLiteBrowser + Admin de Django
*Entorno de desarrollo por defecto utilizando la base de datos local SQLite*



<img width="1920" height="1200" alt="sqlite_admin" src="https://github.com/user-attachments/assets/664ebc79-6107-4e96-aabb-d9ba0cd026dc" />



### 2. phpMyAdmin + Admin de Django
*Entorno adaptado utilizando MariaDB y phpMyAdmin, levantados mediante contenedores de Docker*



<img width="1920" height="1200" alt="phpmyadmin_djangoadmin" src="https://github.com/user-attachments/assets/dafe750e-eca0-44d3-9998-bc52ef01cc38" />




