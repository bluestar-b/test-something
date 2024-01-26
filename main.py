from flask import Flask
import os

app = Flask(__name__)

def register_routes(app):
    route_files = [file for file in os.listdir('routes') if file.endswith('.py')]
    for route_file in route_files:
        module_name = route_file[:-3]  # Remove the '.py' extension
        module = __import__(f'routes.{module_name}', fromlist=['routes'])
        blueprint = getattr(module, f'{module_name}_blueprint')
        app.register_blueprint(blueprint)


register_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
