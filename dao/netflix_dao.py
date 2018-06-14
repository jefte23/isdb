from dao import connection_dao
from model import netflix_model

def netflixAleatoria(file):

    connection, cursor = connection_dao.get_connection(file)

    query = f"SELECT * FROM isdb.netflix ORDER BY RAND() LIMIT 6;"
    cursor.execute(query)

    data = cursor.fetchall()

    netflix = []
    for net in data:
        nt = netflix_model.Netflix(net[0],
                                   net[1],
                                   net[2])
        netflix.append(nt)


    return netflix
