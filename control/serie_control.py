from control import app, mysql
from flask import render_template, request
from dao import serie_dao, elenco_dao, temporada_dao, episodeo_dao, diretor_dao, escritor_dao, banner_dao, netflix_dao

@app.route('/')
def index():
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

@app.route('/series')
def series():
    seriesAleatorias = serie_dao.get_seriesAleatoria(mysql)
    todaSeries = serie_dao.get_series(mysql)


    return render_template("series.html", series = seriesAleatorias, todaSeries = todaSeries)

@app.route('/serie')
def serie():

    idserie = request.args.get('idserie')

    serie = serie_dao.get_serie(mysql, idserie)
    trabalho = elenco_dao.elencoTemporada(mysql, idserie)
    temporada = temporada_dao.get_temporadas(mysql, idserie)

    elenco = []
    for el in trabalho:
        atores = elenco_dao.get_ator(mysql, el.idator)

        elenco.append(atores)

    return render_template("serie.html", serie = serie, elenco = elenco, temporada = temporada)

@app.route('/cadastraserie')
def cadastraserie():
        idserie = request.args.get("idserie")
        ano = request.args.get('ano')
        sinopse = request.args.get('sinopse')
        banner = request.args.get('banner')

        # cadastra valores passados em formulario
        temporada_dao.cadastraTemporada(mysql, idserie, ano, sinopse, banner)

        # Carrega pagina com valores atualizados
        idserie = request.args.get('idserie')
        serie = serie_dao.get_serie(mysql, idserie)
        trabalho = elenco_dao.get_elencoSerie(mysql, idserie)
        temporada = temporada_dao.get_temporadas(mysql, idserie)

        elenco = []
        for el in trabalho:
            atores = elenco_dao.get_ator(mysql, el.idator)

            elenco.append(atores)

        return render_template("serie.html", serie = serie, elenco = elenco, temporada = temporada)


@app.route('/temporada')
def temporada():
    idserie = request.args.get("idserie")
    idtemp = request.args.get("idtemporada")

    serie = serie_dao.get_serie(mysql, idserie)
    temporada = temporada_dao.get_temporada(mysql, idtemp)
    temporadas = temporada_dao.get_temporadas(mysql, idserie)

    trabalho = elenco_dao.get_elencoSerie(mysql, idtemp)

    episodios = episodeo_dao.getEpisodeos(mysql, idserie, idtemp)

    diretor = diretor_dao.get_diretores(mysql)
    escritor = escritor_dao.get_escritores(mysql)


    elenco = []
    for el in trabalho:
        print(el.idator)
        atores = elenco_dao.get_ator(mysql, el.idator)

        elenco.append(atores)

    return render_template("temporada.html", temporada = temporada, temporadas = temporadas, episodios = episodios, serie = serie, elenco = elenco, escritor = escritor, diretor = diretor)


@app.route('/cadastraSerie')
def cadastraSerie():

    nome = request.args.get('nome')
    genero = request.args.get('genero')
    canal = request.args.get('canal')
    sinopse = request.args.get('sinopse')
    banner = request.args.get('banner')

    serie_dao.cadastra_serie(mysql, nome, genero, canal, sinopse, banner)

    seriesAleatorias = serie_dao.get_seriesAleatoria(mysql)
    todaSeries = serie_dao.get_series(mysql)

    return render_template("series.html", series = seriesAleatorias, todaSeries = todaSeries)








