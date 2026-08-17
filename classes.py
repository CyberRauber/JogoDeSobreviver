import random


def criar_personagem(nome, vida=None, forca=None, velocidade=None,
                      inteligencia=None, resistencia=None, inventario=None,
                      fome=100, sede=100):
    return {
        "nome": nome,
        "vida": vida if vida is not None else 100,
        "forca": forca if forca is not None else random.randint(0, 10),
        "velocidade": velocidade if velocidade is not None else random.randint(0, 10),
        "inteligencia": inteligencia if inteligencia is not None else random.randint(1, 10),
        "resistencia": resistencia if resistencia is not None else random.randint(0, 10),
        "inventario": inventario if inventario is not None else [],
        "fome": fome,
        "sede": sede,
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