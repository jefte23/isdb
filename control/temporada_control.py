from control import app, mysql
from flask import render_template, request
from dao import serie_dao, elenco_dao, temporada_dao, episodeo_dao, diretor_dao, escritor_dao

@app.route('/atualizarTemporada')
def atualizarTemporada():
    idtemporada = request.args.get('idtemporada')
    idserie = request.args.get('idserie')
    ano = request.args.get('ano')
    banner = request.args.get('banner')
    sinopse = request.args.get('sinopse')

    temporada_dao.atualizaTemporada(mysql, idtemporada, ano, sinopse, banner)

    serie = serie_dao.get_serie(mysql, idserie)
    temporada = temporada_dao.get_temporada(mysql, idtemporada)
    temporadas = temporada_dao.get_temporadas(mysql, idserie)

    trabalho = elenco_dao.get_elencoSerie(mysql, idtemporada)

    episodios = episodeo_dao.getEpisodeos(mysql, idserie, idtemporada)

    diretor = diretor_dao.get_diretores(mysql)
    escritor = escritor_dao.get_escritores(mysql)


    elenco = []
    for el in trabalho:
        print(el.idator)
        atores = elenco_dao.get_ator(mysql, el.idator)

        elenco.append(atores)

    return render_template("temporada.html", temporada = temporada, temporadas = temporadas, episodios = episodios, serie = serie, elenco = elenco, escritor = escritor, diretor = diretor)

@app.route('/cadastraEpisodio')
def cadastraEpisodio():
    idserie = request.args.get('idserie')
    idtemporada = request.args.get('idtemporada')
    iddiretor = request.args.get('iddiretor')
    idescritor = request.args.get('idescritor')
    temporada = request.args.get('temporada')
    titulo = request.args.get('titulo')
    data = request.args.get('data')
    sinopse = request.args.get('sinopse')


    serie = serie_dao.get_serie(mysql, idserie)
    temporada = temporada_dao.get_temporada(mysql, idtemporada)
    temporadas = temporada_dao.get_temporadas(mysql, idserie)

    trabalho = elenco_dao.get_elencoSerie(mysql, idtemporada)

    episodios = episodeo_dao.getEpisodeos(mysql, idserie, idtemporada)

    diretor = diretor_dao.get_diretores(mysql)
    escritor = escritor_dao.get_escritores(mysql)


    elenco = []
    for el in trabalho:
        print(el.idator)
        atores = elenco_dao.get_ator(mysql, el.idator)

        elenco.append(atores)

    return render_template("temporada.html", temporada = temporada, temporadas = temporadas, episodios = episodios, serie = serie, elenco = elenco, escritor = escritor, diretor = diretor)


@app.route('/atualizaEpisodio')
def atualizaEpisodio():
    idepisodio = request.args.get('idepisodio')
    idserie = request.args.get('idserie')
    idtemporada = request.args.get('idtemporada')
    iddiretor = request.args.get('iddiretor')
    idescritor = request.args.get('idescritor')
    temporada = request.args.get('temporada')
    titulo = request.args.get('titulo')
    data = request.args.get('data')
    sinopse = request.args.get('sinopse')

    serie = serie_dao.get_serie(mysql, idserie)
    temporada = temporada_dao.get_temporada(mysql, idtemporada)
    temporadas = temporada_dao.get_temporadas(mysql, idserie)

    trabalho = elenco_dao.get_elencoSerie(mysql, idtemporada)

    episodios = episodeo_dao.getEpisodeos(mysql, idserie, idtemporada)

    diretor = diretor_dao.get_diretores(mysql)
    escritor = escritor_dao.get_escritores(mysql)


    elenco = []
    for el in trabalho:
        print(el.idator)
        atores = elenco_dao.get_ator(mysql, el.idator)

        elenco.append(atores)

    return render_template("temporada.html", temporada = temporada, temporadas = temporadas, episodios = episodios, serie = serie, elenco = elenco, escritor = escritor, diretor = diretor)


@app.route('/excluirEpisodio')
def excluirEpisodio ():
    idepisodio = request.args.get('idepisodio')
    idserie = request.args.get('idserie')

    episodeo_dao.excluiEpisodio(mysql, idepisodio)

    serie = serie_dao.get_serie(mysql, idserie)
    trabalho = elenco_dao.get_elencoSerie(mysql, idserie)
    temporada = temporada_dao.get_temporadas(mysql, idserie)

    elenco = []
    for el in trabalho:
        atores = elenco_dao.get_ator(mysql, el.idator)

        elenco.append(atores)

    return render_template("serie.html", serie = serie, elenco = elenco, temporada = temporada)

@app.route('/excluirTemporada')
def excluirTemporada():

    idtemporada = request.args.get('idtemporada')

    elenco_dao.excluiTrabalhoIdTemporada(mysql, idtemporada)

    temporada_dao.excluiTemporada(mysql, idtemporada)

    seriesAleatorias = serie_dao.get_seriesAleatoria(mysql)
    todaSeries = serie_dao.get_series(mysql)

    return render_template("series.html", series = seriesAleatorias, todaSeries = todaSeries)

