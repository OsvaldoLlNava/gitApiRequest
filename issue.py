class issue():
    def __init__(self, url='', titulo='', numero='', autor='', labels=[], milestoneTitle='', milestoneDescription=''):
        self._url = url
        self._titulo = titulo
        self._numero = numero
        self._autor = autor
        self._labels = labels
        self._milestoneTitle = milestoneTitle
        self._milestoneDescription = milestoneDescription

    def __str__(self):
        return 'Issue #{}\n- URL: {}\n- Nombre: {}\n- Autor: {}\n- Tags: {}\n- Milestone\n\t- Nombre: {}\n\t- Descripcion: {}'.format(self._numero, self._url, self._titulo, self._autor, self._labels, self._milestoneTitle, self._milestoneDescription)


#         datos importantes
# html_url : este es el url que abre el issue para verlo en github
# title : Nombre del Issue
# number: Numero del Issue
# user[login] : Nombre del Autor del Issue
# labels: Lista de Tags
# milestone[title] : Nombre del Milestone
# milestone[description] : Descripcion del Milestone
