import random

forca = random.randint(10, 20)
vida = random.randint(90, 115)
velocidade = random.randint(7, 15)
inteligencia = random.randint(270, 330)
resistencia = random.randint(50, 70)

zFraco = criar_inimigo("Zumbi Fraco", 50, 10, 5, 20, 10) #nome, vida, forca, velocidade, inteligencia, resistencia
zMedio = criar_inimigo("Zumbi Médio", 100, 20, 10, 30, 20)
zForte = criar_inimigo("Zumbi Forte", 150, 30, 15, 40, 30)
boss1 = criar_inimigo("Zumbi Chefe", 200, 40, 20, 50, 40)
boss2 = criar_inimigo("Zumbi Supremo", 300, 50, 25, 60, 50)
bossFinal = criar_inimigo("Tchola", 500, 60, 30, 70, 60)

espada = criar_item("Espada", "arma", 20, "Causa dano ao inimigo", 10, 1)
machado = criar_item("Machado", "arma", 30, "Causa dano ao inimigo", 7, 1)

def criar_personagem(nome, vida=vida, forca=forca, velocidade=velocidade, inteligencia=inteligencia, resistencia=resistencia, inventario=None, fome=100, sede=100, xp=0, nivel=0):
    return {
        "nome": nome,
        "vida": vida,
        "forca": forca,
        "velocidade": velocidade,
        "inteligencia": inteligencia,
        "resistencia": resistencia,
        "inventario": inventario,
        "fome": fome,
        "sede": sede,
        "xp": xp,
        "nivel": nivel
    }

def criar_item(nome, tipo, dano, efeito, velocidade, quantidade=1):
    return {
        "nome": nome,
        "tipo": tipo,
        "dano": dano,
        "efeito": efeito,
        "velocidade": velocidade,
        "quantidade": quantidade,
    }

def criar_inimigo(nome, vida, forca, velocidade, inteligencia, resistencia):
    return {
        "nome": nome,
        "vida": vida,
        "forca": forca,
        "velocidade": velocidade,
        "inteligencia": inteligencia,
        "resistencia": resistencia
    }

def criar_recurso(nome, tipo, efeito, valorEf):
    return {
        "nome": nome,
        "tipo": tipo,
        "efeito": efeito,
        "valorEf": valorEf
    }

def recursos_itens_inventario(inventario):
    recursos = []
    itens = []
    inventario = recursos + itens
    for item in inventario:
        if item["tipo"] == "recurso":
            recursos.append(item)
        else:
            itens.append(item)
    return inventario

def mostrar_inventario(inventario):#mostra os recursos e itens do inventario
    recursos, itens = recursos_itens_inventario(inventario)
    print("Recursos:")
    for recurso in recursos:
        print(f"{recurso['nome']} --> {recurso['quantidade']} unidades")
    print("\nItens:")
    for item in itens:
        print(f"{item['nome']} --> {item['quantidade']} unidades")
    return recursos_itens_inventario


def inventario_vazio(inventario): # Vê se o inventario esta vazio
    if len(inventario) == 0:
        return "O inventário está vazio."
    else:
        return mostrar_inventario(inventario)

#------------------------------------------------------------------------------------------------------#
#---------------------------------precisa ver direito oq fazer aq--------------------------------------#
#----------------------------------------------|-------------------------------------------------------#
#----------------------------------------------v-------------------------------------------------------#

def itens_aleatórios():#!!!!!!!!!!!!!!!!!!!!!!!!!!!!! a ideia é ter varias funçoes dentro dessa, #cada outra função com um item aleatório encontrado durante a história
    pass

def adicionar_item_inventario(inventario, item):#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    while True:
        item = input("Deseja adicionar este item ao seu inventário?(S/N)\n").upper()
        inventario_atualizado = recursos_itens_inventario(inventario)
        inventario_atualizado.append(itens_aleatórios())
        if item == "S":
            print(inventario_atualizado)
            return inventario_atualizado
        elif item == "N":
            break
        else:
            print("Opção inválida, tente novamente.")
            return

def usar_item_inventario(inventario, item):
    if item in inventario:
        inventario.remove(item)
        print(f"{item['nome']} foi usado.")
    else:
        print(f"{item['nome']} não está no inventário.")