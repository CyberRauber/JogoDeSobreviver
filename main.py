import classes
import random

rHuman = classes.Raca("Humano", 10, 100, 15, 10, 10, 0) #nome, força, vida, velocidade, inteligência, resistência

rAlien = classes.Raca("Alien", 15, 150, 15, 15, 15)

rHibrido = classes.Raca("Híbrido", 20, 200, 20, 20, 20)

rZumbi = classes.Raca("Zumbi", 25, 250, 10, 25, 25)

rMago = classes.Raca("Mago", 5, 50, 10, 30, 5, 50) #nome, força, vida, velocidade, inteligência, resistência, magia

def cad(): #Cadastro de usuário 
    nome = input("Insira o nome do usuário: ")
    rOpc = input("""Escolha a raça do usuário: 
    [1] Humano
    [2] Alien
    [3] Híbrido
    [4] Zumbi
    [5] Mago
    """"")
    match rOpc:
        case "1":
            raca = rHuman
            print(f"{nome} \n Força: {raca.forca}\n Vida: {raca.vida} \n Velocidade: {raca.velocidade} \n Inteligência: {raca.inteligencia} \n Resistência: {raca.resistencia}")
        case "2":
            raca = rAlien
            print(f"{nome} \n Força: {raca.forca}\n Vida: {raca.vida} \n Velocidade: {raca.velocidade} \n Inteligência: {raca.inteligencia} \n Resistência: {raca.resistencia}")
        case "3":
            raca = rHibrido
            print(f"{nome} \n Força: {raca.forca}\n Vida: {raca.vida} \n Velocidade: {raca.velocidade} \n Inteligência: {raca.inteligencia} \n Resistência: {raca.resistencia}")
        case "4":
            raca = rZumbi
            print(f"{nome} \n Força: {raca.forca}\n Vida: {raca.vida} \n Velocidade: {raca.velocidade} \n Inteligência: {raca.inteligencia} \n Resistência: {raca.resistencia}")
        case "5":
            raca = rMago
            print(f"{nome} \n Força: {raca.forca}\n Vida: {raca.vida} \n Velocidade: {raca.velocidade} \n Inteligência: {raca.inteligencia} \n Resistência: {raca.resistencia}")    
cad()