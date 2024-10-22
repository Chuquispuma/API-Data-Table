# API de Gestión de Usuarios

Esta es una aplicación web sencilla construida con Flask que permite gestionar usuarios a través de una API REST. Los datos se almacenan en un archivo JSON (`datos.json`).

## Descripción de la Aplicación

La aplicación permite realizar las siguientes operaciones:

- **Obtener usuarios** con paginación.
- **Agregar nuevos usuarios**.
- **Eliminar usuarios** por ID.
- **Filtrar usuarios** por nombre y rango de edad.
- **Visualizar la distribución de edades** en un gráfico.

## Tecnologías Utilizadas

- Python
- Flask
- JavaScript
- Chart.js
- HTML

## Requisitos

Para ejecutar la aplicación, asegúrate de tener instalado Python 3 y las siguientes librerías:

- Flask

## Instalación

1. **Crear un entorno virtual y activarlo:**

   ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```
2. **Instalar las dependencias:**

   ```bash
    pip install -r requirements.txt
    ```
3. **Ejecutar la aplicación:**

   ```bash
   python app.py 
    ```
   
4. **Visualizar la aplicación:**

   ```bash
   Abre tu navegador y accede al archivo HTML directamente para ver la aplicación (por ejemplo, file:///ruta/a/tu/proyecto/pagina.html).
    ```