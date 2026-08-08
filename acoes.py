import time
import utils
import random


def primeira_acao():
    texto = (
        "Então você ouve os barulhos e percebe a movimentação nos carros...\n"
        "O que você vai fazer?\n"
        "1 - Se fingir de morto\n"
        "2 - Sair correndo com a mochila que encontrou\n"
        "3 - Se esconder novamente e esperar os barulhos acabarem"
    )
    utils.mostrar_texto_com_delay(texto, 0.05)
    escolha = input("\nEscolha uma opção: ")

    if escolha == "1":
        fingir_morto()
    elif escolha == "2":
        correr()
    elif escolha == "3":
        esconder()
    else:
        print("Opção inválida.")

def correr():
    pass
def esconder():
    pass

def fingir_morto():
    chance = random.randint(1, 100)
    if chance >= 20:
        a = (f"""
    Você decide se fingir de morto...

    Alguns minutos passam e os barulhos aumentam...

    Você percebe que aqueles movimentos estranhos estão chegando mais próximos de você.

    Até que derrepende o que você mais temia aconteceu...

    Um ZUMBI!!!

    Quando ele passa ao seu lado, com um cheiro horrível de carniça, percebe que você está deitado no chão.

    Por um momento, ele acha que você está realmente morto.

    Mas como você está vivo, e sentindo um cheiro ruim, você tosse.

    O zumbi começa a correr na sua direção.

    Mas você não tem pra onde fugir.

    O zumbi te alcança.

    Você tenta se defender com o seu braço esquerdo...

    Mas o zumbi é mais forte, e morde seu braço.

    Ele te ataca até você perder todas as forças...

    E até que por um momento, você morre.

    Fim de jogo...""")
        utils.mostrar_texto_com_delay(a, 0.05)
        return
    else:
        b = (f"""
    Você decide se fingir de morto...

    Alguns minutos passam e os barulhos aumentam...

    Você percebe que aqueles movimentos estranhos estão chegando cada vez mais perto.

    Você permanece imóvel, tentando não fazer nenhum barulho.

    Até que, de repente, um ZUMBI passa bem ao seu lado.

    Ele olha para você por alguns segundos...

    Mas parece acreditar que você está realmente morto.

    O zumbi continua andando e desaparece entre os carros.

    Você espera mais alguns minutos, até ter certeza de que está seguro.

    Então, lentamente, você se levanta.

    Você olha ao redor e percebe que os outros zumbis também foram embora.

    Você conseguiu escapar!""")
        utils.mostrar_texto_com_delay(b, 0.05)
        return