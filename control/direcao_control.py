from control import app, mysql
from flask import render_template, request
from dao import serie_dao, elenco_dao, temporada_dao, episodeo_dao, diretor_dao, escritor_dao, banner_dao

@app.route('/cadastrarDirecao')
def cadastrarDirecao():

    tipo = request.args.get('tipo')
    nome = request.args.get('nome')
    datanasciomento = request.args.get('datanasciomento')
    nascionalidade = request.args.get('nascionalidade')
    foto = request.args.get('foto')

    print("tipo", tipo)
    print("nome", nome)
    print("datanasciomento", datanasciomento)
    print("nascionalidade", nascionalidade)
    print("foto", foto)

    if tipo == 'dir':
        diretor_dao.cadastra_diretor(mysql, nome, datanasciomento, nascionalidade, foto)

    elif tipo == 'esc':
        escritor_dao.cadastra_escritor(mysql, nome, datanasciomento, nascionalidade, foto)

    seriesAleatorias = serie_dao.get_seriesAleatoria(mysql)
    elencoAleatorio = elenco_dao.get_atoresAleatorio(mysql)
    banner = banner_dao.bannerAleatorio(mysql)
    dirAleatorio = diretor_dao.diretorAleatorio(mysql)
    escAleatorio = escritor_dao.escritorAleatorios(mysql)
    diretores = diretor_dao.get_diretores(mysql)
    escritores = escritor_dao.get_escritores(mysql)
    netflix = netflix_dao.netflixAleatoria(mysql)

    return render_template("index.html", series = seriesAleatorias, elenco = elencoAleatorio,
                           banner = banner, diretores = diretores, escritores = escritores,
                           escAleatorio = escAleatorio, dirAleatorio = dirAleatorio, netflix = netflix)
