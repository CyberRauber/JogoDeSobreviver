import os
import time


def limpar_tela():
    os.system("clear" if os.name != "nt" else "cls")


def esperar(segundos=0.01):
    time.sleep(segundos)


def mostrar_texto_com_delay(texto, atraso=0.01):
    for letra in texto:
        print(letra, end="", flush=True)
        esperar(atraso)


def enter():
    continuar = input("\nPressione Enter para continuar...")
    if continuar == "":
        limpar_tela()


def mostrar_atributos(jogador):
    vida_maxima = jogador.get("vida_maxima", 100)
    return f"""
        Vida: {jogador['vida']}/{vida_maxima}  Fome: {jogador['fome']}  Sede: {jogador['sede']}
        Força: {jogador['forca']}
        Velocidade: {jogador['velocidade']}
        Inteligência: {jogador['inteligencia']}
        Resistência: {jogador['resistencia']}
"""


def pedir_escolha(opcoes_validas=None, jogador=None, prompt="\nEscolha uma opção: "):
    while True:
        escolha = input(prompt).strip().lower()

        if escolha == "a":
            if jogador is not None:
                print(mostrar_atributos(jogador))
            else:
                print("Atributos não disponíveis aqui.")
            continue

        if escolha == "i":
            if jogador is not None:
                import inventario
                inventario.menu_inventario(jogador)
            else:
                print("Inventário não disponível aqui.")
            continue

        if opcoes_validas is None or escolha in opcoes_validas:
            return escolha

        print("Opção inválida. Tente novamente.")