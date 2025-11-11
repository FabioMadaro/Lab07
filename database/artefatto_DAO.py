from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass

    # TODO
    def get_tutte_epoche(self):
        query = """SELECT DISTINCT epoca 
                   FROM artefatto
                   ORDER BY epoca ASC"""
        result = []

        cnx = None
        cursor = None

        try:
            cnx = ConnessioneDB.get_connection()
            if cnx is None:
                print("Errore: Impossibile connettersi al database.")
                return None

            cursor = cnx.cursor()
            cursor.execute(query)

            for row in cursor.fetchall():
                result.append(row[0])

            return result

        except Exception as err:
            print(f"Errore: {err}")
            return None

        finally:
            if cursor: cursor.close()
            if cnx: cnx.close()


    def cerca_artefatti(self, id_museo, epoca):

        query = """SELECT id, nome, tipologia, epoca, id_museo 
                   FROM artefatto
                   WHERE (%s IS NULL OR id_museo = %s) 
                   AND (%s IS NULL OR epoca = %s)
                   ORDER BY nome ASC"""

        museo_param = id_museo
        epoca_param = epoca

        params = (museo_param, museo_param, epoca_param, epoca_param)

        result = []
        cnx = None
        cursor = None

        try:
            cnx = ConnessioneDB.get_connection()
            if cnx is None:
                print("Errore: Impossibile connettersi al database.")
                return None

            cursor = cnx.cursor(dictionary=True)
            cursor.execute(query, params)

            for row in cursor.fetchall():
                artefatto = Artefatto(
                    row["id"],
                    row["nome"],
                    row["tipologia"],
                    row["epoca"],
                    row["id_museo"]
                )
                result.append(artefatto)
            return result

        except Exception as err:
            print(f"Errore: {err}")
            return None

        finally:
            if cursor: cursor.close()
            if cnx: cnx.close()












