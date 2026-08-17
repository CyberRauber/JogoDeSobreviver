import random
import time


def calcular_dano(atacante, defensor, bonus_arma=0):
    forca_total = atacante.get("forca", 0) + bonus_arma
    return max(1, forca_total - defensor.get("resistencia", 0))


def aplicar_ataque(atacante, defensor, bonus_arma=0):
    dano = calcular_dano(atacante, defensor, bonus_arma)
    defensor["vida"] = max(0, defensor.get("vida", 0) - dano)
    return dano


def armas_disponiveis(jogador):
    return [
        item for item in jogador.get("inventario", [])
        if item.get("categoria") == "item" and item.get("tipo") == "arma"
    ]


def escolher_arma(jogador):
    armas = armas_disponiveis(jogador)

    if not armas:
        print("\nVocê não tem nenhuma arma física em mãos — vai precisar usar os punhos.")
        return "punhos", 3

    print("\nCom qual arma você quer atacar?")
    for i, arma in enumerate(armas, start=1):
        print(f"{i} - {arma['nome']} ({arma.get('efeito', 'sem efeito descrito')})")
    print(f"{len(armas) + 1} - Lutar com os próprios punhos")

    while True:
        escolha = input("Escolha uma opção: ")
        if escolha.isdigit():
            indice = int(escolha)
            if 1 <= indice <= len(armas):
                arma_escolhida = armas[indice - 1]
                return arma_escolhida["nome"], arma_escolhida.get("dano", 0)
            if indice == len(armas) + 1:
                return "punhos", 3
        print("Opção inválida. Tente novamente.")


OPCOES_PADRAO = [
    ("1", "Atacar"),
    ("2", "Fugir/Correr"),
    ("3", "Se fingir de Morto"),
    ("4", "Tentar se esconder"),
]


OPCOES_CONFRONTO_DIRETO = [
    ("1", "Atacar"),
    ("2", "Fugir/Correr"),
]


OPCOES_SEM_FINGIR_DE_MORTO = [
    ("1", "Atacar"),
    ("2", "Fugir/Correr"),
    ("4", "Tentar se esconder"),
]


def menu_batalha(opcoes=None):
    if opcoes is None:
        opcoes = OPCOES_PADRAO

    print("\n    MENU DE ESCOLHAS")
    for numero, texto in opcoes:
        print(f"    {numero} - {texto}")

    validos = [numero for numero, _ in opcoes]
    while True:
        r = input("Escolha uma opção: ")
        if r in validos:
            return r
        print("Opção inválida. Tente novamente.")


def iniciar_combate(jogador, inimigo, opcoes=None):
    print(f"\nVida do {inimigo['nome']}: {inimigo['vida']}\n")

    while jogador["vida"] > 0 and inimigo["vida"] > 0:
        escolha = menu_batalha(opcoes)

        if escolha == "1":
            nome_arma, bonus_arma = escolher_arma(jogador)
            dano = aplicar_ataque(jogador, inimigo, bonus_arma)
            if nome_arma == "punhos":
                print(f"Você golpeia o {inimigo['nome']} com os próprios punhos e causa {dano} de dano. "
                      f"Vida restante do inimigo: {inimigo['vida']}")
            else:
                print(f"Você ataca o {inimigo['nome']} com {nome_arma} e causa {dano} de dano. "
                      f"Vida restante do inimigo: {inimigo['vida']}")
            if inimigo["vida"] <= 0:
                print(f"\nVocê derrotou o {inimigo['nome']}!")
                return True
            dano_inimigo = aplicar_ataque(inimigo, jogador)
            print(f"O {inimigo['nome']} revidou e causou {dano_inimigo} de dano. "
                  f"Sua vida restante: {jogador['vida']}")

        elif escolha == "2":
            chance = 40 + jogador.get("velocidade", 0) * 3 - inimigo.get("velocidade", 0) * 2
            if random.randint(1, 100) <= max(5, min(chance, 95)):
                print("Você conseguiu fugir!")
                return None
            print("Você tentou fugir, mas não conseguiu escapar!")
            dano_inimigo = aplicar_ataque(inimigo, jogador)
            print(f"O {inimigo['nome']} te atacou e causou {dano_inimigo} de dano. "
                  f"Sua vida restante: {jogador['vida']}")

        elif escolha == "3":
            chance = 30 + jogador.get("inteligencia", 0) * 3
            if random.randint(1, 100) <= max(5, min(chance, 90)):
                print(f"O {inimigo['nome']} perde o interesse e se afasta.")
                return None
            print("O truque não funcionou!")
            dano_inimigo = aplicar_ataque(inimigo, jogador)
            print(f"O {inimigo['nome']} te atacou e causou {dano_inimigo} de dano. "
                  f"Sua vida restante: {jogador['vida']}")

        elif escolha == "4":
            chance = 35 + jogador.get("inteligencia", 0) * 2 + jogador.get("velocidade", 0) * 2
            if random.randint(1, 100) <= max(5, min(chance, 90)):
                print("Você se escondeu com sucesso e o perigo passou.")
                return None
            print("Você foi encontrado!")
            dano_inimigo = aplicar_ataque(inimigo, jogador)
            print(f"O {inimigo['nome']} te atacou e causou {dano_inimigo} de dano. "
                  f"Sua vida restante: {jogador['vida']}")

        if jogador["vida"] <= 0:
            print("\nVocê foi derrotado...")
            return False

        time.sleep(0.4)

    return jogador["vida"] > 0