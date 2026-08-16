import time
import utils
import random
import cores
import inventario

def acoes():
    fase1()

def fase1():
    print("FASE 1 — A CASA ABANDONADA")
    texto = (f"""
Depois de horas caminhando sem rumo, você encontra uma pequena casa aparentemente abandonada na beira de uma estrada.

A porta está entreaberta e há marcas de sangue seco na entrada. Mesmo assim, ficar do lado de fora durante a noite parece ainda mais perigoso.

Ao entrar na casa, você encontra uma lata de feijão, uma garrafa de água, bandagens, e alguns objetos como garfos, facas, estacas que podem ser usados como arma.

Você acha que é uma boa ideia ter esse tipo de recurso, então você decide pegar alguns itens para sua mochila.

Qual arma você vai guardar para caso um {cores.verdeT("zumbi")} apareça?

1 - Garfos (dano baixo)
2 - Facas (dano médio)
3 - Estacas (dano alto)
""")

    utils.mostrar_texto_com_delay(texto, 0.05)
    inventario.adicionar_item_inventario("lata de feijão", 1)
    inventario.adicionar_item_inventario("garrafa de água", 1)
    inventario.adicionar_item_inventario("bandagem", 1)
    while True:
        escolha = input("\nEscolha uma opção: ")

        if escolha == "1":
            inventario.adicionar_item_inventario("garfo", 1)
        elif escolha == "2":
            inventario.adicionar_item_inventario("faca", 1)
        elif escolha == "3":
            inventario.adicionar_item_inventario("estaca", 1)
        else:
            print("Opção inválida. Tente novamente.")
            continue
        break
    texto2 = (f"""
Enquanto procura recursos, um barulho de grunhido junto com passos lentos e batidas em portas vem do andar de cima.

Uma pessoa infectada está presa em um dos quartos.

O que você vai fazer?

1 - Usar sua arma para lutar contra o {cores.verdeT("zumbi")} e tentar matá-lo.")
2 - Sair de fininho da casa e sair em busca de outro lugar para se abrigar.
""")
    utils.mostrar_texto_com_delay(texto2, 0.05)
    while True:
        escolha2 = input("\nEscolha uma opção: ")

        if escolha2 == "1":
            print("""Você decide enfrentar o zumbi...

            Você se prepara para o combate, segurando firmemente sua arma escolhida.
            
            Lentamente, você sobe as escadas, cada passo ecoando pela casa silenciosa.
            
            Então, você encontra a porta do quarto trancada. O grunhido fica mais alto e você percebe que o zumbi está tentando sair.
            
            Você, já armado com sua arma, se prepara para o confronto. O zumbi finalmente consegue abrir a porta e avança em sua direção.
            
            """)
            # Aqui você pode adicionar a lógica de combate
            break
        elif escolha2 == "2":
            print("Você decide sair da casa e procurar outro lugar para se abrigar.")
            # Aqui você pode adicionar a lógica de fuga
            break
        else:
            print("Opção inválida. Tente novamente.")
            continue
    
