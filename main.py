import classes
import os
import time

p = 25 # Pontos
vida = classes.vida
forca = classes.forca
velocidade = classes.velocidade
inteligencia = classes.inteligencia
resistencia = classes.resistencia
fome = 100
sede = 100
xp = 0
nivel = 0

pedra = classes.criar_item("pedra", "recurso", 0, "construção", 0)
madeira = classes.criar_item("madeira", "recurso", 0, "construção", 0)
pao = classes.criar_recurso("pão", "comida", "restaura 10 de fome", 10)
aguaNormal = classes.criar_recurso("água", "bebida", "restaura 10 de sede", 10)



def attNiveis(p, xp, nivel): # Atualiza o nivel do personagem
    if xp >= 100:
        nivel += 1
        xp -= 100
        p+=5
        print(f"Parabéns! Você subiu para o nível {nivel}!")
    return xp, nivel

pao = classes.criar_recurso("pão", "comida", "restaura 10 de fome", 10)
aguaNormal = classes.criar_recurso("água", "bebida", "restaura 10 de sede", 10)

def limp():
    os.system('cls')

def mA(): # Mostra Atributos
    return f"""
        Vida: {vida}  Fome: {fome}  Sede: {sede}  
        Força: {forca}
        Velocidade: {velocidade}
        Inteligência: {inteligencia}
        Resistência: {resistencia}
        XP: {xp} ()  Nível: {nivel}
"""

def cadastro(): #Cadastro
    limp()
    nome = input("Cadastro do Usuário \n Digite o nome: ")
    print(f"\nBem-vindo(a), {nome}! \n seus atributos iniciais são: ")
    print(mA())
    

def AddP(p, vida, forca, velocidade, inteligencia, resistencia): #Adiciona pontos aos atributos do personagem
    if p <= 0:
        print("Você não possui pontos para distribuir.")
        return
    while p > 0:
        print(f"\nVocê possui {p} pontos para distribuir entre os atributos do personagem.")
        print("Escolha um atributo para aumentar: ")
        print("""
        1 - Vida
        2 - Força
        3 - Velocidade
        4 - Inteligência
        5 - Resistência
        6 - Mostrar Atributos
        0 - Sair 
        """)
        escolha = input("Digite o número do atributo que deseja aumentar: ")

        if escolha not in ["1", "2", "3", "4", "5", "6", "0"]:
            print("Opção inválida. Tente novamente.")
            time.sleep(1)
            continue
        elif escolha == "6":
                    print(mA())
                    continue
        qP = int(input("Quantos pontos deseja adicionar?\n")) #Quantidade de pontos a adicionar

        if qP > p:
            print("Você não possui pontos suficientes. Tente novamente.")
            time.sleep(1)
            continue
        elif qP < 0:
            print("Você não pode adicionar pontos negativos. Tente novamente.")
            time.sleep(1)
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
            time.sleep(1)
    return

def menu():
    print("""
    MENU PRINCIPAL
    1 - Começar o jogo
    2 - Mostrar Atributos
    0 - Sair
""")


    
def main(): # Onde o jogo começa
    limp()
    print("Iniciando jogo!")
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(0.7)
    

cadastro()
AddP(p, vida, forca, velocidade, inteligencia, resistencia)
main()