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


def aplicar_efeito_item(jogador, item):
    ganhos = []

    restaura_fome = item.get("restaura_fome", 0)
    if restaura_fome:
        antes = jogador.get("fome", 0)
        jogador["fome"] = min(100, antes + restaura_fome)
        ganhos.append(f"+{jogador['fome'] - antes} de fome")

    restaura_sede = item.get("restaura_sede", 0)
    if restaura_sede:
        antes = jogador.get("sede", 0)
        jogador["sede"] = min(100, antes + restaura_sede)
        ganhos.append(f"+{jogador['sede'] - antes} de sede")

    restaura_vida = item.get("restaura_vida", 0)
    if restaura_vida:
        antes = jogador.get("vida", 0)
        vida_maxima = jogador.get("vida_maxima", 100)
        jogador["vida"] = min(vida_maxima, antes + restaura_vida)
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
            if jogador is not None and item.get("categoria") == "recurso":
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