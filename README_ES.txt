Instrucciones de configuración del entorno para Windows / Windows Intructions (Spanish)

1. Descargar e Instalar Git: https://git-scm.com/downloads
2. Descargar Python 2.7: https://www.python.org/downloads/
3. Instalar en C:\Python27
4. Click derecho en Equipo 
   > Propiedades 
   > Configuración Avanzada del Sistema
   > Opciones Avanzadas
   > Variables de Entorno
   > Buscar una variable del sistema llamada "Path"
   > Agregar a esta la ruta:
     "C:\Python27; C:\Python27\Scripts"
   > Aceptar
5. Abrir la consola de Git:
6. Ejecutar con la consola de Git: 
   "git config --system http.sslverify false"
7. Descargar el proyecto con en la consola de Git:
   "git clone https://github.com/64lines/project_eba"
8. Ir a la carpeta del usario en la consola de comandos de Windows:
    cd C:/Users/nombredelusuario
9. Instalar Django con la consola de comandos de Windows:
   "pip install django"
10. Ejecutar el servidor local con la consola de comandos de Windows:
   "python manage.py runserver"
11. Verificar el servidor local ingresando en el navegador
   "127.0.0.1:8000/admin"
12. Intalar Sublime Text: http://www.sublimetext.com/2
13. Abrir Sublime Text y cargar la carpeta del proyecto en "/Users/nombredelusuario" o "/Usuarios/nombredelusuario".
14. Trabajar en el código...

Para Subir los Cambios Realizados

1. Crear una cuenta en www.github.com si no se tiene una
2. Abrir la consola de Git.
3. Mirar los cambios que se han hecho con:
   "git status"
4. Incluir todos los cambios que se han hecho con:
   "git add ."
5. Guardar los cambios en el repositorio local usando el siguiente comando:
   git commit -m "Se realizaron cambios en ..."
6. Subir los cambios en el repositorio general:
   git push origin master:tu-nombre


