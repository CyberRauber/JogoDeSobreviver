import random
import time
import inventario


LIMIAR_CURA = 40
MULTIPLICADOR_DANO_JOGADOR = 1.2
MULTIPLICADOR_DANO_INIMIGO = 0.75


OPCOES_PADRAO = [
    ("1", "Atacar"),
    ("2", "Fugir/Correr"),
    ("3", "Se fingir de Morto"),
    ("4", "Tentar se esconder")
]

OPCOES_CONFRONTO_DIRETO = [
    ("1", "Atacar"),
    ("2", "Fugir/Correr")
]

OPCOES_SEM_FINGIR_DE_MORTO = [
    ("1", "Atacar"),
    ("2", "Fugir/Correr"),
    ("4", "Tentar se esconder")
]


def calcular_dano(atacante, defensor, bonus_arma=0, multiplicador=1.0):
    forca_total = atacante["forca"] + bonus_arma
    dano = forca_total - defensor["resistencia"]
    dano = dano * multiplicador

    dano = int(dano + 0.5)

    if dano < 1:
        dano = 1

    return dano


def aplicar_ataque(atacante, defensor, bonus_arma=0, multiplicador=1.0):
    dano = calcular_dano(atacante, defensor, bonus_arma, multiplicador)
    defensor["vida"] = defensor["vida"] - dano

    if defensor["vida"] < 0:
        defensor["vida"] = 0

    return dano


def armas_disponiveis(jogador):
    armas = []

    for item in jogador["inventario"]:
        if item["categoria"] == "item" and item["tipo"] == "arma":
            armas.append(item)

    return armas


def melhor_arma(jogador):
    armas = armas_disponiveis(jogador)

    if len(armas) == 0:
        return "punhos", 3

    melhor = armas[0]

    for arma in armas:
        if arma["dano"] > melhor["dano"]:
            melhor = arma

    return melhor["nome"], melhor["dano"]


def itens_de_cura(jogador):
    curas = []

    for item in jogador["inventario"]:
        if item["categoria"] == "recurso":
            if item["restaura_vida"] > 0 and item["quantidade"] > 0:
                curas.append(item)

    return curas


def melhor_cura(jogador):
    curas = itens_de_cura(jogador)

    if len(curas) == 0:
        return None

    melhor = curas[0]

    for item in curas:
        if item["restaura_vida"] > melhor["restaura_vida"]:
            melhor = item

    return melhor


def tentar_fugir(jogador, inimigo):
    chance = 40 + jogador["velocidade"] * 3 - inimigo["velocidade"] * 2

    if chance < 5:
        chance = 5

    if chance > 95:
        chance = 95

    numero = random.randint(1, 100)

    if numero <= chance:
        return True

    return False


def iniciar_combate(jogador, inimigo, opcoes=None):
    print(f"\nUm combate contra {inimigo['nome']} começou! Vida do inimigo: {inimigo['vida']}")

    nome_arma, bonus_arma = melhor_arma(jogador)

    if nome_arma == "punhos":
        print("Você não tem nenhuma arma física em mãos — vai lutar com os próprios punhos.\n")
    else:
        print(f"Você entra no combate empunhando: {nome_arma}.\n")

    vida_maxima = jogador["vida_maxima"]
    rodada = 1

    while jogador["vida"] > 0 and inimigo["vida"] > 0:
        print(f"--- Rodada {rodada} ---")

        if jogador["vida"] < LIMIAR_CURA:
            item_cura = melhor_cura(jogador)

            if item_cura is not None:
                print(f"Sua vida está baixa ({jogador['vida']}/{vida_maxima}) — você usa {item_cura['nome']} para se curar!")
                inventario.usar_item_inventario(jogador["inventario"], item_cura["nome"], jogador)

                dano_inimigo = aplicar_ataque(inimigo, jogador, 0, MULTIPLICADOR_DANO_INIMIGO)
                print(f"O {inimigo['nome']} aproveita a brecha e causa {dano_inimigo} de dano. Sua vida restante: {jogador['vida']}")

                if jogador["vida"] <= 0:
                    print("\nVocê foi derrotado...")
                    return False

                rodada += 1
                time.sleep(0.5)
                continue

        if jogador["vida"] <= vida_maxima * 0.3:
            print(f"Sua vida está crítica ({jogador['vida']}/{vida_maxima}) e você não tem mais cura — você tenta fugir do {inimigo['nome']}!")

            if tentar_fugir(jogador, inimigo):
                print("Você conseguiu escapar a tempo!")
                return None

            print("Você tentou fugir, mas não conseguiu escapar!")
            dano_inimigo = aplicar_ataque(inimigo, jogador, 0, MULTIPLICADOR_DANO_INIMIGO)
            print(f"O {inimigo['nome']} aproveitou a brecha e causou {dano_inimigo} de dano. Sua vida restante: {jogador['vida']}")

            if jogador["vida"] <= 0:
                print("\nVocê foi derrotado...")
                return False

            rodada += 1
            time.sleep(0.5)
            continue

        dano = aplicar_ataque(jogador, inimigo, bonus_arma, MULTIPLICADOR_DANO_JOGADOR)

        if nome_arma == "punhos":
            print(f"Você golpeia o {inimigo['nome']} com os próprios punhos e causa {dano} de dano. Vida restante do inimigo: {inimigo['vida']}")
        else:
            print(f"Você ataca o {inimigo['nome']} com {nome_arma} e causa {dano} de dano. Vida restante do inimigo: {inimigo['vida']}")

        if inimigo["vida"] <= 0:
            print(f"\nVocê derrotou o {inimigo['nome']}!")
            return True

        dano_inimigo = aplicar_ataque(inimigo, jogador, 0, MULTIPLICADOR_DANO_INIMIGO)
        print(f"O {inimigo['nome']} revidou e causou {dano_inimigo} de dano. Sua vida restante: {jogador['vida']}")

        if jogador["vida"] <= 0:
            print("\nVocê foi derrotado...")
            return False

        rodada += 1
        time.sleep(0.5)

    if jogador["vida"] > 0:
        return True

    return False
