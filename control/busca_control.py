from control import app, mysql
from flask import render_template, request
from dao import serie_dao, elenco_dao, temporada_dao, episodeo_dao, diretor_dao, escritor_dao, banner_dao, netflix_dao


@app.route('/buscaValores')
def buscaValores():

    tipo = request.args.get("tipo")
    palavrachave = request.args.get("palavrachave")

    if tipo == 'art':
        elenco_dao

    if tipo == 'ser':
        serie_dao

    elif tipo == 'dir':
        diretor_dao

    elif tipo == 'dir':
        escritor_dao

    elif tipo == 'gen':
        serie_dao

    elif tipo == 'ano':
        temporada_dao

