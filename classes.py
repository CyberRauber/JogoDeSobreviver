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
        "nivel": nivel,
    }


def criar_inimigo(nome, vida, forca, velocidade, inteligencia, resistencia):
    return {
        "nome": nome,
        "vida": vida,
        "forca": forca,
        "velocidade": velocidade,
        "inteligencia": inteligencia,
        "resistencia": resistencia,
    }


zFraco = criar_inimigo("Zumbi Fraco", 50, 10, 5, 20, 10)
zMedio = criar_inimigo("Zumbi Médio", 100, 20, 10, 30, 20)
zForte = criar_inimigo("Zumbi Forte", 150, 30, 15, 40, 30)
boss1 = criar_inimigo("Zumbi Chefe", 200, 40, 20, 50, 40)
boss2 = criar_inimigo("Zumbi Supremo", 300, 50, 25, 60, 50)
bossFinal = criar_inimigo("Tchola", 500, 60, 30, 70, 60)