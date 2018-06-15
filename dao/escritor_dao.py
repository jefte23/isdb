
from dao import connection_dao
from model import escritor_model

#----------------------------------------------------------------------------#

def get_escritor (file, idescritor):

    connection, cursor = connection_dao.get_connection(file)

    query = f"SELECT * FROM isdb.escritor where idescritor = '{idescritor}'"
    cursor.execute(query)

    data = cursor.fetchone()
    escritor = escritor_model.Escritor(idescritor,
                                       data[1],
                                       data[2],
                                       data[3],
                                       data[4])

    return escritor

#----------------------------------------------------------------------------#

def escritorAleatorios(file):

    connection, cursor = connection_dao.get_connection(file)

    cursor.execute(f"SELECT * FROM isdb.escritor ORDER BY RAND() LIMIT 6;")

    data = cursor.fetchall()

    escritor = []
    for esc in data:
        _escritor = escritor_model.Escritor (esc[0],
                                             esc[1],
                                             esc[2],
                                             esc[3],
                                             esc[4])

        escritor.append(_escritor)

    return escritor

#----------------------------------------------------------------------------#

def get_escritores(file):

    connection, cursor = connection_dao.get_connection(file)

    cursor.execute(f"SELECT * FROM isdb.escritor")

    data = cursor.fetchall()

    escritor = []
    for esc in data:
        _escritor = escritor_model.Escritor (esc[0],
                                             esc[1],
                                             esc[2],
                                             esc[3],
                                             esc[4])

        escritor.append(_escritor)

    return escritor

#----------------------------------------------------------------------------#

def cadastra_escritor(file, nome, datanascimento, nascionalidade, foto):

    connection, cursor = connection_dao.get_connection(file)

    query = f"INSERT INTO isdb.escritor (nome, datanascimento, nascionalidade, foto) " \
            f"VALUES ('{nome}', '{datanascimento}', '{nascionalidade}', '{foto}')"

    cursor.execute(query)
    connection.commit()

    connection.close()

#----------------------------------------------------------------------------#

def atualizar_diretor(file, idescritor, nome, datanascimento, nascionalidade, foto):

    connection, cursor = connection_dao.get_connection(file)

    query = f"UPDATE isdb.escritor " \
            f"SET nome = '{nome}', isdb.escritor = '{datanascimento}', nascionalidade = '{nascionalidade}', " \
            f"foto) = {foto}' " \
            f"WHERE idator = '{idescritor}'"

    cursor.execute(query)
    connection.commit()

    connection.close()

#----------------------------------------------------------------------------#

def excluir_escritor(file, idescritor):

    connection, cursor = connection_dao.get_connection(file)

    query = f"DELETE FROM isdb.escritor where idescritor = '{idescritor}'"

    cursor.execute(query)
    connection.commit()

#----------------------------------------------------------------------------#

def buscaEscritor(file, palavraChave):
    connection, cursor = connection_dao.get_connection(file)

    query = f"SELECT * FROM isdb.escritor WHERE upper(nome) like upper('%{palavraChave}%') or upper(nascionalidade) like upper('%{palavraChave}%')";

    cursor.execute(query)
    data = cursor.fetchall()

    escritor = []
    for esc in data:
        _escritor = escritor_model.Escritor (esc[0],
                                             esc[1],
                                             esc[2],
                                             esc[3],
                                             esc[4])

        escritor.append(_escritor)

    return escritor