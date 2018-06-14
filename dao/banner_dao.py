from dao import connection_dao
from model import banner_model

def bannerAleatorio(file):

    connection, cursor = connection_dao.get_connection(file)

    query = f"SELECT * FROM isdb.banner ORDER BY RAND() LIMIT 3;"
    cursor.execute(query)

    data = cursor.fetchall()

    banner = []
    for bnn in data:
        bn = banner_model.Banner(bnn[0],
                                 bnn[1])

        banner.append(bn)


    return banner
