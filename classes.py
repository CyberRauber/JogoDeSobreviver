import random

forca = random.randint(10, 20)
vida = random.randint(90, 115)
velocidade = random.randint(7, 15)
inteligencia = random.randint(270, 330)
resistencia = random.randint(50, 70)

class Personagem:
    def __init__(self, nome, vida=vida, forca=forca, velocidade=velocidade, inteligencia=inteligencia, resistencia=resistencia, inventario=None):
        self.nome = nome
        self.vida = vida
        self.forca = forca
        self.velocidade = velocidade
        self.inteligencia = inteligencia
        self.resistencia = resistencia
        self.inventario = inventario

class Item:
    def __init__(self, nome, tipo, dano, efeito, quantidade=0):
        self.nome = nome
        self.tipo = tipo
        self.dano = dano
        self.quantidade = quantidade
        self.efeito = efeito

