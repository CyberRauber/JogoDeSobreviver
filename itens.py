def criar_item(nome, tipo, dano, efeito, quantidade=1):
    return {
        "nome": nome,
        "categoria": "item",
        "tipo": tipo,
        "dano": dano,
        "efeito": efeito,
        "quantidade": quantidade,
    }

def criar_recurso(nome, tipo, efeito, quantidade):
    return {
        "nome": nome,
        "categoria": "recurso",
        "tipo": tipo,
        "dano": 0,
        "efeito": efeito,
        "quantidade": quantidade,
    }