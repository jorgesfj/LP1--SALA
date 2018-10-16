import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('p1lp1-e4bc1-firebase-adminsdk-xa5b0-fa875ede5b.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
def delete(codigo):
	global db
	db.collection(u'biblioteca').document(codigo).delete()
	print("REMOVIDO COM SUCESSO!!!")

def create(code,dicionario):
	global db
	db.collection(u'biblioteca').document(code).set(dicionario)
	print("CADASTRADO COM SUCESSO!!!\n")

def atualizar(codigo,dicionario):
	global db
	db.collection(u'biblioteca').document(codigo).update(dicionario)
	print("MUDANÇAS CADASTRADAS!!!")

def ler(codigo):
	global db
	livro_referencia = db.collection(u'biblioteca')
    
	if(codigo=="TODOS"):
		todos_livros = livro_referencia.get()
		for livrou in todos_livros:
			print("{} => {}".format(livrou.id,livrou.to_dict()))
	else:
		livro_referencia.document(codigo)
		todos_livros = livro_referencia.get()
		for livrou in docs:
			print("{} => {}".format(livrou.id,livrou.to_dict()))    
def menu():
	print("<<=====================Sistema de estoque!========================>>")
	print('''P1/LP1 2018.1                                      Desenvolvido por:Jorge Soares//Débora Silva//Savyo Nascimento''')
	print("1 - Cadastro")
	print("2 - Consulta")
	print("3 - Editar")
	print("4 - Remover")
	opcao = int(input())
	if (opcao == 1):
		dicionario = {}

		print("digite o título do livro")
		dicionario["nome"] = input()

		print("digite um código para o livro")
		code = input()
		dicionario["codigo"] = code

		print("digite o preco do livro")
		dicionario["preco"] = input()

		create(code,dicionario)	

	if (opcao==2):
		print("Informe o código do livro, ou 'TODOS' para se informar de todos os livros disponíveis.")
		codigo = input()
		ler(codigo)

	if (opcao==3):
		dicionario = {}
		print("Código do livro a ser Editado")
		codigo=input()
		print("Novo nome")
		aux = input()
		if(aux!=''):
			dicionario["nome"]=aux
		print("Novo preco")
		aux = input()
		if(aux!=''):
			dicionario["preco"]=float(aux)
		atualizar(codigo,dicionario)

	if (opcao==4):
		print("Código do livro a ser removido")
		codigo = input()
		delete(codigo)

while True:
	menu()
