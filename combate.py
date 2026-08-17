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


def melhor_arma(jogador):
    """Seleciona automaticamente a arma de maior dano no inventário do jogador."""
    armas = armas_disponiveis(jogador)

    if not armas:
        return "punhos", 3

    arma_escolhida = max(armas, key=lambda arma: arma.get("dano", 0))
    return arma_escolhida["nome"], arma_escolhida.get("dano", 0)


LIMIAR_FUGA = 0.3 


def tentar_fugir(jogador, inimigo):
    chance = 40 + jogador.get("velocidade", 0) * 3 - inimigo.get("velocidade", 0) * 2
    return random.randint(1, 100) <= max(5, min(chance, 95))

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


def iniciar_combate(jogador, inimigo, opcoes=None):
    """Combate totalmente automático: o jogador ataca sozinho, rodada a rodada,
    com a melhor arma disponível, até que ele ou o inimigo seja derrotado.
    Se a vida do jogador cair abaixo de LIMIAR_FUGA, ele tenta fugir
    automaticamente em vez de continuar atacando."""
    print(f"\nUm combate contra {inimigo['nome']} começou! Vida do inimigo: {inimigo['vida']}")

    nome_arma, bonus_arma = melhor_arma(jogador)
    if nome_arma == "punhos":
        print("Você não tem nenhuma arma física em mãos — vai lutar com os próprios punhos.\n")
    else:
        print(f"Você entra no combate empunhando: {nome_arma}.\n")

    vida_maxima = jogador.get("vida_maxima", 100)

    rodada = 1
    while jogador["vida"] > 0 and inimigo["vida"] > 0:
        print(f"--- Rodada {rodada} ---")

        if jogador["vida"] <= vida_maxima * LIMIAR_FUGA:
            print(f"Sua vida está baixa ({jogador['vida']}/{vida_maxima}) — você tenta fugir do {inimigo['nome']}!")
            if tentar_fugir(jogador, inimigo):
                print("Você conseguiu escapar a tempo!")
                return None

            print("Você tentou fugir, mas não conseguiu escapar!")
            dano_inimigo = aplicar_ataque(inimigo, jogador)
            print(f"O {inimigo['nome']} aproveitou a brecha e causou {dano_inimigo} de dano. "
                  f"Sua vida restante: {jogador['vida']}")

            if jogador["vida"] <= 0:
                print("\nVocê foi derrotado...")
                return False

            rodada += 1
            time.sleep(0.5)
            continue

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

        if jogador["vida"] <= 0:
            print("\nVocê foi derrotado...")
            return False

        rodada += 1
        time.sleep(0.5)

    return jogador["vida"] > 0