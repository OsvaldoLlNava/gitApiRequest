from issue import issue
import sqlite3


def Crear_Tabla_Issues():
    try:
        conexion = sqlite3.connect('issues.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = """CREATE TABLE IF NOT EXISTS issues(
                numero TEXT,
                link TEXT,
                titulo TEXT ,
                autor TEXT,
                labels TEXT,
                milestoneTitle TEXT,
                milestoneDescription TEXT
                );"""
        cursor.execute(query)

        print('Tabla creada con exito')
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion', error)

    finally:
        if(conexion):
            conexion.close()


def Agregar_Elemento_Issue(numero, url, titulo, autor, labels, milestoneTitle, milestoneDescription):
    try:
        conexion = sqlite3.connect('issues.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = """INSERT INTO issues VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format(
            numero, url, titulo, autor, labels, milestoneTitle, milestoneDescription)
        resultado = cursor.execute(query)
        conexion.commit()
        print('Valor Insertado Correctamente', resultado)
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion', error, "queso")

    finally:
        if(conexion):
            conexion.close()


def Agregar_Elemento():
    try:
        conexion = sqlite3.connect('issues.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = """INSERT INTO issues VALUES ('{}', '{}', '{}', '{}', '{}', '{}')""".format(
            "numero", "url", "titulo", "autor", "labels", "milestoneTitle", "milestoneDescription")
        resultado = cursor.execute(query)
        conexion.commit()
        print('Valor Insertado Correctamente', resultado)
        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion', error, "queso")

    finally:
        if(conexion):
            conexion.close()


def Ver_Todo():
    try:
        conexion = sqlite3.connect('issues.db')
        cursor = conexion.cursor()
        print('Conectado')

        query = 'SELECT * FROM issues;'
        cursor.execute(query)
        rows = cursor.fetchall()
        print('Total de registros: ', len(rows))

        print('------------Registros-------------')

        for row in rows:
            print(
                'Issue #{}\n- URL: {}\n- Nombre: {}\n- Autor: {}\n- Tags: [{}]\n- Milestone\n\t- Nombre: {}\n\t- Descripcion: {}'.format(*row))
            print('-------------------------------')

        print('Total de registros: ', len(rows))

        cursor.close()

    except sqlite3.Error as error:
        print('Error con la conexion', error)

    finally:
        if(conexion):
            conexion.close()
