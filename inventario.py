import itens


def recursos_itens_inventario(inventario):
    recursos = []
    itens = []
    for item in inventario:
        if item.get("categoria") == "recurso":
            recursos.append(item)
        else:
            itens.append(item)
    return recursos, itens


def mostrar_inventario(inventario):
    if inventario_vazio(inventario):
        print("O inventário está vazio.")
        return

    recursos, itens = recursos_itens_inventario(inventario)

    if recursos:
        print("Recursos:")
        for recurso in recursos:
            print(f"{recurso['nome']} --> {recurso['quantidade']} unidades")

    if itens:
        print("\nItens:")
        for item in itens:
            print(f"{item['nome']} --> {item['quantidade']} unidades")


def inventario_vazio(inventario):
    return len(inventario) == 0


def adicionar_item_inventario(inventario, item, mostrar=True):
    if item is None:
        return inventario

    if not isinstance(item, dict):
        print("Erro: item inválido não pôde ser adicionado ao inventário.")
        return inventario

    for existente in inventario:
        if existente["nome"] == item["nome"]:
            existente["quantidade"] += item.get("quantidade", 1)
            if mostrar:
                print(f"\n+ {item.get('quantidade', 1)}x {item['nome']} adicionado ao inventário.")
                mostrar_inventario(inventario)
            return inventario

    inventario.append(item)
    if mostrar:
        print(f"\n+ {item.get('quantidade', 1)}x {item['nome']} adicionado ao inventário.")
        mostrar_inventario(inventario)
    return inventario


def quantidade_recurso(inventario, nome):
    for recurso in inventario:
        if recurso["nome"].lower() == nome.lower():
            return recurso["quantidade"]
    return 0


def remover_recurso(inventario, nome, quantidade):
    for recurso in inventario:
        if recurso["nome"].lower() == nome.lower():
            recurso["quantidade"] -= quantidade
            if recurso["quantidade"] <= 0:
                inventario.remove(recurso)
            return


def menu_criacao(jogador):
    inventario_lista = jogador["inventario"]

    while True:
        print("""
    CRIAÇÃO DE ITENS
    1 - Faca improvisada (1 madeira e 1 pedra)
    2 - Lança (1 madeira e 1 metal)
    3 - Bandagem (2 panos)
    4 - Kit médico (2 panos e 1 erva medicinal)
    0 - Voltar
""")
        escolha = input("Escolha um item para criar: ")

        if escolha == "1":
            if quantidade_recurso(inventario_lista, "madeira") >= 1 and quantidade_recurso(inventario_lista, "pedra") >= 1:
                remover_recurso(inventario_lista, "madeira", 1)
                remover_recurso(inventario_lista, "pedra", 1)
                novo_item = itens.criar_item("faca improvisada", "arma", 12, "dano médio", 1)
                adicionar_item_inventario(inventario_lista, novo_item, mostrar=False)
                print("\nFaca improvisada criada.")
                mostrar_inventario(inventario_lista)
            else:
                print("\nVocê não tem os recursos necessários.")
        elif escolha == "2":
            if quantidade_recurso(inventario_lista, "madeira") >= 1 and quantidade_recurso(inventario_lista, "metal") >= 1:
                remover_recurso(inventario_lista, "madeira", 1)
                remover_recurso(inventario_lista, "metal", 1)
                novo_item = itens.criar_item("lança", "arma", 18, "dano alto", 1)
                adicionar_item_inventario(inventario_lista, novo_item, mostrar=False)
                print("\nLança criada.")
                mostrar_inventario(inventario_lista)
            else:
                print("\nVocê não tem os recursos necessários.")
        elif escolha == "3":
            if quantidade_recurso(inventario_lista, "pano") >= 2:
                remover_recurso(inventario_lista, "pano", 2)
                novo_item = itens.criar_recurso("bandagem", "cura", "restaura 15 de vida", 1, restaura_vida=15)
                adicionar_item_inventario(inventario_lista, novo_item, mostrar=False)
                print("\nBandagem criada.")
                mostrar_inventario(inventario_lista)
            else:
                print("\nVocê não tem os recursos necessários.")
        elif escolha == "4":
            if quantidade_recurso(inventario_lista, "pano") >= 2 and quantidade_recurso(inventario_lista, "erva medicinal") >= 1:
                remover_recurso(inventario_lista, "pano", 2)
                remover_recurso(inventario_lista, "erva medicinal", 1)
                novo_item = itens.criar_recurso("kit médico", "cura", "restaura 30 de vida", 1, restaura_vida=30)
                adicionar_item_inventario(inventario_lista, novo_item, mostrar=False)
                print("\nKit médico criado.")
                mostrar_inventario(inventario_lista)
            else:
                print("\nVocê não tem os recursos necessários.")
        elif escolha == "0":
            return
        else:
            print("\nOpção inválida.")


def aplicar_efeito_item(jogador, item):
    ganhos = []

    restaura_fome = item.get("restaura_fome", 0)
    if restaura_fome:
        antes = jogador.get("fome", 0)
        jogador["fome"] = antes + restaura_fome
        if jogador["fome"] > 100:
            jogador["fome"] = 100
        ganhos.append(f"+{jogador['fome'] - antes} de fome")

    restaura_sede = item.get("restaura_sede", 0)
    if restaura_sede:
        antes = jogador.get("sede", 0)
        jogador["sede"] = antes + restaura_sede
        if jogador["sede"] > 100:
            jogador["sede"] = 100
        ganhos.append(f"+{jogador['sede'] - antes} de sede")

    restaura_vida = item.get("restaura_vida", 0)
    if restaura_vida:
        antes = jogador.get("vida", 0)
        jogador["vida"] = antes + restaura_vida
        if jogador["vida"] > jogador.get("vida_maxima", 100):
            jogador["vida"] = jogador.get("vida_maxima", 100)
        ganhos.append(f"+{jogador['vida'] - antes} de vida")

    for atributo, chave_bonus in (
        ("forca", "bonus_forca"),
        ("resistencia", "bonus_resistencia"),
        ("velocidade", "bonus_velocidade"),
        ("inteligencia", "bonus_inteligencia"),
    ):
        bonus = item.get(chave_bonus, 0)
        if bonus:
            jogador[atributo] = jogador.get(atributo, 0) + bonus
            ganhos.append(f"+{bonus} de {atributo}")

    if ganhos:
        print(f"Você sente os efeitos de {item['nome']}: {', '.join(ganhos)}.")


def usar_item_inventario(inventario, nome_item, jogador=None):
    for item in inventario:
        if item["nome"].lower() == nome_item.lower():
            if item.get("categoria") != "recurso" or item.get("tipo") not in ["comida", "bebida", "cura"]:
                print(f"\n{item['nome']} não pode ser consumido.")
                return inventario

            if jogador is not None:
                aplicar_efeito_item(jogador, item)

            item["quantidade"] -= 1
            print(f"\n{item['nome']} foi usado.")
            if item["quantidade"] <= 0:
                inventario.remove(item)

            mostrar_inventario(inventario)
            return inventario

    print(f"{nome_item} não está no inventário.")
    return inventario


def menu_inventario(jogador):
    inventario_lista = jogador["inventario"]
    mostrar_inventario(inventario_lista)

    if inventario_vazio(inventario_lista):
        return

    recursos, _ = recursos_itens_inventario(inventario_lista)
    if not recursos:
        return

    resposta = input(
        "\nDigite o nome de um recurso para consumir, ou Enter para voltar: "
    ).strip()
    if resposta == "":
        return

    usar_item_inventario(inventario_lista, resposta, jogador)
