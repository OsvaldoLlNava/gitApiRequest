import requests
import database
import issue
import pprint
import json


def obtener_issues():
    count = 1
    resp = ""
    seguir = True
    while (seguir):
        resp = requests.get(
            'https://api.github.com/repos/golang/go/issues?labels=Go2&page={}&per_page=100'.format(count))
        count += 1
        body = resp.json()
        print(resp)
        print("----------------------------")
        print(body)
        if body != []:
            for problema in body:
                tags = ""
                labels = problema["labels"]
                for tag in labels:
                    tags += tag["name"]
                    tags += ","
                milestoneT = " "
                milestoneD = " "
                if problema["milestone"] is not None:
                    milestoneT = problema["milestone"]["title"]
                    milestoneD = problema["milestone"]["description"]
                database.Agregar_Elemento_Issue(issue.issue(problema["number"], problema["html_url"], problema["title"], problema["user"]
                                                ["login"], tags, milestoneT, milestoneD))
        else:
            seguir = False

#         datos importantes
# html_url : este es el url que abre el issue para verlo en github
# title : Nombre del Issue
# number: Numero del Issue
# user[login] : Nombre del Autor del Issue
# labels: Lista de Tags
# milestone[title] : Nombre del Milestone
# milestone[description] : Descripcion del Milestone


if __name__ == '__main__':
    database.Crear_Tabla_Issues()
    obtener_issues()
    database.Ver_Todo()
    print("fin")
