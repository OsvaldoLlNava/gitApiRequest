import requests
import database
import issue

# uso de la Api de github, documentacion: https://docs.github.com/en/rest


def obtener_issues():
    count = 1  # inicializacion de contador, este servira para las paginas, no revisar solo los primeros resultados, sino buscar todos en las diferentes paginas de resultados
    seguir = True

    while (seguir):  # ciclo para poder hacer mas de una peticion, dependiendo cuantas paginas de issues tenga el repo
        resp = requests.get(
            'https://api.github.com/repos/golang/go/issues?labels=Go2&page={}&per_page=100&state=all'.format(count))
        # los parametros dados son: que se busque que tenga la etiqueta de Go2 (labels=Go2), el numero de pagina a consultar (page={} donde {} va incrementando desde el 1)
        # la peticion se hace con 100 resultados por pagina ya que asi se reducen la cantidad de peticiones por hacer, 100 es el numero maximo de resultados por pagina que permite la API
        # y pos ultimo el parametro state define en que estado queremos los issues, teniendo "open", "close" y "all", en este caso el problema decia todos asi que se uso "all"
        count += 1
        body = resp.json()

        if body != []:  # Esta es una validacion para saber cuando parar, si la respuesta ya no nos entrega informacion entonces es momento de terminar el ciclo
            for problema in body:
                tags = ""
                labels = problema["labels"]
                for tag in labels:
                    tags += tag["name"]
                    tags += ","
                milestoneT = " "
                milestoneD = " "
                # validacion de si milestone no existe ya que algunos resultados de issues no contenian la llave milestone
                if problema["milestone"] is not None:
                    milestoneT = problema["milestone"]["title"]
                    milestoneD = problema["milestone"]["description"]
                database.Agregar_Elemento_Issue(issue.issue(problema["number"], problema["html_url"], problema["title"], problema["user"]
                                                ["login"], tags, milestoneT, milestoneD))
        else:
            seguir = False


if __name__ == '__main__':
    database.Crear_Tabla_Issues()
    obtener_issues()
    database.Ver_Todo()


# pasos a seguir en este codigo:
# obtener los datos de los issues disponibles en el repositorio  https://github.com/golang/go/
# guardar esos datos en base de datos
# visualizar la base de datos con formato especifico
