def recursos_itens_inventario(inventario):
    recursos = []
    itens = []
    for item in inventario:
        if item["tipo"] == "recurso":
            recursos.append(item)
        else:
            itens.append(item)
    return recursos, itens


def mostrar_inventario(inventario):
    recursos, itens = recursos_itens_inventario(inventario)
    print("Recursos:")
    for recurso in recursos:
        print(f"{recurso['nome']} --> {recurso['quantidade']} unidades")
    print("\nItens:")
    for item in itens:
        print(f"{item['nome']} --> {item['quantidade']} unidades")
    return recursos, itens


def inventario_vazio(inventario):
    if len(inventario) == 0:
        return "O inventário está vazio."
    else:
        return mostrar_inventario(inventario)


def adicionar_item_inventario(inventario, item):
    if item is None:
        return inventario

    if isinstance(item, dict):
        inventario.append(item)
        return inventario

    while True:
        resposta = input("Deseja adicionar este item ao seu inventário?(S/N)\n").upper()
        if resposta == "S":
            inventario.append(item)
            return inventario
        if resposta == "N":
            return inventario
        print("Opção inválida, tente novamente.")


def usar_item_inventario(inventario, item):
    if item in inventario:
        inventario.remove(item)
        print(f"{item['nome']} foi usado.")
    else:
        print(f"{item['nome']} não está no inventário.")
