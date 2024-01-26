from flask import Blueprint

api_blueprint = Blueprint('api', __name__, url_prefix='/api')

@api_blueprint.route('/')
def index():
    return 'This is the API index page.'

@api_blueprint.route('/smth')
def something():
    return 'This is /api/smth endpoint.'
