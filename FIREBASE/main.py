import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('p1lp1-e4bc1-firebase-adminsdk-xa5b0-fa875ede5b.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
def delete(codigo):
	global db
	db.collection(u'biblioteca').document(codigo).delete()

    print ("---------------------------------------------------------------------------")
	print("REMOVIDO COM SUCESSO!!!")
    print ("---------------------------------------------------------------------------")

def create(code,dicionario):
	global db
	db.collection(u'biblioteca').document(code).set(dicionario)

    print ("---------------------------------------------------------------------------")
	print("CADASTRADO COM SUCESSO!!!\n")
    print ("---------------------------------------------------------------------------")

def atualizar(codigo,dicionario):
	global db
	db.collection(u'biblioteca').document(codigo).update(dicionario)
    
    print ("---------------------------------------------------------------------------")
	print("MUDANÇAS CADASTRADAS!!!")
    print ("---------------------------------------------------------------------------")

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
	print("=======================================HELPBOOKS=======================================")
    
	print('''P1/LP1 2018.1                                      Desenvolvido por:Jorge Soares//Débora Barbosa//Savyo Nascimento''')
	print("1 - Cadastro")
	print("2 - Consulta")
	print("3 - Editar")
	print("4 - Remover")
	opcao = int(input())
	if (opcao == 1):
		dicionario = {}

		print ("---------------------------------------------------------------------------")
        print("Digite o título do livro:")
		print ("---------------------------------------------------------------------------")

        dicionario["nome"] = input()

		print ("---------------------------------------------------------------------------")
        print("Digite um código para o livro:")
		print ("---------------------------------------------------------------------------")
        code = input()
        print ("---------------------------------------------------------------------------")

		dicionario["codigo"] = code

		print ("---------------------------------------------------------------------------")
        print("Digite o preco do livro:")
        print ("---------------------------------------------------------------------------")

		dicionario["preco"] = input()

		create(code,dicionario)	

	if (opcao==2):
        print ("-------------------------------------------------------------------------------------")
		print("Informe o código do livro, ou 'TODOS' para se informar de todos os livros disponíveis:")
		print ("---------------------------------------------------------------------------")

        codigo = input()
		ler(codigo)

	if (opcao==3):
		dicionario = {}
        print ("---------------------------------------------------------------------------")
		print("Código do livro a ser Editado:")
		print ("---------------------------------------------------------------------------")

        codigo=input()

		print ("---------------------------------------------------------------------------")
        print("Novo nome:")
		print ("---------------------------------------------------------------------------")

        aux = input()

		if(aux!=''):
			dicionario["nome"]=aux
		print ("---------------------------------------------------------------------------")
        print("Novo preco:")
		print ("---------------------------------------------------------------------------")

        aux = input()

		if(aux!=''):
			dicionario["preco"]=float(aux)
		atualizar(codigo,dicionario)

	if (opcao==4):
        print ("---------------------------------------------------------------------------")
		print("Código do livro a ser removido:")
        print ("---------------------------------------------------------------------------")

		codigo = input()
		delete(codigo)

while True:
	menu()
