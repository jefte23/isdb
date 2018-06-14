from dao import connection_dao
from model import temporada_model
#----------------------------------------------------------------------------#

def get_temporada(file, idtemporada):

    connection, cursor = connection_dao.get_connection(file)
    query = f"SELECT * FROM isdb.temporada WHERE idtemporada = '{idtemporada}'"
    cursor.execute(query)

    data = cursor.fetchone()

    temporada = temporada_model.Temporada(idtemporada,
                                          data[1],
                                          data[2],
                                          data[3],
                                          data[4])

    connection.close()

    return temporada



#----------------------------------------------------------------------------#

def get_temporadas(file, idserie):

    connection, cursor = connection_dao.get_connection(file)
    query = f"SELECT * FROM isdb.temporada WHERE idserie = '{idserie}'"
    cursor.execute(query)

    data = cursor.fetchall()

    temporadas = []
    for tmp in data:
        temporada = temporada_model.Temporada(tmp[0],
                                              tmp[1],
                                              tmp[2],
                                              tmp[3],
                                              tmp[4])
        temporadas.append(temporada)

    connection.close()

    return temporadas

#----------------------------------------------------------------------------#
def get_todasTemporadas(file):

    connection, cursor = connection_dao.get_connection(file)
    query = f"SELECT * FROM isdb.temporada"
    cursor.execute(query)

    data = cursor.fetchall()

    temporadas = []
    for tmp in data:
        temporada = temporada_model.Temporada(tmp[0],
                                              tmp[1],
                                              tmp[2],
                                              tmp[3],
                                              tmp[4])
        temporadas.append(temporada)

    connection.close()

    return temporadas


#----------------------------------------------------------------------------#

def cadastraTemporada(file, idserie, ano, sinopse, banner):

    connection, cursor = connection_dao.get_connection(file)
    query = f"INSERT INTO isdb.temporada (idserie, ano, sinopse, banner) VALUES ('{idserie}', '{ano}', '{sinopse}', '{banner}');"
    cursor.execute(query)
    connection.commit()


#----------------------------------------------------------------------------#

def atualizaTemporada(file, idtemporada, ano, sinopse, banner):

    connection, cursor = connection_dao.get_connection(file)
    query = f"UPDATE isdb.temporada SET ano = '{ano}', sinopse = '{sinopse}', banner = '{banner}' WHERE idtemporada = '{idtemporada}'"
    cursor.execute(query)
    connection.commit()

#----------------------------------------------------------------------------#

def excluiTemporada(file, idtemporada):

    connection, cursor = connection_dao.get_connection(file)
    query = f"DELETE FROM isdb.temporada WHERE idtemporada = '{idtemporada}';"
    cursor.execute(query)
    connection.commit()
