import fases
import inventario


LISTA_DE_FASES = [
    fases.fase1, fases.fase2, fases.fase3, fases.fase4, fases.fase5,
    fases.fase6, fases.fase7, fases.fase8, fases.fase9, fases.fase10,
    fases.fase11, fases.fase12, fases.fase13, fases.fase14, fases.fase15,
    fases.fase16, fases.fase17, fases.fase18, fases.fase19, fases.fase20
]


def oferecer_uso_de_item(jogador):
    resposta = input("\nDeseja usar algum item do inventário antes de continuar? (s/n): ").lower()

    if resposta == "s":
        inventario.menu_inventario(jogador)


def acoes(jogador):
    numero_fase = 1

    for fase in LISTA_DE_FASES:
        fase(jogador)

        if fases.jogador_vivo(jogador) == False:
            return

        if numero_fase < len(LISTA_DE_FASES):
            oferecer_uso_de_item(jogador)

        numero_fase += 1
