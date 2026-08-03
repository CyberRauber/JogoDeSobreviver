def criar_item(nome, tipo, dano, efeito, velocidade, quantidade=1):
    return {
        "nome": nome,
        "tipo": tipo,
        "dano": dano,
        "efeito": efeito,
        "velocidade": velocidade,
        "quantidade": quantidade,
    }


def criar_recurso(nome, tipo, efeito, valorEf):
    return {
        "nome": nome,
        "tipo": tipo,
        "efeito": efeito,
        "valorEf": valorEf,
        "quantidade": 1,
    }


def itens_aleatorios():
    return None
