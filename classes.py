import random


def criar_personagem(nome, vida=None, forca=None, velocidade=None,
                      inteligencia=None, resistencia=None, inventario=None,
                      fome=100, sede=100, vida_maxima=None):

    if vida is None:
        vida = 100

    if vida_maxima is None:
        vida_maxima = vida

    if forca is None:
        forca = random.randint(0, 10)

    if velocidade is None:
        velocidade = random.randint(0, 10)

    if inteligencia is None:
        inteligencia = random.randint(1, 10)

    if resistencia is None:
        resistencia = random.randint(0, 10)

    if inventario is None:
        inventario = []

    personagem = {
        "nome": nome,
        "vida": vida,
        "vida_maxima": vida_maxima,
        "forca": forca,
        "velocidade": velocidade,
        "inteligencia": inteligencia,
        "resistencia": resistencia,
        "inventario": inventario,
        "fome": fome,
        "sede": sede
    }

    return personagem


def criar_inimigo(nome, vida, forca, velocidade, inteligencia, resistencia):
    inimigo = {
        "nome": nome,
        "vida": vida,
        "forca": forca,
        "velocidade": velocidade,
        "inteligencia": inteligencia,
        "resistencia": resistencia
    }

    return inimigo


zFraco = criar_inimigo("Zumbi Fraco", 25, 5, 3, 10, 7)
zMedio = criar_inimigo("Zumbi Médio", 50, 10, 5, 20, 15)
zForte = criar_inimigo("Zumbi Forte", 100, 20, 15, 30, 25)
boss1 = criar_inimigo("Zumbi Chefe", 125, 30, 20, 40, 30)
boss2 = criar_inimigo("Zumbi Supremo", 150, 40, 20, 50, 35)
bossFinal = criar_inimigo("Tchola", 200, 45, 25, 60, 40)
