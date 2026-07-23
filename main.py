import classes
import os
import time

p = 25
vida = classes.vida
forca = classes.forca
velocidade = classes.velocidade
inteligencia = classes.inteligencia
resistencia = classes.resistencia

def limp():
    os.system('cls')

def cadastro():
    limp()
    nome = input("Cadastro do Usuário \n Digite o nome: ")
    print(f"Bem-vindo(a), {nome}! \n seus atributos iniciais são: ")
    print(mA())
    

def AddP(p, vida, forca, velocidade, inteligencia, resistencia):
      
    for i in range(p):
        print(f"\nVocê possui {p} pontos para distribuir entre os atributos do personagem.")
        print("Escolha um atributo para aumentar: ")
        print("""
        1 - Vida
        2 - Força
        3 - Velocidade
        4 - Inteligência
        5 - Resistência
        0 - Sair 
        """)
        escolha = input("Digite o número do atributo que deseja aumentar: ")
        qP = int(input("Quantos pontos deseja adicionar?\n"))
        if qP > p:
            print("Você não possui pontos suficientes. Tente novamente.")
            time.sleep(1.5)
            continue
        elif qP < 0:
            print("Você não pode adicionar pontos negativos. Tente novamente.")
            time.sleep(1.5)
            continue
        elif escolha == "1":
            p -= qP
            vida += qP
            print(f"Vida aumentada para {vida}")
        elif escolha == "2":
            p -= qP
            forca += qP
            print(f"Força aumentada para {forca}")
        elif escolha == "3":
            p -= qP
            velocidade += qP
            print(f"Velocidade aumentada para {velocidade}")
        elif escolha == "4":
            p -= qP
            inteligencia += qP
            print(f"Inteligência aumentada para {inteligencia}")
        elif escolha == "5":
            p -= qP
            resistencia += qP
            print(f"Resistência aumentada para {resistencia}")
        elif escolha == "0":
            print("...")
            break
        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(1.5)

def mA():
    return f"""
        Vida: {vida}
        Força: {forca}
        Velocidade: {velocidade}
        Inteligência: {inteligencia}
        Resistência: {resistencia}
"""

cadastro()
AddP(p, vida, forca, velocidade, inteligencia, resistencia)