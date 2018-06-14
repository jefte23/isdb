from dao import connection_dao
from model import elenco_model, trabalhos_model, elencoSerie_model
#----------------------------------------------------------------------------#
from model.trabalhos_model import Trabalhos


def get_atoresAleatorio(file):

    connection, cursor = connection_dao.get_connection(file)

    cursor.execute(f"SELECT * FROM isdb.ator ORDER BY RAND() LIMIT 24")
    data = cursor.fetchall()

    atores = []
    for ator in data:
        atr = elenco_model.Ator(ator[0],
                                ator[1],
                                ator[2],
                                ator[3],
                                ator[4],
                                ator[5])

        atores.append(atr)

    return atores

#----------------------------------------------------------------------------#

def get_elenco(file):

    connection, cursor = connection_dao.get_connection(file)

    cursor.execute(f"SELECT * FROM isdb.ator order by nome asc")
    data = cursor.fetchall()

    atores = []
    for ator in data:
        atr = elenco_model.Ator(ator[0],
                                ator[1],
                                ator[2],
                                ator[3],
                                ator[4],
                                ator[5])

        atores.append(atr)

    return atores

#----------------------------------------------------------------------------#
def get_ator(file, idator):

    connection, cursor = connection_dao.get_connection(file)

    cursor.execute(f"SELECT * FROM isdb.ator where idator = '{idator}'")

    data = cursor.fetchone()

    ator = elenco_model.Ator(idator,
                             data[1],
                             data[2],
                             data[3],
                             data[4],
                             data[5])


    return ator
#----------------------------------------------------------------------------#

def get_cadastraTrabalho(file, idator, idserie, idtemporada):

    connection, cursor = connection_dao.get_connection(file)

    query = f"INSERT INTO isdb.trabalhos (idator, idserie, idtemporada) " \
            f"VALUES ('{idator}', '{idserie}', '{idtemporada}')"

    cursor.execute(query)
    connection.commit()

#----------------------------------------------------------------------------#

def get_trabalho(file, idator):

    connection, cursor = connection_dao.get_connection(file)

    query = f"SELECT * FROM isdb.trabalhos WHERE idator = '{idator}';"

    cursor.execute(query)
    data = cursor.fetchall()

    trabalhos = []
    for trb in data:
        tb = trabalhos_model.Trabalhos(trb[0],
                                       trb[1],
                                       trb[2],
                                       trb[3])

        trabalhos.append(tb)

    return trabalhos

#----------------------------------------------------------------------------#

def elencoTemporada(file, idserie):
    connection, cursor = connection_dao.get_connection(file)

    query = f"SELECT distinct idator, idserie FROM isdb.trabalhos WHERE idserie = '{idserie}';"

    cursor.execute(query)
    data = cursor.fetchall()

    trabalhos = []
    for trb in data:
        tb = elencoSerie_model.ElncoSerie(trb[0],
                                          trb[1])

        trabalhos.append(tb)

    return trabalhos




#----------------------------------------------------------------------------#
def get_elencoSerie(file, idtemp):
    connection, cursor = connection_dao.get_connection(file)

    query = f"SELECT * FROM isdb.trabalhos where idtemporada = '{idtemp}';"

    cursor.execute(query)
    data = cursor.fetchall()

    trabalhos = []
    for trb in data:
        tb = trabalhos_model.Trabalhos(trb[0],
                                       trb[1],
                                       trb[2],
                                       trb[3])

        trabalhos.append(tb)

    return trabalhos

#----------------------------------------------------------------------------#

def cadastrar_ator(file, nome, biografia, datanascimento, nascionalidade, foto):

    connection, cursor = connection_dao.get_connection(file)

    query = f"INSERT INTO isdb.ator (nome, biografia, datanascimento, nascionalidade, foto) " \
            f"VALUES ('{nome}', '{biografia}', '{datanascimento}', '{nascionalidade}', '{foto}')"
    cursor.execute(query)
    connection.commit()

#----------------------------------------------------------------------------#

def excluir_ator(file, idator):

    connection, cursor = connection_dao.get_connection(file)

    query = f"DELET FROM isdb.ator where idator = '{idator}''"
    cursor.execute(query)
    connection.commit()

#----------------------------------------------------------------------------#
def excluiTrabalho(file, idserie):
    connection, cursor = connection_dao.get_connection(file)

    query = f"DELET FROM isdb.trabalhos where idserie = '{idserie}'"
    cursor.execute(query)
    connection.commit()


#----------------------------------------------------------------------------#
def atualizar_ator(file, idator, nome, datanascimento, nascionalidade, foto):

    connection, cursor = connection_dao.get_connection(file)

    query = f"UPDATE isdb.ator SET nome = '{nome}', datanascimento = '{datanascimento}', " \
            f"nascionalidade = '{nascionalidade}', " \
            f"foto) = {foto}' WHERE idator = '{idator}'"
    cursor.execute(query)
    connection.commit()