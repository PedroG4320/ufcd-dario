def tipo_dia():
    dia = input("Dia: ").lower()
    match dia:
        case "sábado" | "domingo":
            print("Fim de semana")
        case "segunda" | "terça" | "quarta" | "quinta" | "sexta":
            print("Dia útil")
        case _:
            print("Dia inválido")


def classificacao_nota():
    nota = int(input("Nota: "))
    if nota >= 90:
        print("Excelente")
    elif nota >= 70:
        print("Bom")
    elif nota >= 50:
        print("Suficiente")
    else:
        print("Insuficiente")


def tipo_pedido():
    tipo = input("Tipo (compra/venda): ").lower()
    valor = float(input("Valor: "))
    pedido = {"tipo": tipo, "valor": valor}

    match pedido:
        case {"tipo": "compra", "valor": v}:
            print(f"Compra de {v}€")
        case {"tipo": "venda", "valor": v}:
            print(f"Venda de {v}€")
        case _:
            print("Pedido desconhecido")


def tipo_dado():
    valor = input("Digite algo: ")

    try:
        valor_int = int(valor)
        print("Número inteiro")
    except:
        try:
            valor_float = float(valor)
            print("Número decimal")
        except:
            if valor.startswith("[") and valor.endswith("]"):
                print("Lista")
            elif valor.isdigit():
                print("String numérica")
            else:
                print("String textual")


def analise_mensagem():
    msg = input("Mensagem: ").lower()

    match msg:
        case "olá" | "bom dia":
            print("Saudação")
        case _ if msg.endswith("?"):
            print("Pergunta")
        case _ if "tchau" in msg or "adeus" in msg:
            print("Despedida")
        case _:
            print("Mensagem genérica")


def estado_servidor():
    status = input("Status (ok/erro): ").lower()
    tempo = int(input("Tempo de resposta (ms): "))
    dados = {"status": status, "tempo_resposta": tempo}

    match dados:
        case {"status": "ok", "tempo_resposta": t} if t > 200:
            print("Servidor lento")
        case {"status": "ok"}:
            print("Servidor ativo")
        case {"status": "erro"}:
            print("Servidor indisponível")
        case _:
            print("Estado desconhecido")


def classificacao_produto():
    categoria = input("Categoria: ").lower()
    preco = float(input("Preço: "))
    produto = {"categoria": categoria, "preco": preco}

    match produto:
        case {"categoria": "eletrônico", "preco": p} if p > 1000:
            print("Produto de luxo")
        case {"categoria": "eletrônico", "preco": p}:
            print("Produto comum")
        case {"categoria": "alimento"}:
            print("Produto alimentar")
        case _:
            print("Categoria desconhecida")


def operacao_matematica():
    op = input("Operação: ").lower()
    n1 = float(input("Número 1: "))
    n2 = float(input("Número 2: "))

    match op:
        case "soma":
            print(n1 + n2)
        case "subtrai":
            print(n1 - n2)
        case "multiplica":
            print(n1 * n2)
        case "divide":
            print(n1 / n2 if n2 != 0 else "Erro: divisão por zero")
        case _:
            print("Operação inválida")


def processamento_requisicao():
    metodo = input("Método (GET/POST): ").upper()
    conteudo = input("Conteúdo: ")
    req = {"metodo": metodo, "conteudo": conteudo}

    match req:
        case {"metodo": "GET"}:
            print("Requisição GET recebida")
        case {"metodo": "POST", "conteudo": c} if c:
            print("Requisição POST com dados válidos")
        case {"metodo": "POST", "conteudo": ""}:
            print("Requisição POST sem dados")
        case _:
            print("Método não suportado")


def jogo():
    j1 = input("Jogador 1: ").lower()
    j2 = input("Jogador 2: ").lower()

    match (j1, j2):
        case (x, y) if x == y:
            print("Empate")
        case ("pedra", "tesoura") | ("tesoura", "papel") | ("papel", "pedra"):
            print("Jogador 1 venceu")
        case _:
            print("Jogador 2 venceu")


# MENU
while True:
    print("\n--- MENU ---")
    print("1 - Tipo de dia")
    print("2 - Classificação de nota")
    print("3 - Tipo de pedido")
    print("4 - Tipo de dado")
    print("5 - Análise de mensagem")
    print("6 - Estado do servidor")
    print("7 - Classificação de produto")
    print("8 - Operação matemática")
    print("9 - Processamento de requisição")
    print("10 - Pedra, Papel ou Tesoura")
    print("0 - Sair")

    opcao = input("Escolha: ")

    match opcao:
        case "1":
            tipo_dia()
        case "2":
            classificacao_nota()
        case "3":
            tipo_pedido()
        case "4":
            tipo_dado()
        case "5":
            analise_mensagem()
        case "6":
            estado_servidor()
        case "7":
            classificacao_produto()
        case "8":
            operacao_matematica()
        case "9":
            processamento_requisicao()
        case "10":
            jogo()
        case "0":
            print("Saindo...")
            break
        case _:
            print("Opção inválida")