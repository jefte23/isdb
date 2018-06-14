from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = "root"
app.config["MYSQL_DATABASE_DB"] = "isdb"

mysql = MySQL(app)
mysql.init_app(app)

import control.elenco_control
import control.direcao_control
import control.serie_control
import control.temporada_control
import control.busca_control

app.run(debug=True)