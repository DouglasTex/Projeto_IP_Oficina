from datetime import datetime
import arquivos

def realizaVenda(itens):

    now = datetime.now()
    data = "%d/%d/%d %d:%d:%d" %(now.day, now.month, now.year, now.hour , now.minute, now.second)
    venda = data + ";"
    for i in range(len(itens)):
        venda = venda + itens[i]
        if i+1 < len(itens):
             venda = venda + ","

    arq = open("vendas.txt","a")
    arq.write(venda+"\n")
    arq.close()

def getVendas():
    vendas = []
    arq = open("vendas.txt","r")
    linhas = arq.read().splitlines()
    arq.close()
    for linha in linhas:
        codigos = []
        quantidade = []
        if len(linha) == 0:
            continue
        venda = linha.split(";")
        datahora = venda[0]
        codigosVenda = venda[1].split(",")
        for i in range(len(codigosVenda)):
            temp = codigosVenda[i].split("|")
            codigos.append(temp[1])
            quantidade.append(temp[0])

        vendas.append([datahora,codigos,quantidade])
    return vendas
