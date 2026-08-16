def criar_item(nome, tipo, dano, efeito, quantidade=1):
    return {
        "nome": nome,
        "tipo": tipo,
        "dano": dano,
        "efeito": efeito,
        "quantidade": quantidade,
    }


def criar_recurso(nome, tipo, efeito, quantidade):
    return {
        "nome": nome,
        "tipo": tipo,
        "efeito": efeito,
        "quantidade": quantidade,
    }
