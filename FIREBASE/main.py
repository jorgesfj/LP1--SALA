import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('p1lp1-e4bc1-firebase-adminsdk-xa5b0-fa875ede5b.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
def create(code,dicionario):
	global gb
	db.collection(u'biblioteca').document(code).set(dicionario)
	print("CADASTRADO COM SUCESSO!!!\n")
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

		print("digite um codigo para o livro")
		code = input()
		dicionario["codigo"] = code

		print("digite o preco do livro")
		dicionario["preco"] = input()

		create(code,dicionario)	

	if (opcao==2):
		print("Informe o código do livro, ou 'TODOS' para se informar de todos os livros disponíveis.")
		codigo = input()
		ler(codigo)
while True:
	menu()