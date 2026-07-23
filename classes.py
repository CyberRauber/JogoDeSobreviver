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