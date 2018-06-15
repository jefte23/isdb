from builtins import print
import json
from control import app, mysql
from flask import render_template, request
from dao import serie_dao, elenco_dao, temporada_dao


@app.route('/artistas')
def artistas():
    series = serie_dao.get_series(mysql)
    elencoAleatorio = elenco_dao.get_atoresAleatorio(mysql)
    alencoCompleto = elenco_dao.get_elenco(mysql)

    return render_template("artistas.html", series = series, elenco = elencoAleatorio, elencoCompleto = alencoCompleto)

@app.route('/temporada1',methods=["GET", "POST"])
def temporada1():
    idserie = request.args.get('idserie')

    lista = temporada_dao.get_temporadas(mysql, idserie)
    ano  = []
    for v in lista:
        s = v.ano + "_" + str(v.idtemporada)
        ano.append(s)

    return json.dumps(ano)


@app.route('/artista', methods=["GET", "POST"])
def artista():

    idator = request.args.get('idator')
    artista = elenco_dao.get_ator(mysql, idator)
    trabalhos = elenco_dao.get_trabalho(mysql, idator)
    todaSeries = serie_dao.get_series(mysql)



    series = []
    for tr in trabalhos:
        sr = serie_dao.get_serie(mysql, tr.idserie)

        series.append(sr)



    if series == []:
        temporadas = []
        return render_template("artista.html", series=series, artista=artista, todaSeries=todaSeries, temporadas=temporadas)

    else:
        temporadas = temporada_dao.buscaTemporadaV2(mysql, idator)
        return render_template("artista.html", series=series, artista=artista, todaSeries=todaSeries, temporadas=temporadas)



@app.route('/cadastrarArtista')
def cadastrarArtista():
    nome = request.args.get('nome')
    biografia = request.args.get('biografia')
    datanascimento = request.args.get('datanascimento')
    nascionalidade = request.args.get('nascionalidade')
    foto = request.args.get('foto')

    elenco_dao.cadastrar_ator(mysql, nome, biografia, datanascimento, nascionalidade, foto)

    series = serie_dao.get_series(mysql)
    elencoAleatorio = elenco_dao.get_atoresAleatorio(mysql)
    alencoCompleto = elenco_dao.get_elenco(mysql)

    return render_template("artistas.html", series = series, elenco = elencoAleatorio, elencoCompleto = alencoCompleto)



@app.route('/cadastroTrabalho')
def cadastroTrabalho():
    idator = request.args.get('idator')
    idserie = request.args.get('idserie')
    idtemporada = request.args.get('idtemporada')

    elenco_dao.get_cadastraTrabalho(mysql, idator, idserie, idtemporada)

    artista = elenco_dao.get_ator(mysql, idator)
    trabalhos = elenco_dao.get_trabalho(mysql, idator)
    todaSeries = serie_dao.get_series(mysql)

    series = []
    for tr in trabalhos:
        sr = serie_dao.get_serie(mysql, tr.idserie)

        series.append(sr)


    if series == []:
        temporadas = []
        return render_template("artista.html", series=series, artista=artista, todaSeries=todaSeries, temporadas=temporadas)

    else:
        temporadas = temporada_dao.buscaTemporadaV2(mysql, idator)
        return render_template("artista.html", series=series, artista=artista, todaSeries=todaSeries, temporadas=temporadas)




