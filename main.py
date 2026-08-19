import classes
import time
import cores
import acoes
import inventario
import itens
import utils


def mostrar_historia(nome):
    pular_historia = input("Deseja pular a história? (s/n): ").lower()
    if pular_historia == "s":
        print("História pulada.")
        return
    historia = (f""" O ÚLTIMO SOBREVIVENTE

Tudo começou com uma {cores.amareloT("doença")}.

    No início, parecia apenas mais um {cores.verdeT("Vírus")}. O chamado {cores.verdeT("Vírus Suehtam-19")} Os primeiros casos surgiram em pequenas cidades, causando febre intensa, confusão mental e um comportamento agressivo. Em poucos dias, hospitais ficaram lotados. Em poucas semanas, países inteiros entraram em quarentena.

Os governos afirmavam que tudo estava sob controle.

Não estava.

O {cores.verdeT("Vírus")} sofria mutações em uma velocidade impossível. Pessoas aparentemente saudáveis podiam carregar a infecção por dias sem apresentar sintomas. Quando eles finalmente apareciam, já era tarde demais.

A mente desaparecia.

Restava apenas um corpo movido por instintos violentos.

As grandes cidades foram as primeiras a cair. A energia elétrica falhou, redes de comunicação deixaramde funcionar e o abastecimento de água e alimentos entrou em colapso. Milhões morreram. Outros milhões foram infectados.

Quem sobreviveu precisou abandonar tudo.

Famílias foram separadas. Amigos desapareceram. Cidades inteiras tornaram-se cemitérios silenciosos.

Meses depois, a natureza começou a recuperar o que era seu. Árvores cresceram entre o asfalto, prédios foram cobertos por plantas e o silêncio tomou conta das ruas.

Mas o silêncio era enganoso.

Em qualquer esquina, dentro de qualquer casa ou escondido em qualquer floresta, algo podia estar esperando.

Você não sabe quanto tempo se passou.

Também não lembra como chegou até ali.

Sua última lembrança é confusa: pessoas correndo, tiros ao longe, sirenes, alguém gritando...

"{cores.vermelhoT(nome)}!"

Depois disso...

Escuridão.

Seus olhos se abrem lentamente.

Sua cabeça dói.

Você tenta lembrar de alguma coisa, mas tudo parece distante, como um sonho esquecido.

Uma voz ecoa em sua mente.

"Meu nome é... {cores.vermelhoT(nome)}."

É a única certeza que você tem.

Você se levanta com dificuldade.

O abrigo onde acordou está abandonado. Há poeira sobre os móveis, alimentos vencidos e marcas de sangue espalhadas pelo chão. A porta principal está entreaberta, balançando lentamente com o vento.

Lá fora, o mundo parece morto.

Nenhuma voz.

Nenhum carro.

Nenhuma fumaça no horizonte.

Apenas o som do vento atravessando prédios vazios e o ranger distante de estruturas prestes a desabar.

Você respira fundo.

— Ainda estou vivo...

Mas por quanto tempo?

Você caminha alguns passos para fora do abrigo.

A rua está coberta por carros enferrujados, placas caídas e vegetação tomando conta do asfalto.

Uma mochila velha está jogada próxima à entrada.

Dentro dela há apenas uma garrafa de água quase vazia, uma lanterna fraca e um pequeno caderno.

Na primeira página está escrito à mão:

"Se você encontrou isto, significa que ainda há esperança. Continue vivendo, {cores.vermelhoT(nome)}. Não importa o que aconteça... não pare."

Você vira rapidamente as outras páginas.

Todas estão em branco.

Um arrepio percorre seu corpo.

Quem escreveu aquilo?

Como essa pessoa sabia seu nome?

Antes que consiga pensar em uma resposta...

Um grunhido quebra o silêncio.

Depois outro.

E outro.

Algo está se movendo entre os carros abandonados.

Você prende a respiração.

O mundo não acabou.

Ele apenas pertence a outra coisa agora.

Você não é um soldado.

Não é um cientista.

Não conhece uma cura.

Você é apenas {cores.vermelhoT(nome)}.

E, neste mundo, isso terá que ser suficiente.

Seu único objetivo é sobreviver.

Mais um dia.

Depois mais um.

Até que não reste mais ninguém...

Ou até que você descubra a verdade por trás do {cores.verdeT("Vírus")}.
""")

    utils.mostrar_texto_com_delay(historia, 0.01)
    utils.enter()


def limp():
    utils.limpar_tela()


def nome_usuario():
    while True:
        nome = input("Cadastro do Usuário \nDigite seu nome de jogador: ").strip()
        if nome == "":
            print("Nome inválido. Tente novamente.")
            time.sleep(1)
            limp()
            continue
        elif len(nome) < 3:
            print("O nome deve ter pelo menos 3 caracteres. Tente novamente.")
            time.sleep(1)
            limp()
            continue
        elif len(nome) > 20:
            print("O nome deve ter no máximo 20 caracteres. Tente novamente.")
            time.sleep(1)
            limp()
            continue
        else:
            break
    return nome


def cadastro():
    nome_jogador = nome_usuario()
    limp()
    mostrar_historia(nome_jogador)
    jogador = classes.criar_personagem(nome_jogador, inventario=[])
    itens_iniciais = [
        itens.criar_recurso("pedra", "construção", "usado para criar itens", 1),
        itens.criar_recurso("madeira", "construção", "usado para criar itens", 1),
        itens.criar_recurso("pão", "comida", "restaura 10 de vida", 1, restaura_vida=10),
        itens.criar_recurso("água", "bebida", "restaura 10 de vida'", 1, restaura_vida=10),
        itens.criar_recurso("feijão", "comida", "restaura 20 de vida", 1, restaura_vida=20),
    ]
    for item in itens_iniciais:
        inventario.adicionar_item_inventario(jogador["inventario"], item, mostrar=False)

    print(f"\nBem-vindo(a), {cores.vermelhoT(nome_jogador)}! \n seus atributos iniciais são: ")
    print(utils.mostrar_atributos(jogador))
    print(f"{cores.amareloT('Itens iniciais:')}")
    inventario.mostrar_inventario(jogador["inventario"])
    print(
        f"\n{cores.amareloT('Dica:')} a qualquer momento em que o jogo pedir uma escolha, "
        "digite 'A' para ver seus atributos ou 'I' para ver/usar seu inventário."
    )
    utils.enter()
    return jogador


def menu(jogador):
    while True:
        print("""
    MENU PRINCIPAL
    1 - Continuar o jogo
    2 - Mostrar Atributos
    3 - Mostrar história
    4 - Mostrar Inventário
    0 - Sair
""")
        r = input("Escolha uma opção: ")
        if r == "1":
            iniciar_jogo(jogador)
            if jogador["vida"] <= 0:
                print(f"\n{cores.vermelhoT('FIM DE JOGO')} — sua jornada chega ao fim aqui.")
                break
        elif r == "2":
            print(utils.mostrar_atributos(jogador))
            utils.enter()
        elif r == "3":
            mostrar_historia(jogador["nome"])
        elif r == "4":
            inventario.menu_inventario(jogador)
            utils.enter()
        elif r == "0":
            print("Saindo do jogo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


def iniciar_jogo(jogador):
    limp()
    print("Iniciando jogo!")
    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(0.7)
    print()
    acoes.acoes(jogador)


if __name__ == "__main__":
    jogador_atual = cadastro()
    menu(jogador_atual)