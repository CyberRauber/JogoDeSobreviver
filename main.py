import classes
import random

rHuman = classes.Raca("Humano", 10, 100, 15, 10, 10) #nome, força, vida, velocidade, inteligência, resistência

rAlien = classes.Raca("Alien", 15, 150, 15, 15, 15)

rHibrido = classes.Raca("Híbrido", 20, 200, 20, 20, 20)

rZumbi = classes.Raca("Zumbi", 25, 250, 10, 25, 25)


def cad(): #Cadastro de usuário 
    nome = input("Insira o nome do usuário: ")
    r = input("""Escolha a raça do usuário: 
    [1] Humano
    [2] Alien
    [3] Híbrido
    [4] Zumbi
    """"")
