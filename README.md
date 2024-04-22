# Trabajo Práctico: Aspectos Legales de la Informática

## Introducción:
- En este desafío, exploraremos la Ley de Protección de Datos Personales y la tecnología de Firma Digital en el contexto de la empresa John Doe S.A., que desarrolla y administra un sistema hospitalario. La aplicacion consiste de formularios simples para alta, baja y modificacion de pacientes. Los usuarios pueden ser un paciente, un medico o un administrador. De acuerdo al tipo de usuario cada uno tiene distintas vistas de la aplicacion y permisos. El administrativo en este caso es un super-usuario. Los pacientes podran darse de alta en la aplicacion completando un formulario de registro con un usuario, mail y contraseña. Los usuario que tienen permiso de entrar en la aplicacion son solo los usuario autenticados por lo que al momento de registrase se le enviara un enlace de autenticacion al correo y podran ingresar en la aplicacion. La vista del paciente es algo escaza, pero puede solicitar turnos (sin implementar), ver sus datos e historia clinica. Los medicos pueden ver los pacientes y darlos de alta tambien. Pueden cargar datos en su historia clinica y tambien asignarles turnos (sin implementar). Los administrativos pueden dar de alta, baja y modifcar pacientes y medicos.

## Profesores 
- Consentino, Guillermo
- Zappellini, Bruno

## Alumno:
- Barea Matias Ezequiel

# Documentacion
- Framework utilizado: Flask
- Frontend: Bootstrap 5

## Diseño

- Estructura de archivos:
   - src/
      - app.py
      - config.sql
      - utils/
      - templates/
         - ...
         - auth/
            - login.html
            - register.html
      - static/
         - css/
            - ...
         - images/
            - ...
      - routes/
         - ...
      - models/
         - entities/
            - ...
         - ...
      - database/
         - ...
   - .venv/
   - README.md

## Base de datos:
Se opto por utilizar una base de datos relacional en postgreSQL

## Intrucciones de ejecucion
## Requisitos

- *Tener Docker instalado*
    Link para descargar: https://www.docker.com/products/docker-desktop/
- *Tener git instalado*
    Link para descargar: https://git-scm.com/downloads

## Correr aplicacion
- Una vez que se cumple con lo requisitos previos hay que descargar el repositorio desde *GitHub*. Para ello abriremos una consola de *git bash*, nos desplazaremos al directorio en el cual clonar el repositorio y ejecutar el comando `git clone https://github.com/Matiaseze/tp-aspectos-legales.git` 

- Una vez descargado nos situaremos dentro del directorio con el comando `cd tp-aspectos-legales/`

- Para poner en funcionamiento la aplicacion utilizaremos el comando:
`docker-compose up -d ` 
El cual levanta dos imagenes, una de la base de datos postgres para almacenar datos e informacion de los usuarios de la aplicacion y la otra es la aplicacion en cuestion en un entorno aislado y configurado para funcione de acuerdo a los requerimientos necesarios.

NOTA: en caso de no poder logearse es probable que el dump no se haya ejecutado cuando inicio el contenedor. Utilizar el comando `docker exec tp-aspectos-legales-dbpg-1 pg_restore -U postgres -d flask-restapi < /docker-entrypoint-initdb.d/backup.sql`. luego de ejecutarlo comprobar la aplicacion.

# Abrir la app
http://localhost:7000/



