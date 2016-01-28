from flask import Flask, jsonify, abort, make_response, request
import Pessoa


app = Flask(__name__)


_pessoa = Pessoa.Pessoa()
_pessoa.id = 1
_pessoa.nome = 'Welker Arantes'
_pessoa.idade = 23
_pessoa.telefone = '(64) 9296 4354'

Json = [
    {'id' : 1, 'nome' : _pessoa.nome, 'idade' : _pessoa.idade, 'telefone' : _pessoa.telefone}
]


@app.route('/service/api/all', methods=['GET'])
def retrieve_all():
    return jsonify({'pessoas': Json})


@app.route('/service/api/<int:id>', methods=['GET'])
def by_id(id):
    p = [p for p in Json if p['id'] == id]
    if len(p) == 0:
        abort(404)

    return jsonify({'pessoa': p[0]})


@app.route('/service/api/add', methods=['POST'])
def add():
    if not request.json or not 'id' in request.json or not 'nome' in request.json or not 'telefone' in request.json:
        abort(404)

    return jsonify({'response' : 'Url indisponivel'})


@app.route('/service/api/update/<int:id>', methods=['PUT'])
def update(id):
    if not request.json or id <= 0:
        abort(404)

    return jsonify({'response' : 'Url indisponivel'})


@app.route('/service/api/delete/<int:id>', methods=['DELETE'])
def delete(id):
    if not request.json or id <= 0:
        abort(404)

    return jsonify({'response' : 'Url indisponivel'})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)

if __name__ == '__main__':
    app.run(port=8080, debug=True)