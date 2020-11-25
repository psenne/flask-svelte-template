from flask import Flask, send_from_directory, make_response, abort, request, jsonify
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import click

app = Flask(__name__,static_folder='client/public',static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.secret_key = 'secret!$#'

api = Api(app)
ma = Marshmallow(app)
db = SQLAlchemy(app)

from server.routes import *


@click.group()
def cli():
    pass

@cli.command()
@click.option('--debug', is_flag=True, help='start in debug mode')
@click.argument('port', default=3000)
def serve(port, debug):
    app.run(debug=debug, port=port)


@cli.command()
def initdb():
    click.echo('Creating the database')
    db.create_all()
    db.init_app(app)

if __name__ == '__main__':
    cli()
