import random

forca = random.randint(10, 20)
vida = random.randint(90, 115)
velocidade = random.randint(7, 15)
inteligencia = random.randint(270, 330)
resistencia = random.randint(50, 70)

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

def criar_item(nome, tipo, dano, efeito, quantidade=0):
    return {
        "nome": nome,
        "tipo": tipo,
        "dano": dano,
        "quantidade": quantidade,
        "efeito": efeito
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

def itens_aleatórios():#!!!!!!!!!!!!!!!!!!!!!!!!!!!!! a ideia é ter varias funçoes dentro dessa, 
    #cada outra função com um item aleatório encontrado durante a história
    pass

def adicionar_item_inventario(inventario, item):#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    while True:
        item = input("Deseja adicionar este item ao seu inventário?(S/N)\n").upper()
        inventario_atualizado = recursos_itens_inventario(inventario).append(itens_aleatórios())
        if item == "S":
            print(inventario_atualizado)
            return inventario_atualizado
        elif item == "N":
            break
        else:
            print("Opção inválida, tente novamente.")
            return

def usar_item_inventario(inventario, item):#?
    pass