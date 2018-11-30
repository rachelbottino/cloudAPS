import requests
import json

#url padrão
url = 'localhost:5000/tarefas'
#comandos validos
comandos = ['listar', 'buscar', 'apagar', 'adicionar', 'atualizar']

#comandos do endpoint da APS 1
def listar():
	r = request.get(url=url)
	r.json()

def buscar(id):
	r = request.get(url=url+'/{id}')
	r.json()

def apagar(id):
	r = request.delete(url=url+'/{id}')
	r.json()

def adicionar(nome):
	nova_tarefa = json.dumps({"nome": nome})
	r = request.post(url=url, data=nova_tarefa)

def atualizar(id, nome):
	atualiza_tarefa = json.dumps({"nome": nome})
	r = request.put(url=url+'/{id}', data=atualiza_tarefa)

	#lendo argumentos
	if (sys.argv[0] == 'listar'):
		listar()

	elif (sys.argv[0] == 'buscar'):
		id_busca = sys.argv[1]
		buscar(id_busca)

	elif (sys.argv[0] == 'apagar'):
		id_apaga = sys.argv[1]
		apagar(id_apaga)

	elif (sys.argv[0] == 'adicionar'):
		nome_tarefa = sys.argv[1]
		adicionar(nome_tarefa)

	elif (sys.argv[0] == 'atualizar'):
		id_tarefa = sys.argv[1]
		nome_tarefa = sys.argv[2]
		atualizar(id_tarefa,nome_tarefa)

	else:
		print("Comandos validos: \n")
		for c in comandos:
			print(c"\n")
