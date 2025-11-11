import mysql

from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        pass

        # TODO

    def get_tutti_musei(self):
        query = """SELECT * 
                   FROM museo"""
        result = []

        cnx = None
        cursor = None

        try:
            cnx =ConnessioneDB.get_connection()
            if cnx is None:
                print("Errore: Impossibile connettersi al database.")
                return None

            cursor = cnx.cursor(dictionary=True)
            cursor.execute(query)

            for row in cursor.fetchall():
                museo = Museo(row["id"],
                              row["nome"],
                              row["tipologia"])
                result.append(museo)

            return result


        except Exception as err:
            print(f"Errore nella lettura dal database: {err}")
            return None
        finally:
            if cursor: cursor.close()
            if cnx: cnx.close()














