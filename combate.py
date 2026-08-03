def calcular_dano(atacante, defensor):
    return max(1, atacante.get("forca", 0) - defensor.get("resistencia", 0))


def aplicar_ataque(atacante, defensor):
    dano = calcular_dano(atacante, defensor)
    defensor["vida"] = max(0, defensor.get("vida", 0) - dano)
    return dano
