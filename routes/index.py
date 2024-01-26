from flask import Blueprint
import platform
index_blueprint = Blueprint('index', __name__)

@index_blueprint.route('/')
def index():
    os_name = platform.system()
    full_cpu_name = platform.processor()
    return f"Running normally on {os_name}"