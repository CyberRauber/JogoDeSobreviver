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
    if continuar == " ":
        limpar_tela()
