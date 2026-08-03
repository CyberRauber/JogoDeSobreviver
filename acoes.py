import time
import utils


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
    utils.mostrar_texto_com_delay(a, 0.01)
    return
