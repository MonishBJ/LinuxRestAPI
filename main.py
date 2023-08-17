from flask import jsonify, Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)


class Hello(Resource):

    def get(self):
        return jsonify({'data': 'welcome to demo'})

    def post(self):
        return jsonify({'data': "vialsad"}), 201

api.add_resource(Hello,'/')

if __name__ == '__main__':
    app.run(debug=True)