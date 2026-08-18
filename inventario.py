def recursos_itens_inventario(inventario):
    recursos = []
    itens = []

    for item in inventario:
        if item["categoria"] == "recurso":
            recursos.append(item)
        else:
            itens.append(item)

    return recursos, itens


def mostrar_inventario(inventario):
    if len(inventario) == 0:
        print("O inventário está vazio.")
        return

    recursos, itens = recursos_itens_inventario(inventario)

    if len(recursos) > 0:
        print("Recursos:")
        for recurso in recursos:
            print(f"{recurso['nome']} --> {recurso['quantidade']} unidades")

    if len(itens) > 0:
        print("\nItens:")
        for item in itens:
            print(f"{item['nome']} --> {item['quantidade']} unidades")


def inventario_vazio(inventario):
    if len(inventario) == 0:
        return True

    return False


def adicionar_item_inventario(inventario, item, mostrar=True):
    if item is None:
        return inventario

    for existente in inventario:
        if existente["nome"] == item["nome"]:
            existente["quantidade"] += item["quantidade"]

            if mostrar:
                print(f"\n+ {item['quantidade']}x {item['nome']} adicionado ao inventário.")
                mostrar_inventario(inventario)

            return inventario

    inventario.append(item)

    if mostrar:
        print(f"\n+ {item['quantidade']}x {item['nome']} adicionado ao inventário.")
        mostrar_inventario(inventario)

    return inventario


def aplicar_efeito_item(jogador, item):
    mostrou_efeito = False

    if item["restaura_fome"] > 0:
        jogador["fome"] += item["restaura_fome"]
        print(f"+{item['restaura_fome']} de fome")
        mostrou_efeito = True

    if item["restaura_sede"] > 0:
        jogador["sede"] += item["restaura_sede"]
        print(f"+{item['restaura_sede']} de sede")
        mostrou_efeito = True

    if item["restaura_vida"] > 0:
        jogador["vida"] += item["restaura_vida"]
        print(f"+{item['restaura_vida']} de vida")
        mostrou_efeito = True

    if item["bonus_forca"] > 0:
        jogador["forca"] += item["bonus_forca"]
        print(f"+{item['bonus_forca']} de forca")
        mostrou_efeito = True

    if item["bonus_resistencia"] > 0:
        jogador["resistencia"] += item["bonus_resistencia"]
        print(f"+{item['bonus_resistencia']} de resistencia")
        mostrou_efeito = True

    if item["bonus_velocidade"] > 0:
        jogador["velocidade"] += item["bonus_velocidade"]
        print(f"+{item['bonus_velocidade']} de velocidade")
        mostrou_efeito = True

    if item["bonus_inteligencia"] > 0:
        jogador["inteligencia"] += item["bonus_inteligencia"]
        print(f"+{item['bonus_inteligencia']} de inteligencia")
        mostrou_efeito = True

    if mostrou_efeito:
        print(f"Você sente os efeitos de {item['nome']}.")


def usar_item_inventario(inventario, nome_item, jogador=None):
    for item in inventario:
        if item["nome"].lower() == nome_item.lower():

            if jogador is not None:
                if item["categoria"] == "recurso":
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

    if len(inventario_lista) == 0:
        return

    recursos, itens = recursos_itens_inventario(inventario_lista)

    if len(recursos) == 0:
        return

    resposta = input("\nDigite o nome de um recurso para consumir, ou Enter para voltar: ").strip()

    if resposta == "":
        return

    usar_item_inventario(inventario_lista, resposta, jogador)
