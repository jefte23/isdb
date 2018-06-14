from dao import connection_dao
from model import episodeo_model, episodioV2_model
#----------------------------------------------------------------------------#

# Todos os episodios de uma serie
def get_TodosEpisodios(file, idserie):
    connection, cursor = connection_dao.get_connection(file)

    query = f"SELECT * FROM isdb.episodio WHERE idserie = '{idserie}'"
    cursor.execute(query)

    data = cursor.fetchall()

    episodeos = []
    for episodeo in data:
        _episodeos = episodeo_model.Episodeo(episodeos[0], episodeos[1], episodeos[2],
                                             episodeos[3], episodeos[4], episodeos[5],
                                             episodeos[6], episodeos[7], episodeos[8])
        episodeos.append(_episodeos)

    connection.close()
    return episodeo

#----------------------------------------------------------------------------#

# todos os episodios de uma temporada
def get_TempEpisodios(file, idserie, idtemporada):

    connection, cursor = connection_dao.get_connection(file)

    query = f"SELECT * FROM isdb.episodio WHERE idserie = '{idserie}' and idtemporada = '{idtemporada}'"
    cursor.execute(query)

    data = cursor.fetchall()

    episodeos = []
    for episodeo in data:
        _episodeos = episodeo_model.Episodeo(episodeo[0], episodeo[1], episodeo[2],
                                             episodeo[3], episodeo[4], episodeo[5],
                                             episodeo[6], episodeo[7], episodeo[8])
        episodeos.append(_episodeos)


    return episodeos

#----------------------------------------------------------------------------#

# seleciona apenas o episodio passado
def get_episodio(file, idepisodeo):
    connection, cursor = connection_dao.get_connection(file)

    query = f"SELECT * FROM isdb.episodio WHERE idepisodeo = '{idepisodeo}'"
    cursor.execute(query)

    data = cursor.fetchone()
    episodeo = episodeo_model.Episodeo(idepisodeo, data[0], data[1],
                                       data[2], data[3], data[4], data[5],data[6], data[7])


    connection.close()

    return episodeo


#----------------------------------------------------------------------------#

# cadastro de episodeo
def cadastra_episodio(file, idserie, idtemporada, iddiretor, idescritor, temporada, titulo, data, sinopse):

    connection, cursor = connection_dao.get_connection(file)

    query = f"INSERT INTO isdb.episodio (idserie, idtemporada, iddiretor, idescritor, temporada, titulo, data, sinopse) " \
            f"VALUES ('{idserie}', '{idtemporada}', '{iddiretor}', '{idescritor}', '{temporada}', '{titulo}', " \
            f"'{data}', '{sinopse}')"
    cursor.execute(query)
    connection.commit()

#----------------------------------------------------------------------------#

# alteração em nos dados cadastrados
def atualizaEpisodio(file, idepisodio, idserie, idtemporada, iddiretor, idescritor, temporada, titulo, data, sinopse):

    connection, cursor = connection_dao.get_connection(file)

    query = f"UPDATE isdb.episodio SET idtemporada = '{idtemporada}', iddiretor = '{iddiretor}', idescritor = '{idescritor}', temporada = '{temporada}', " \
            f"titulo = '{titulo}', data = '{data}' , sinopse = '{sinopse}' " \
            f"WHERE idepisodio = '{idepisodio}' and idserie = '{idserie}'"
    cursor.execute(query)
    connection.commit()

#----------------------------------------------------------------------------#

# exclusão de um episodeo
def excluiEpisodio(file, idepisodio):
    connection, cursor = connection_dao.get_connection(file)

    query = f"DELETE FROM isdb.episodio WHERE idepisodio = '{idepisodio}'"
    cursor.execute(query)
    connection.commit()

#----------------------------------------------------------------------------#

def getEpisodeos(file, idserie, idtemporada):
    connection, cursor = connection_dao.get_connection(file)

    query = f"select idepisodio as 'idepisodio', serie.nome as 'serie', temporada.ano as 'ano', diretor.nome as 'diretor', escritor.nome as 'escritor', episodio.titulo as 'titulo', episodio.data as 'data', episodio.sinopse " \
            f"from episodio " \
            f"LEFT JOIN serie ON serie.idserie = episodio.idserie " \
            f"LEFT JOIN escritor ON episodio.idescritor = escritor.idescritor " \
            f"LEFT JOIN diretor ON episodio.iddiretor = diretor.iddiretor " \
            f"INNER JOIN temporada ON temporada.idtemporada = episodio.idtemporada " \
            f"where episodio.idserie = '{idserie}' " \
            f"and episodio.idtemporada = '{idtemporada}'"
    cursor.execute(query)

    data = cursor.fetchall()

    episodios = []
    for episodio in data:
        _episodios = episodioV2_model.EpisodioV2(episodio[0],
                                                 episodio[1],
                                                 episodio[2],
                                                 episodio[3],
                                                 episodio[4],
                                                 episodio[5],
                                                 episodio[6],
                                                 episodio[7])
        episodios.append(_episodios)

    return episodios

#----------------------------------------------------------------------------#