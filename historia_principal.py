import time
import main
import os

def limp():
    os.system('clear' if os.name != 'nt' else 'cls')

def primeira_acao():
    contexto = """Então você ouve os barulhos e percebe a movimentação nos carros...
    O que você vai fazer?
    1 - Se fingir de morto
    2 - Sair correndo com a mochila que encontrou
    3 - Se esconder novamente e esperar os barulhos acabarem
    """
    for letra in contexto:
        print(letra, end="", flush=True)
        time.sleep(0.01)
    entrar = input("\n\nPressione Enter para continuar...")
    if entrar == "":
        limp()

    if contexto == "1":
        correr()

    elif contexto == "2":
        fingir_morto()

    elif contexto == "3":
        esconder()

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
    for letra in a:
            print(letra, end="", flush=True)
            time.sleep(0.01)
    return
