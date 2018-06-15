
from dao import connection_dao
from model import diretor_model

#----------------------------------------------------------------------------#

def get_diretor (file, iddiretor):

    connection, cursor = connection_dao.get_connection(file)

    cursor.execute(f"SELECT * FROM isdb.diretor where iddiretor = '{iddiretor}'")

    data = cursor.fetchone()
    diretor = diretor_model.Diretor(iddiretor,
                                     data[1],
                                     data[2],
                                     data[3],
                                     data[4])


    return diretor

#----------------------------------------------------------------------------#
def diretorAleatorio(file):

    connection, cursor = connection_dao.get_connection(file)

    cursor.execute(f"SELECT * FROM isdb.diretor ORDER BY RAND() LIMIT 6;")

    data = cursor.fetchall()

    diretor = []
    for dir in data:
        _diretor = diretor_model.Diretor(dir[0],
                                         dir[1],
                                         dir[2],
                                         dir[3],
                                         dir[4])

        diretor.append(_diretor)

    return diretor


#----------------------------------------------------------------------------#
def get_diretores(file):

    connection, cursor = connection_dao.get_connection(file)

    cursor.execute(f"SELECT * FROM isdb.diretor")

    data = cursor.fetchall()

    diretor = []
    for dir in data:
        _diretor = diretor_model.Diretor(dir[0],
                                         dir[1],
                                         dir[2],
                                         dir[3],
                                         dir[4])

        diretor.append(_diretor)

    return diretor

#----------------------------------------------------------------------------#

def cadastra_diretor(file, nome, datanascimento, nascionalidade, foto):

    connection, cursor = connection_dao.get_connection(file)

    query = f"INSERT INTO isdb.diretor (nome, datanascimento, nascionalidade, foto) " \
            f"VALUES ('{nome}', '{datanascimento}', '{nascionalidade}', '{foto}')"

    cursor.execute(query)
    connection.commit()

    connection.close()

#----------------------------------------------------------------------------#

def atualizar_diretor(file, iddiretor, nome, datanascimento, nascionalidade, foto):

    connection, cursor = connection_dao.get_connection(file)

    query = f"UPDATE isdb.diretor " \
            f"SET nome = '{nome}', datanascimento = '{datanascimento}', nascionalidade = '{nascionalidade}', " \
            f"foto) = {foto}' " \
            f"WHERE idator = '{iddiretor}'"

    cursor.execute(query)
    connection.commit()

    connection.close()

#----------------------------------------------------------------------------#

def excluir_diretor(file, iddiretor):

    connection, cursor = connection_dao.get_connection(file)

    query = f"DELET FROM isdb.diretor where iddiretor = '{iddiretor}'"

    cursor.execute(query)
    connection.commit()

#----------------------------------------------------------------------------#

def buscaDiretor(file, palavraChave):
    connection, cursor = connection_dao.get_connection(file)

    query = f"SELECT * FROM isdb.diretor WHERE upper(nome) like upper('%{palavraChave}%') or upper(nascionalidade) like upper('%{palavraChave}%');"

    cursor.execute(query)

    data = cursor.fetchall()

    diretor = []
    for dir in data:
        _diretor = diretor_model.Diretor(dir[0],
                                         dir[1],
                                         dir[2],
                                         dir[3],
                                         dir[4])

        diretor.append(_diretor)

    return diretor