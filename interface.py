from unicurses import *
import arquivos, vendas

def logo():
    cores()
    mvaddstr(1, 0, "-"*80)
    mvaddstr(2, 32, "OFICINA DO ZE")
    mvaddstr(3, 0, "-"*80)
    return 0

def op1(stdscr, chave):
    if chave == 1:
        mvaddstr(5, 7, "Cadastrar produto", A_REVERSE)
    else:
        mvaddstr(5, 7, "Cadastrar produto")

def op2(stdscr, chave):
    if chave == 2:
        mvaddstr(6, 7, "Listar produtos", A_REVERSE)
    else:
        mvaddstr(6, 7, "Listar produtos")

def op3(stdscr, chave):
    if chave == 3:
        mvaddstr(7, 7, "Apagar produto", A_REVERSE)
    else:
        mvaddstr(7, 7, "Apagar produto")

def op4(stdscr, chave):
    if chave == 4:
        mvaddstr(8, 7, "Alterar estoque", A_REVERSE)
    else:
        mvaddstr(8, 7, "Alterar estoque")

def op5(stdscr, chave):
    if chave == 5:
        mvaddstr(9, 7, "Realizar venda", A_REVERSE)
    else:
        mvaddstr(9, 7, "Realizar venda")

def op6(stdscr, chave):
    if chave == 6:
        mvaddstr(10, 7, "Listar vendas", A_REVERSE)
    else:
        mvaddstr(10, 7, "Listar vendas")

def main():
    cores()
    stdscr = initscr()
    chave = 1

    while True:

        erase()
        logo()
        mvaddstr(5, 60, "(esc para sair)")
        op1(stdscr, chave)
        op2(stdscr, chave)
        op3(stdscr, chave)
        op4(stdscr, chave)
        op5(stdscr, chave)
        op6(stdscr, chave)
        mvaddstr(12, 0, "-"*80)

        curs_set(False) # Impede que o traco de digitacao apareca
        key = getch()

        if key == 27:
            erase()
            noecho()
            mvaddstr(10, 15, "Saindo do sistema... (Qualquer tecla para sair)")
            getch()
            break
        elif key == 10: #enter
            if chave == 1: #opcao 1
                cadastraProduto(stdscr)
            elif chave == 2: #opcao 2
                listaProdutos(stdscr)
            elif chave == 3: #opcao 3
                apagaProduto(stdscr)
            elif chave == 4: #opcao 4
                editaEstoque(stdscr)
            elif chave == 5: #opcao 5
                realizaVenda(stdscr)
            elif chave == 6: #opcao 6
                listaVendas(stdscr)
        elif key == 119:
            if chave > 1:
                chave -= 1
            else:
                chave = 6
        elif key == 115:
            if chave < 6:
                chave += 1
            else:
                chave = 1

    endwin()
    return 0

def ajeita(name):
    name = str(name)
    name = name[2:len(name)-1]
    return name

def pegaCodigo(stdscr):
    cores()
    while True:
        codigo = ajeita(stdscr.getstr(9, 20, 5))
        if (arquivos.getProduto(codigo)):
            mvaddstr(9, 20, "          >> ERRO: Codigo em uso", color_pair(1))
        else:
            mvaddstr(9, 30, ">> OK                  ", color_pair(2))
            break
    return codigo

def pegaNome(stdscr):
    cores()
    while True:
        nome = ajeita(stdscr.getstr(10, 20, 20))
        if (len(nome) == 0):
            mvaddstr(10, 20, "          >> ERRO: Nome invalido", color_pair(1))
        else:
            mvaddstr(10, 30, ">> OK                  ", color_pair(2))
            break
    return nome.upper()

def pegaPreco(stdscr):
    cores()
    while True:
        mvaddstr(11, 20, " "*10)
        preco = ajeita(stdscr.getstr(11, 20, 10))
        if float(preco) >= 0:
            mvaddstr(11, 30, ">> OK                              ", color_pair(2))
            break
        mvaddstr(11, 20, "          >> ERRO: preco deve ser positivo.", color_pair(1))
    return preco

def pegaEstoque(stdscr):
    cores()
    while True:
        mvaddstr(12, 20, " "*10)
        estoque = ajeita(stdscr.getstr(12, 20, 10))
        if int(estoque) >= 0:
            mvaddstr(12, 30, ">> OK                           ", color_pair(2))
            break
        mvaddstr(12, 30, ">> ERRO: Estoque deve ser positivo.", color_pair(1))
    return estoque

def cadastraProduto(stdscr):
    cores()

    while True:
        erase()
        logo()
        mvaddstr(4, 24, "CADASTRO DE PRODUTOS E SERVICOS")
        mvaddstr(5, 0, "-"*80)
        noecho()
        mvaddstr(7, 26, "(1)SERVICO OU (2)PRODUTO?       (esc para cancelar)\n")
        tipo = getch()
        mvaddstr(8, 0, " ") # APAGAR A OPCAO DIGITADA ACIMA
        echo()
        if tipo == 27:
            break
        elif tipo == 49: # Servico
            curs_set(True)
            tipo = "s"
            mvaddstr(9, 0, "Codigo do servico: ")
            codigo = pegaCodigo(stdscr)
            mvaddstr(10, 0, "Nome do servico:   ")
            nome = pegaNome(stdscr)
            mvaddstr(11, 0, "Preco do servico: ")
            preco = pegaPreco(stdscr)
            estoque = 0

            arquivos.cadastraProduto(tipo, codigo, nome, preco, estoque)
            noecho()
            curs_set(False)
            mvaddstr(14, 20, "PRODUTO CADASTRADO", color_pair(2))
            getch()

        elif tipo == 50: # produto
            curs_set(True)
            tipo = "p"
            mvaddstr(9, 0, "Codigo do produto: ")
            codigo = pegaCodigo(stdscr)
            mvaddstr(10, 0, "Nome do produto:   ")
            nome = pegaNome(stdscr)
            mvaddstr(11, 0, "Preco do produto: ")
            preco = pegaPreco(stdscr)
            mvaddstr(12, 0, "Estoque: ")
            estoque = pegaEstoque(stdscr)

            arquivos.cadastraProduto(tipo, codigo, nome, preco, estoque)
            noecho()
            curs_set(False)
            mvaddstr(14, 20, "PRODUTO CADASTRADO", color_pair(2))
            getch()

    return 0

def listaProdutos(stdscr):
    produtos = arquivos.listaProdutos()
    erase()
    logo()
    mvaddstr(4, 30, "LISTA DE PRODUTOS")
    mvaddstr(5, 0, "-"*80)
    mvaddstr(6, 0, "CODIGO |")
    mvaddstr(6, 30, "NOME")
    mvaddstr(6, 52, "|   PRECO")
    mvaddstr(6, 69, "|  ESTOQUE ")
    mvaddstr(7, 0, "-"*80)

    for i in range(len(produtos)):
        mvaddstr(8+i, 0, "%7s" % (produtos[i][1]))
        mvaddstr(8+i, 7, "| %s" % (produtos[i][2]))
        mvaddstr(8+i, 52, "| %6.2f" % (float(produtos[i][3])))
        mvaddstr(8+i, 69, "| %8s" % (produtos[i][4]))

    getch()
    return 0

def apagaProduto(stdscr):
    erase()
    logo()
    cores()
    mvaddstr(4, 31, "DELETAR UM PRODUTO")
    mvaddstr(5, 0, "-"*80)
    curs_set(True)
    echo()
    mvaddstr(7, 0, "Codigo: ")
    codigo = ajeita(stdscr.getstr(7, 10, 10))
    apagou = arquivos.apagaProduto(codigo)
    noecho()
    curs_set(False)
    if (apagou):
        mvaddstr(7, 30, ">> PRODUTO APAGADO (Enter para continuar)", color_pair(2))
    else:
        mvaddstr(7, 30, ">> PRODUTO NAO ENCONTRADO (Enter para continuar)", color_pair(1))
    getch()

    return 0

def editaEstoque(stdscr):
    erase()
    logo()
    cores()
    mvaddstr(4, 28, "MUDANCA DE ESTOQUE")
    mvaddstr(5, 0, "-"*80)
    echo()
    mvaddstr(7, 0, "Codigo do produto:")
    codigo = ajeita(stdscr.getstr(7, 25, 10))
    if (arquivos.getTipo(codigo) != None):
        if (arquivos.getTipo(codigo) == "p"):
            mvaddstr(7, 30, ">> Produto encontrado", color_pair(2))
            mvaddstr(8, 0, "Quantidade a se retirar: ")
            retirarEstoque = ajeita(stdscr.getstr(8, 25, 10))
            noecho()
            curs_set(False)
            if(arquivos.alteraEstoque(codigo, int(retirarEstoque)) == True):
                mvaddstr(8, 30, ">> Estoque atualizado", color_pair(2))
            else:
                mvaddstr(8, 30, ">>ERRO: Quantidade invalida", color_pair(1))
        else:
            noecho()
            curs_set(False)
            mvaddstr(7, 30, ">> ERRO: Codigo se refere a um servico", color_pair(1))
    else:
        noecho()
        curs_set(False)
        mvaddstr(7, 20, "Produto nao encontrado", color_pair(1))
    getch()
    return 0

def realizaVenda(stdscr):
    continuar = ord("s")
    itens = []
    cores()
    while continuar == 115: #"s"
        erase()
        logo()
        echo()
        curs_set(True)
        mvaddstr(4, 31, "CAIXA DE VENDAS")
        mvaddstr(5, 0, "-"*80)
        mvaddstr(7, 0, "Codigo do produto:")
        codigo = ajeita(stdscr.getstr(7, 25, 10))
        produto = arquivos.getProduto(codigo)
        if (produto != None):
            mvaddstr(7, 30, ">> Produto encontrado", color_pair(2))
            mvaddstr(8, 0, "Quantidade:")
            quantidade = ajeita(stdscr.getstr(8, 25, 10))
            if (arquivos.alteraEstoque(codigo, quantidade)):
                itens.append("%s|%s" % (quantidade, codigo))
                mvaddstr(8, 30, ">> Registrado", color_pair(2))
            else:
                mvaddstr(8, 30, ">>ERRO: Venda nao registrada", color_pair(1))
            mvaddstr(10, 0, "continuar? (s/n)")
            continuar = getch()
        else:
            noecho()
            curs_set(False)
            mvaddstr(7, 20, "Produto nao encontrado", color_pair(1))
            getch()

    vendas.realizaVenda(itens)

    return 0

def listaVendas(stdscr):
    venda = vendas.getVendas()

    erase()
    logo()
    mvaddstr(4, 29, "HISTORICO DE VENDAS")
    mvaddstr(5, 0, "-"*80)
    linha = 6

    for i in range(len(venda)):
        codigos = venda[i][1]
        quantidade = venda[i][2]
        mvaddstr(linha+i, 0, "Venda realizada em: %s" % (venda[i][0]))
        mvaddstr(linha+1+i, 0, " CODIGO |")
        mvaddstr(linha+1+i, 18, "NOME")
        mvaddstr(linha+1+i, 32, "| ESTOQUE")
        mvaddstr(linha+1+i, 42, "|   PRECO")
        mvaddstr(linha+1+i, 54, "| QUANTIDADE")
        mvaddstr(linha+1+i, 67, "| VALOR TOTAL")

        for j in range(len(codigos)):
            produto = arquivos.getProduto(codigos[j])
            mvaddstr(linha+2+j+i, 0, " %s" % produto[1])
            mvaddstr(linha+2+j+i, 8, "| %s" % produto[2])
            mvaddstr(linha+2+j+i, 32, "| %3s" % produto[4])
            mvaddstr(linha+2+j+i, 42, "| %6.2f" % float(produto[3]))
            mvaddstr(linha+2+j+i, 54, "| %6s" % quantidade[j])
            total = float(quantidade[j])*float(produto[3])
            mvaddstr(linha+2+j+i, 67, "| %5.2f" % total)
        linha=linha+2+len(codigos)
    getch()
    return 0

def cores():
    start_color()
    init_pair(1, COLOR_RED, COLOR_BLACK)
    init_pair(2, COLOR_GREEN, COLOR_BLACK)

main()
