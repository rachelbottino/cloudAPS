from flask import Flask, jsonify, abort, make_response, request, url_for
from flask.ext.httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

tarefas = [{
		'id':1,
		'nome': u'Buy Chocolates',
		},
		{
		'id':2,
		'nome': u'Learn Python',
		}]

'''
Method to convert tarefaid into tarefa URI
'''
def uri_tarefa(tarefa):
	nova_tarefa = {}
	for t in tarefa:
		if t == 'id':
			nova_tarefa['uri'] = url_for('lista_tarefa', id_tarefa = tarefa['id'], _external = True)
		else:
			nova_tarefa[t] = tarefa[t]
	return nova_tarefa

'''
Lista todas as tarefas
'''
@app.route('/tarefas', methods = ['GET'])
def lista_tarefas():
	return jsonify({'tarefas': [uri_tarefa(tarefa) for tarefa in tarefas]})

'''
Cria tarefa
'''
@app.route('/tarefas', methods = ['POST'])
def cria_tarefa():
	if not request.json or not 'nome' in request.json:
		abort(400)
	tarefa = {
	'id': tarefas[-1]['id']+1,
	'nome': request.json['nome'],
	}
	tarefas.append(tarefa)
	return jsonify({ 'tarefa' : tarefa }),201

'''
Atualiza tarefa
'''
@app.route('/tarefas/<int:id_tarefa>', methods = ['PUT'])
def atualiza_tarefa(id_tarefa):
	tarefa = filter(lambda t:t['id'] == id_tarefa, tarefas)
	if len(tarefa) == 0:
		abort(400)
	if not request.json:
		abort(400)
	if 'nome' in request.json and type(request.json['nome']) != unicode:
		abort(400)

	tarefa[0]['nome'] = request.json.get('nome', tarefa[0]['nome'])
	return jsonify({ 'tarefa' : tarefa[0] })

'''
Deleta tarefa
'''
@app.route('/tarefas/<int:id_tarefa>', methods = ['DELETE'])
def deleta_tarefa(id_tarefa):
	tarefa = filter(lambda t: t['id'] == id_tarefa, tarefas)
	if len(tarefa) == 0:
		abort(400)
	tarefas.remove(tarefa[0])
	return jsonify({ 'result': True })
	
'''
Mostra tarefa com id
'''
@app.route('/tarefas/<int:id_tarefa>', methods = ['GET'])
def lista_tarefa(id_tarefa):
	for t in tarefas:
		if t['id'] == id_tarefa:
			tarefa = t
			return jsonify({'tarefa' : t})
	abort(404)

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({ 'error' : 'Not Found' }), 404)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
