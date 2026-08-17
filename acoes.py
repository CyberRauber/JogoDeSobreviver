import fases


LISTA_DE_FASES = [
    fases.fase1,
    fases.fase2,
    fases.fase3,
    fases.fase4,
    fases.fase5,
    fases.fase6,
    fases.fase7,
    fases.fase8,
    fases.fase9,
    fases.fase10,
    fases.fase11,
    fases.fase12,
    fases.fase13,
    fases.fase14,
    fases.fase15,
    fases.fase16,
    fases.fase17,
    fases.fase18,
    fases.fase19,
    fases.fase20,
]


def acoes(jogador):
    for fase in LISTA_DE_FASES:
        fase(jogador)
        if not fases.jogador_vivo(jogador):
            return