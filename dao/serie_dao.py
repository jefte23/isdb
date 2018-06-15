from dao import connection_dao
from model import serie_model, avaliacao_model
#----------------------------------------------------------------------------#

def get_serie(file, idserie):
    connection, cursor = connection_dao.get_connection(file)

    query = f"SELECT * FROM isdb.serie WHERE idserie = '{idserie}'"
    cursor.execute(query)

    data = cursor.fetchone()
    serie = serie_model.Serie(idserie,
                              data[1],
                              data[2],
                              data[3],
                              data[4],
                              data[5])

    connection.close()

    return serie

#----------------------------------------------------------------------------#

def get_series(file):

    connection, cursor = connection_dao.get_connection(file)

    query = f"SELECT * FROM isdb.serie order by nome asc"
    cursor.execute(query)

    data = cursor.fetchall()

    series = []
    for srt in data:
        sr = serie_model.Serie(srt[0],
                               srt[1],
                               srt[2],
                               srt[3],
                               srt[4],
                               srt[5])

        series.append(sr)

    # connection.close()

    return series

#----------------------------------------------------------------------------#

def get_seriesAleatoria(file):

    connection, cursor = connection_dao.get_connection(file)

    query = f"SELECT * FROM isdb.serie ORDER BY RAND() LIMIT 18;"
    cursor.execute(query)

    data = cursor.fetchall()

    series = []
    for serie in data:
        sr = serie_model.Serie(serie[0],
                               serie[1],
                               serie[2],
                               serie[3],
                               serie[4],
                               serie[5])

        series.append(sr)


    #connection.close()

    return series


#----------------------------------------------------------------------------#
def cadastra_serie(file, nome, genero, canal, sinopse, banner):

    connection, cursor = connection_dao.get_connection(file)

    query = f"INSERT INTO isdb.serie (nome, genero, canal, sinopse, banner) VALUES ('{nome}', '{genero}', '{canal}', '{sinopse}', '{banner}');"

    cursor.execute(query)
    connection.commit()

#----------------------------------------------------------------------------#
def atualizar_serie(file, idserie, nome, genero, canal, sinopse, banner):

    connection, cursor = connection_dao.get_connection(file)

    query = f"UPDATE isdb.serie SET nome = '{nome}', genero = '{genero}, canal = '{canal}', " \
            f"sinopse = '{sinopse}', banner = '{banner}' " \
            f"WHERE idserie = '{idserie}"
    cursor.execute(query)
    connection.commit()


#----------------------------------------------------------------------------#
def excluir_serie(file, idserie):

    connection, cursor = connection_dao.get_connection(file)

    query = f"DELETE FROM isdb.serie WHERE idserie = '{idserie}'"
    cursor.execute(query)
    connection.commit()


#----------------------------------------------------------------------------#

def buscaSerie(file, palavraChave):

    connection, cursor = connection_dao.get_connection(file)
    query = f"SELECT * FROM isdb.serie WHERE upper(nome) like upper('%{palavraChave}%') or upper(sinopse) like upper('%{palavraChave}%');"

    cursor.execute(query)
    data = cursor.fetchall()

    series = []
    for srt in data:
        sr = serie_model.Serie(srt[0],
                               srt[1],
                               srt[2],
                               srt[3],
                               srt[4],
                               srt[5])

        series.append(sr)

    # connection.close()

    return series

#----------------------------------------------------------------------------#

def buscaGenero(file, palavraChave):
    connection, cursor = connection_dao.get_connection(file)

    query = f"SELECT * FROM isdb.serie WHERE upper(genero) like upper('%{palavraChave}%');"

    cursor.execute(query)

    data = cursor.fetchall()

    series = []
    for srt in data:
        sr = serie_model.Serie(srt[0],
                               srt[1],
                               srt[2],
                               srt[3],
                               srt[4],
                               srt[5])

        series.append(sr)

    # connection.close()

    return series

#----------------------------------------------------------------------------#

def cadastraAvaliacao(file, idserie, nome, avaliacao, avatar):

    connection, cursor = connection_dao.get_connection(file)

    query = f"INSERT INTO isdb.avaliacao (idserie, nome, avaliacao, avatar) VALUES ('{idserie}', '{nome}', '{avaliacao}', '{avatar}');"
    cursor.execute(query)
    connection.commit()

#----------------------------------------------------------------------------#

def buscaAvaliacao(file, idserie):

    connection, cursor = connection_dao.get_connection(file)
    query = f"SELECT * FROM isdb.avaliacao where idserie = '{idserie}';"

    cursor.execute(query)

    data = cursor.fetchall()

    avaliacao = []
    for ava in data:
        av = avaliacao_model.Avaliacao(ava[0],
                                       ava[1],
                                       ava[2],
                                       ava[3],
                                       ava[4])

        avaliacao.append(av)

    # connection.close()

    return avaliacao

#----------------------------------------------------------------------------#

def excluiAvaliacao(file, idserie):

    connection, cursor = connection_dao.get_connection(file)

    query = f"DELETE FROM isdb.avaliacao WHERE idserie = '{idserie}'"
    cursor.execute(query)
    connection.commit()
