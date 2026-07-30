import classes
import os
import time
import cores

def mostrar_historia(nome):
    pular_historia = input("Deseja pular a história? (s/n): ").lower()
    if pular_historia.lower() == "s":
        print("História pulada.")
        return
    historia = (f""" O Último Sobrevivente

Tudo começou com uma {cores.amareloT("doença")}.

No início, parecia apenas mais um {cores.verdeT("Vírus")}. Os primeiros casos surgiram em pequenas cidades, causando febre intensa, confusão mental e um comportamento agressivo. Em poucos dias, hospitais ficaram lotados. Em poucas semanas, países inteiros entraram em quarentena.

Os governos afirmavam que tudo estava sob controle.

Não estava.

O {cores.verdeT("Vírus")} sofria mutações em uma velocidade impossível. Pessoas aparentemente saudáveis podiam carregar a infecção por dias sem apresentar sintomas. Quando eles finalmente apareciam, já era tarde demais.

A mente desaparecia.

Restava apenas um corpo movido por instintos violentos.

As grandes cidades foram as primeiras a cair. A energia elétrica falhou, redes de comunicação deixaramde funcionar e o abastecimento de água e alimentos entrou em colapso. Milhões morreram. Outros milhões foram infectados.

Quem sobreviveu precisou abandonar tudo.

Famílias foram separadas. Amigos desapareceram. Cidades inteiras tornaram-se cemitérios silenciosos.

Meses depois, a natureza começou a recuperar o que era seu. Árvores cresceram entre o asfalto, prédios foram cobertos por plantas e o silêncio tomou conta das ruas.

Mas o silêncio era enganoso.

Em qualquer esquina, dentro de qualquer casa ou escondido em qualquer floresta, algo podia estar esperando.

Você não sabe quanto tempo se passou.

Também não lembra como chegou até ali.

Sua última lembrança é confusa: pessoas correndo, tiros ao longe, sirenes, alguém gritando...

"{cores.vermelhoT(nome)}!"

Depois disso...

Escuridão.

Seus olhos se abrem lentamente.

Sua cabeça dói.

Você tenta lembrar de alguma coisa, mas tudo parece distante, como um sonho esquecido.

Uma voz ecoa em sua mente.

"Meu nome é... {cores.vermelhoT(nome)}."

É a única certeza que você tem.

Você se levanta com dificuldade.

O abrigo onde acordou está abandonado. Há poeira sobre os móveis, alimentos vencidos e marcas de sangue espalhadas pelo chão. A porta principal está entreaberta, balançando lentamente com o vento.

Lá fora, o mundo parece morto.

Nenhuma voz.

Nenhum carro.

Nenhuma fumaça no horizonte.

Apenas o som do vento atravessando prédios vazios e o ranger distante de estruturas prestes a desabar.

Você respira fundo.

— Ainda estou vivo...

Mas por quanto tempo?

Você caminha alguns passos para fora do abrigo.

A rua está coberta por carros enferrujados, placas caídas e vegetação tomando conta do asfalto.

Uma mochila velha está jogada próxima à entrada.

Dentro dela há apenas uma garrafa de água quase vazia, uma lanterna fraca e um pequeno caderno.

Na primeira página está escrito à mão:

"Se você encontrou isto, significa que ainda há esperança. Continue vivendo, {cores.vermelhoT(nome)}. Não importa o que aconteça... não pare."

Você vira rapidamente as outras páginas.

Todas estão em branco.

Um arrepio percorre seu corpo.

Quem escreveu aquilo?

Como essa pessoa sabia seu nome?

Antes que consiga pensar em uma resposta...

Um grunhido quebra o silêncio.

Depois outro.

E outro.

Algo está se movendo entre os carros abandonados.

Você prende a respiração.

O mundo não acabou.

Ele apenas pertence a outra coisa agora.

Você não é um soldado.

Não é um cientista.

Não conhece uma cura.

Você é apenas {cores.vermelhoT(nome)}.

E, neste mundo, isso terá que ser suficiente.

Seu único objetivo é sobreviver.

Mais um dia.

Depois mais um.

Até que não reste mais ninguém...

Ou até que você descubra a verdade por trás do {cores.verdeT("Vírus")}.
""")
    
    for letra in historia:
        print(letra, end="", flush=True)
        time.sleep(0.01)
    entrar = input("\n\nPressione Enter para continuar...")
    if entrar == "":
        limp()

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
    while True:
        nome = input("Cadastro do Usuário \n Digite o nome: ").strip()
        if nome == "" or nome in "                                    ":
            print("Nome inválido. Tente novamente.")
            time.sleep(1)
            limp()
            continue
        elif len(nome) < 3:
            print("O nome deve ter pelo menos 3 caracteres. Tente novamente.")
            time.sleep(1)
            limp()
            continue
        elif len(nome) > 20:
            print("O nome deve ter no máximo 20 caracteres. Tente novamente.")
            time.sleep(1)
            limp()
            continue
        else:
            break
    limp()
    mostrar_historia(nome)
    print(f"\nBem-vindo(a), {cores.vermelhoT(nome)}! \n seus atributos iniciais são: ")
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