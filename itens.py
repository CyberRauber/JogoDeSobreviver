def criar_item(nome, tipo, dano, efeito, quantidade=1):
    return {
        "nome": nome,
        "categoria": "item",
        "tipo": tipo,
        "dano": dano,
        "efeito": efeito,
        "quantidade": quantidade,
    }

def criar_recurso(nome, tipo, efeito, quantidade,
                   restaura_fome=0, restaura_sede=0, restaura_vida=0,
                   bonus_forca=0, bonus_resistencia=0,
                   bonus_velocidade=0, bonus_inteligencia=0):
    return {
        "nome": nome,
        "categoria": "recurso",
        "tipo": tipo,
        "dano": 0,
        "efeito": efeito,
        "quantidade": quantidade,
        "restaura_fome": restaura_fome,
        "restaura_sede": restaura_sede,
        "restaura_vida": restaura_vida,
        "bonus_forca": bonus_forca,
        "bonus_resistencia": bonus_resistencia,
        "bonus_velocidade": bonus_velocidade,
        "bonus_inteligencia": bonus_inteligencia,
    }