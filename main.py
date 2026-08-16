import classes
import time
import cores
import acoes
import inventario
import itens
import utils

def mostrar_historia(nome):
    pular_historia = input("Deseja pular a história? (s/n): ").lower()
    if pular_historia == "s":
        print("História pulada.")
        return
    historia = (f""" O ÚLTIMO SOBREVIVENTE

Tudo começou com uma {cores.amareloT("doença")}.

    No início, parecia apenas mais um {cores.verdeT("Vírus")}. O chamado {cores.verdeT("Vírus Nossila")} Os primeiros casos surgiram em pequenas cidades, causando febre intensa, confusão mental e um comportamento agressivo. Em poucos dias, hospitais ficaram lotados. Em poucas semanas, países inteiros entraram em quarentena.

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
    
    utils.mostrar_texto_com_delay(historia, 0.01)
    entrar = input("\n\nPressione Enter para continuar...")
    if entrar == "":
        limp()

vida = classes.vida
forca = classes.forca
velocidade = classes.velocidade
inteligencia = classes.inteligencia
resistencia = classes.resistencia
fome = 100
sede = 100

zFraco = classes.zFraco
zMedio = classes.zMedio
zForte = classes.zForte
boss1 = classes.boss1
boss2 = classes.boss2
bossFinal = classes.bossFinal

pedra = itens.criar_item("pedra", "recurso", 0, "construção", 0)
madeira = itens.criar_item("madeira", "recurso", 0, "construção", 0)
pao = itens.criar_recurso("pão", "comida", "restaura 10 de fome", 10)
aguaNormal = itens.criar_recurso("água", "bebida", "restaura 10 de sede", 10)
feijao = itens.criar_recurso("feijão", "comida", "restaura 20 de fome", 20)
def limp():
    utils.limpar_tela()

def mA(): # Mostra Atributos
    return f"""
        Vida: {vida}  Fome: {fome}  Sede: {sede}  
        Força: {forca}
        Velocidade: {velocidade}
        Inteligência: {inteligencia}
        Resistência: {resistencia}
"""

def nome_usuario():
    while True:
        nome = input("Cadastro do Usuário \nDigite seu nome de jogador: ").strip()
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
    return nome

def cadastro(): #Cadastro
    nome_jogador = nome_usuario()
    limp()
    mostrar_historia(nome_jogador)
    print(f"\nBem-vindo(a), {cores.vermelhoT(nome_jogador)}! \n seus atributos iniciais são: ")
    print(mA())
    return nome_jogador

def menu(nome):
    print("""
    MENU PRINCIPAL
    1 - Continuar o jogo
    2 - Mostrar Atributos
    3 - Mostrar história
    4 - Craftar Item
    0 - Sair
""")
    r = input("Escolha uma opção: ")
    if r == "1":
        main()
    elif r == "3":
        mostrar_historia(nome)

def menuEscolha():
    print("""






""")

def menuEscolhaBatalha():
    print("""
    MENU DE ESCOLHAS
    1 - Atacar
    2 - Fugir/Correr
    3 - Se fingir de Morto
    4 - Tentar se esconder
""")
    r = input("Escolha uma opção: ")
    if r == "1":
        pass
    elif r == "2":
        pass
    elif r == "3":
        pass
    elif r == "4":
        pass
    elif r == "0":
        menu()
def main(): # Onde o jogo começa
    limp()
    print("Iniciando jogo!")
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(0.7)
    acoes.acoes()
    

nome = cadastro()
main()