El problema planteado requeria el uso de la API de github
el objetivo actual era obtener los issues del repositorio https://github.com/golang/go/ , especificando 
que se obtendrian solamente los issues que contuvieran la etiqueta "Go2"
despues de recuperar estos datos, tenian que ser almacenados en una base de datos para su
posterior lectura y presentacion en un formato definido


Para la solucion de esto se opto por usar python, usandose en su ultima version que es la version 3.9.5
y acompañado a este lenguaje se utilizo sqlite como motor de base de datos
Todo esto fue desarrollado sobre el sistema operativo de Windows 10


Librerias:

Como librerias se utilizaron 2:
La primera, una libreria para realizar peticiones llamada "requests" la cual tuvo que 
ser instalada usando "pip install requests", esto para su correcto funcionamiento y fue utilizada para realizar las 
peticiones necesarias a la API para obtener los datos requeridos
Ademas de que se utilizo la libreria de "sqlite3" para hacer uso de sqlite en este proyecto


Explicacion:

Se desarrollaron 3 archivos, un archivo llamado "issue.py" en el cual se creo el objeto issue, para hacer mas facil su manipulacion,
otro archivo de nombre "database.py" en el cual como su nombre lo indica es el archivo que contiene lo necesario para la
manipulacion de la base de datos, en este caso la creacion de la tabla, la insercion de cada elemento y la recuperacion de estos datos
y por ultimo el archivo "main.py", este es el archivo central el cual contiene la obtencion de los datos requeridos y la ejecucion de las funciones correspondientes
EL archivo "main.py" realiza la peticion a la API para obtener los issues del repositorio indicado y con las caracteristicas deseadas iniciando desde la pagina 1 de issues, 
una vez obtenidos los datos, son convertidos a formato json para facilitar su manejo, posteriormente se extraen los datos significativos
del json y una vez comprobado que existan los datos que puedan faltar y se hayan adaptado los datos, son guardados en la base de datos mediante la funcion correspondiente,
una vez terminado este proceso se repite cambiando la pagina a consultar, ya que cada peticion consulta una pagina de maximo 100 elementos, en caso de ser mas de 100 elementos
es necesario revisar una segunda pagina y asi sucesivamente hasta que ya no haya mas paginas disponibles con informacion

Una vez que se ejecute el archivo "main.py" se realizara todo el proceso y se generara la base de datos llamada "issues.db" en la cual estaran almacenados los datos correspondientes


