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


def adicionar_item_inventario(inventario, item):
    if item is None:
        return inventario

    if not isinstance(item, dict):
        print("Erro: item inválido não pôde ser adicionado ao inventário.")
        return inventario

    for existente in inventario:
        if existente["nome"] == item["nome"]:
            existente["quantidade"] += item.get("quantidade", 1)
            return inventario

    inventario.append(item)
    return inventario


def usar_item_inventario(inventario, nome_item):
    for item in inventario:
        if item["nome"] == nome_item:
            item["quantidade"] -= 1
            print(f"{item['nome']} foi usado.")
            if item["quantidade"] <= 0:
                inventario.remove(item)
            return inventario

    print(f"{nome_item} não está no inventário.")
    return inventario