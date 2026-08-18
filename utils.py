import os
import time


def limpar_tela():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def esperar(segundos=0.01):
    time.sleep(segundos)


def mostrar_texto_com_delay(texto, atraso=0.01):
    for letra in texto:
        print(letra, end="", flush=True)
        esperar(atraso)


def enter():
    input("\nPressione Enter para continuar...")
    limpar_tela()


def mostrar_atributos(jogador):
    texto = f"""
        Vida: {jogador['vida']}/{jogador['vida_maxima']}  Fome: {jogador['fome']}  Sede: {jogador['sede']}
        Força: {jogador['forca']}
        Velocidade: {jogador['velocidade']}
        Inteligência: {jogador['inteligencia']}
        Resistência: {jogador['resistencia']}
"""
    return texto


def pedir_escolha(opcoes_validas=None, jogador=None, prompt="\nEscolha uma opção: "):
    while True:
        escolha = input(prompt).strip().lower()

        if escolha == "a":
            if jogador is not None:
                print(mostrar_atributos(jogador))
            else:
                print("Atributos não disponíveis aqui.")

        elif escolha == "i":
            if jogador is not None:
                import inventario
                inventario.menu_inventario(jogador)
            else:
                print("Inventário não disponível aqui.")

        else:
            if opcoes_validas is None:
                return escolha

            if escolha in opcoes_validas:
                return escolha

            print("Opção inválida. Tente novamente.")
