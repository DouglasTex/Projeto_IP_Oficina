def leArquivo():
    arq = open("produtos.txt","r")
    temp = arq.readlines()
    arq.close()
    return temp

def getProduto(codigo):
    linhas = leArquivo()
    produtos = []

    for linha in linhas:
        produto = linha.split(";")
        if produto[1] == codigo:
            return produto
    return None

def listaProdutos():
    arq = open("produtos.txt","r")

    produtos = []
    linhas = arq.read().splitlines()
    for linha in linhas:
        produto = linha.split(";")

        tipo = produto[0]
        codigo = produto[1]
        nome = produto[2]
        preco = produto[3]
        estoque = produto[4]

        produtos.append([tipo, codigo, nome, preco, estoque])
    arq.close()

    return produtos

def cadastraProduto(tipo, codigo, nome, preco, estoque):
    arq = open("produtos.txt","a")
    arq.write("%s;%s;%s;%s;%s;\n" % (tipo, codigo, nome, preco, estoque))
    arq.close()

def gravaArquivo(produtos):
    arq = open("produtos.txt","w")
    for produto in produtos:
        arq.write(produto)
    arq.close()

def getPreco(codigo):
    produtos = leArquivo()

    for i in range(len(produtos)):
        produto = produtos[i].split(";")
        if produto[1] == codigo:
            return produto[3]
    return None

def getTipo(codigo):
    produtos = leArquivo()

    for i in range(len(produtos)):
        produto = produtos[i].split(";")
        if produto[1] == codigo:
            return produto[0]
    return None

def existeProduto(codigo):
    produtos = leArquivo()

    for i in range(len(produtos)):
        produto = produtos[i].split(";")
        if produto[1] == codigo:
            return True
    return False

def apagaProduto(codigo):
    produtos = leArquivo()

    for i in range(len(produtos)):
        produto = produtos[i].split(";")
        if produto[1] == codigo:
            produtos[i] = ""
            gravaArquivo(produtos)
            return True
    return False

def atualizaProduto(produtos, produto, indice):
    produtoString = "%s;%s;%s;%s;%s;\n" % (produto[0], produto[1], produto[2], produto[3], produto[4])
    produtos[indice] = produtoString
    gravaArquivo(produtos)

def alteraEstoque(codigo, valor): # recebe o codigo e o valor a ser retirado

    produtos = leArquivo()
    for i in range(len(produtos)):
        produto = produtos[i].split(";")
        if produto[1] == codigo:
            if produto[0] == "p":
                if int(produto[4]) >= int(valor):
                    produto[4] = str(int(produto[4]) - int(valor))
                    atualizaProduto(produtos, produto, i)
                    return True
                else:
                    return False
            else:
                return True
