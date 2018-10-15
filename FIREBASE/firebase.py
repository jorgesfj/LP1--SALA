import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def create(code,dictionary):
    global db
    db.collection(u'product').document(code).set(dictionary)
    print("Cadastrado com Sucesso!")

def read(code):
    global db
    product_ref = db.collection(u'product')
    
    if(code=="ALL"):
        docs = product_ref.get()
        for doc in docs:
            print("{} => {}".format(doc.id,doc.to_dict()))
    else:
        product_ref.document(code)
        docs = product_ref.get()
        for doc in docs:
            print("{} => {}".format(doc.id,doc.to_dict()))
    
def update(code,dictionary):
    global db
    db.collection(u'product').document(code).update(dictionary)
    print("Atualizado com Sucesso!")

def delete(code):
    global db
    db.collection(u'product').document(code).delete()
    print("Removido com Sucesso!")
    
def menu():
    print("Sistema de estoque!")
    print("1 - Cadastro")
    print("2 - Consulta")
    print("3 - Editar")
    print("4 - Remover")
    option = int(input())
    
    # ===========create=========
    if(option==1):
        dictionary = {}
        print("codigo:")
        code=input()
        print("nome")
        dictionary["name"]=input()
        print("Preço")
        dictionary["price"]=float(input())
        create(code,dictionary)

    # ===========read===========
    if(option==2):
        print("Digite o codigo do produto ou ALL para carregar todos os produtos")
        code = input()
        read(code)

    #============update========
    if(option==3):
        dictionary = {}
        print("codigo:")
        code=input()
        print("nome")
        aux = input()
        if(aux!=''):
            dictionary["name"]=aux
        print("Preço")
        aux = input()
        if(aux!=''):
            dictionary["price"]=float(aux)
        update(code,dictionary)

    #============delete========
    if(option==4):
        print("codigo:")
        delete(input())

while(True):
    menu()