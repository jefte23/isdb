from control import app, mysql
from flask import render_template, request
from dao import serie_dao, elenco_dao, temporada_dao, episodeo_dao, diretor_dao, escritor_dao, banner_dao, netflix_dao


@app.route('/buscaValores')
def buscaValores():

    tipo = request.args.get("tipo")
    palavrachave = request.args.get("palavrachave")

    if tipo == 'art':
        artista = elenco_dao.buscaAtor(mysql, palavrachave)
        return render_template("resultadoArtista.html", artista = artista, palavra = palavrachave)


    if tipo == 'ser':
        serie = serie_dao.buscaSerie(mysql, palavrachave)
        return render_template("resultadoSerie.html", serie = serie, palavra = palavrachave )


    elif tipo == 'dir':
        diretor = diretor_dao.buscaDiretor(mysql, palavrachave)
        return render_template("resultadoDiretor.html", diretor = diretor,  palavra = palavrachave)


    elif tipo == 'esc':
        escritor = escritor_dao.buscaEscritor(mysql, palavrachave)
        return render_template("resultadoEscritor.html", escritor = escritor, palavra = palavrachave)


    elif tipo == 'gen':
        serie = serie_dao.buscaGenero(mysql, palavrachave)
        return render_template("resultadoGenero.html", serie = serie, palavra=palavrachave)


    elif tipo == 'ano':

        temporada = temporada_dao.buscaTemporada(mysql, palavrachave)

        idserie = temporada_dao.buscaIdSerieTemporada(mysql)

        serie = []
        for sr in idserie:
            print(sr.idserie)
            _serie = serie_dao.get_serie(mysql, sr.idserie)

            serie.append(_serie)

        return render_template("resultadoTemporada.html", temporada = temporada, serie = serie, palavra=palavrachave)



