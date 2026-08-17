import utils
import cores
import inventario
import itens
import combate
import classes


def jogador_vivo(jogador):
    return jogador.get("vida", 0) > 0


def fase1(jogador):
    print("FASE 1 — A CASA ABANDONADA")
    texto = (f"""
Depois de horas caminhando sem rumo, você encontra uma pequena casa aparentemente abandonada na beira de uma estrada.

A porta está entreaberta e há marcas de sangue seco na entrada. Mesmo assim, ficar do lado de fora durante a noite parece ainda mais perigoso.

Ao entrar na casa, você encontra uma lata de feijão, uma garrafa de água, bandagens, e alguns objetos como garfos, facas, estacas que podem ser usados como arma.

Você acha que é uma boa ideia ter esse tipo de recurso, então você decide pegar alguns itens para sua mochila.

Qual arma você vai guardar para caso um {cores.verdeT("zumbi")} apareça?

1 - Garfos (dano baixo)
2 - Facas (dano médio)
3 - Estacas (dano alto)
""")
    utils.mostrar_texto_com_delay(texto, 0.05)
    inventario.adicionar_item_inventario(
        jogador["inventario"],
        itens.criar_recurso("lata de feijão", "comida", "restaura 20 de fome", 1, restaura_fome=20),
        mostrar=False,
    )
    inventario.adicionar_item_inventario(
        jogador["inventario"],
        itens.criar_recurso("garrafa de água", "bebida", "restaura 10 de sede", 1, restaura_sede=10),
        mostrar=False,
    )
    inventario.adicionar_item_inventario(
        jogador["inventario"],
        itens.criar_recurso("bandagem", "cura", "restaura vida", 1, restaura_vida=15),
        mostrar=False,
    )
    inventario.mostrar_inventario(jogador["inventario"])

    while True:
        escolha = utils.pedir_escolha(jogador=jogador)

        if escolha == "1":
            arma = itens.criar_item("garfo", "arma", 5, "dano baixo", 1)
        elif escolha == "2":
            arma = itens.criar_item("faca", "arma", 10, "dano médio", 1)
        elif escolha == "3":
            arma = itens.criar_item("estaca", "arma", 15, "dano alto", 1)
        else:
            print("Opção inválida. Tente novamente.")
            continue

        inventario.adicionar_item_inventario(jogador["inventario"], arma)
        break

    texto2 = (f"""
Enquanto procura recursos, um barulho de grunhido junto com passos lentos e batidas em portas vem do andar de cima.

Uma pessoa infectada está presa em um dos quartos.

O que você vai fazer?

1 - Usar sua arma para lutar contra o {cores.verdeT("zumbi")} e tentar matá-lo.
2 - Sair de fininho da casa e sair em busca de outro lugar para se abrigar.
""")
    utils.mostrar_texto_com_delay(texto2, 0.05)

    while True:
        escolha2 = utils.pedir_escolha(jogador=jogador)

        if escolha2 == "1":
            print("""
Você decide enfrentar o zumbi...

Você se prepara para o combate, segurando firmemente sua arma escolhida.

Lentamente, você sobe as escadas, cada passo ecoando pela casa silenciosa.

Então, você encontra a porta do quarto trancada. O grunhido fica mais alto e você percebe que o zumbi está tentando sair.

Você, já armado com sua arma, se prepara para o confronto. O zumbi finalmente consegue abrir a porta e avança em sua direção.
""")

            inimigo = classes.criar_inimigo("Zumbi Fraco", 50, 10, 5, 20, 10)
            resultado = combate.iniciar_combate(jogador, inimigo)
            if resultado is True:
                print("\nA casa está segura... por enquanto.")
            elif resultado is False:
                print("\nSua jornada termina aqui.")
            break
        elif escolha2 == "2":
            print("Você decide sair da casa e procurar outro lugar para se abrigar.")
            break
        else:
            print("Opção inválida. Tente novamente.")
            continue


def fase2(jogador):
    print("\nFASE 2 — A FLORESTA SOMBRIA")
    texto = (f"""
Você deixa a casa para trás e mergulha na escuridão da floresta que cerca a estrada.

As árvores altas bloqueiam quase toda a luz da lua, e o som dos seus próprios passos parece ecoar mais do que deveria.

Depois de alguns minutos caminhando, você encontra uma lanterna ainda funcionando, largada perto de uma fogueira apagada há dias. Você a guarda, sabendo que pode precisar dela mais à frente.

De repente, um rosnado grave corta o silêncio. Não é o gemido lento de um {cores.verdeT("zumbi")} — é mais rápido, mais animal.

Entre as árvores, você vê pares de olhos brilhando no escuro. Uma {cores.verdeT("matilha de cães infectados")} pelo vírus se aproxima, rosnando e batendo os dentes.

O que você vai fazer?

1 - Lutar contra a matilha usando sua arma.
2 - Subir em uma árvore próxima e esperar os cães perderem o interesse.
""")
    utils.mostrar_texto_com_delay(texto, 0.05)

    inventario.adicionar_item_inventario(
        jogador["inventario"],
        itens.criar_item("lanterna", "ferramenta", 0, "ilumina o caminho em lugares escuros", 1),
    )

    while True:
        escolha = utils.pedir_escolha(jogador=jogador)

        if escolha == "1":
            print("""
Você segura sua arma com força e planta os pés no chão coberto de folhas.

A matilha avança rápido, contornando você por todos os lados. Não há tempo para pensar — só para reagir.
""")
            inimigo = classes.criar_inimigo("Matilha Infectada", 40, 8, 15, 5, 5)
            resultado = combate.iniciar_combate(jogador, inimigo)
            if resultado is True:
                print("\nOs cães que sobraram fogem uivando para dentro da mata. Você respira fundo, aliviado.")
            elif resultado is False:
                print("\nSua jornada termina aqui.")
            elif resultado is None:
                print("\nVocê se afasta o quanto pode, o coração ainda acelerado.")
            break
        elif escolha == "2":
            print("""
Você se agarra ao tronco de uma árvore próxima e sobe o mais rápido que consegue.

Os cães latem furiosamente logo abaixo, arranhando o tronco, mas não conseguem alcançá-lo.

Depois de alguns minutos tensos, a matilha perde o interesse e segue seu caminho pela floresta.
""")
            break
        else:
            print("Opção inválida. Tente novamente.")
            continue


def fase3(jogador):
    print("\nFASE 3 — O POSTO DE GASOLINA")
    texto = (f"""
Ao amanhecer, você avista um posto de gasolina abandonado à beira da estrada, com um letreiro quebrado balançando ao vento.

Suas provisões estão acabando, então você decide se arriscar e entrar.

Dentro da loja de conveniência, as prateleiras estão parcialmente saqueadas, mas ainda restam alguns itens úteis.

Antes que você consiga pegar qualquer coisa, uma voz rouca fala atrás de você:

— Devagar. Isso tudo é meu agora.

Um {cores.vermelhoT("sobrevivente armado")} surge de trás do balcão, segurando um cano de metal, os olhos fundos e desconfiados de quem sobreviveu sozinho por tempo demais.

— Você vai embora com as mãos vazias, ou vai embora sem elas. A escolha é sua.

O que você vai fazer?

1 - Enfrentar o saqueador para proteger o que encontrar.
2 - Recuar e sair do posto sem confronto.
""")
    utils.mostrar_texto_com_delay(texto, 0.05)

    while True:
        escolha = utils.pedir_escolha(jogador=jogador)

        if escolha == "1":
            print("""
Você não vai recuar. Não depois de tudo que passou para chegar até aqui.

O saqueador avança primeiro, o cano de metal cortando o ar em sua direção.
""")
            inimigo = classes.criar_inimigo("Saqueador", 60, 12, 8, 15, 8)
            resultado = combate.iniciar_combate(jogador, inimigo)
            if resultado is True:
                print("\nCom o saqueador derrotado, você reúne o que restou nas prateleiras.")
                inventario.adicionar_item_inventario(
                    jogador["inventario"],
                    itens.criar_recurso("barra de cereal", "comida", "restaura 15 de fome", 2, restaura_fome=15),
                )
            elif resultado is False:
                print("\nSua jornada termina aqui.")
            elif resultado is None:
                print("\nVocê consegue se afastar, mas sente que fez um inimigo.")
            break
        elif escolha == "2":
            print("""
Você levanta as mãos lentamente e recua até a porta.

O saqueador não baixa a guarda até você desaparecer na estrada, mas ao menos ninguém se feriu.
""")
            break
        else:
            print("Opção inválida. Tente novamente.")
            continue


def fase4(jogador):
    print("\nFASE 4 — A CIDADE EM RUÍNAS")
    texto = (f"""
A estrada termina nos arredores de uma cidade que já foi grande. Prédios pela metade, carros amontoados e um silêncio pesado tomam conta de tudo.

Você atravessa uma avenida coberta de mato quando escuta passos — rápidos demais para serem de um zumbi comum.

Vindo de uma esquina, um {cores.verdeT("zumbi corredor")} dispara em sua direção, os movimentos bruscos e imprevisíveis, muito mais ágil do que qualquer infectado que você já viu.

Não há tempo para pensar em rotas alternativas.

O que você vai fazer?

1 - Ficar firme e enfrentá-lo antes que ele alcance você.
2 - Correr em direção a um prédio próximo e tentar trancar a porta.
""")
    utils.mostrar_texto_com_delay(texto, 0.05)

    while True:
        escolha = utils.pedir_escolha(jogador=jogador)

        if escolha == "1":
            print("""
Você planta os pés e ergue sua arma bem no momento em que o zumbi corredor se lança contra você.
""")
            inimigo = classes.criar_inimigo("Zumbi Corredor", 70, 15, 20, 15, 8)
            resultado = combate.iniciar_combate(jogador, inimigo)
            if resultado is True:
                print("\nO zumbi corredor finalmente para de se mexer. Sua respiração ainda está descompassada.")
            elif resultado is False:
                print("\nSua jornada termina aqui.")
            elif resultado is None:
                print("\nVocê escapa por pouco, o som de passos ainda ecoando atrás de você.")
            break
        elif escolha == "2":
            print("""
Você dispara em direção ao prédio mais próximo, os pulmões ardendo.

Na última fração de segundo, você entra e consegue trancar a porta enferrujada, ouvindo o zumbi bater do outro lado até desistir e seguir em frente.
""")
            break
        else:
            print("Opção inválida. Tente novamente.")
            continue


def fase5(jogador):
    print("\nFASE 5 — O HOSPITAL ABANDONADO")
    texto = (f"""
Seguindo placas desbotadas, você chega a um hospital que serviu como um dos últimos pontos de triagem antes do colapso.

Os corredores estão cobertos de macas viradas, prontuários espalhados e um cheiro que você prefere não identificar.

Você precisa de remédios — sua ferida do combate anterior ainda dói — e a farmácia do hospital pode ser sua única chance.

Ao entrar na ala de quarentena, você encontra algo que já foi um paciente. O corpo está deformado de um jeito que você nunca viu antes, os membros estendidos em ângulos errados.

Um {cores.verdeT("zumbi mutante")} vira lentamente a cabeça em sua direção.

O que você vai fazer?

1 - Enfrentar o zumbi mutante para conseguir chegar à farmácia.
2 - Tentar contornar a sala pela lateral, em silêncio.
""")
    utils.mostrar_texto_com_delay(texto, 0.05)

    while True:
        escolha = utils.pedir_escolha(jogador=jogador)

        if escolha == "1":
            print("""
Não há como passar despercebido por aquela coisa. Você se posiciona entre as macas e se prepara para o pior.
""")
            inimigo = classes.criar_inimigo("Zumbi Mutante", 100, 20, 10, 30, 20)
            resultado = combate.iniciar_combate(jogador, inimigo)
            if resultado is True:
                print("\nCom o caminho livre, você finalmente alcança a farmácia e encontra alguns suprimentos médicos.")
                inventario.adicionar_item_inventario(
                    jogador["inventario"],
                    itens.criar_recurso("kit médico", "cura", "restaura vida", 1, restaura_vida=30, bonus_resistencia=1),
                )
            elif resultado is False:
                print("\nSua jornada termina aqui.")
            elif resultado is None:
                print("\nVocê recua da sala, sem conseguir chegar à farmácia dessa vez.")
            break
        elif escolha == "2":
            print("""
Você se move devagar, colado à parede, prendendo a respiração a cada passo.

O zumbi mutante balança a cabeça, como se farejasse o ar, mas não chega a notar você.

Você consegue sair da ala de quarentena, ainda que sem os remédios que procurava.
""")
            break
        else:
            print("Opção inválida. Tente novamente.")
            continue


def fase6(jogador):
    print("\nFASE 6 — A PONTE BLOQUEADA")
    texto = (f"""
O único caminho adiante é uma longa ponte sobre um rio seco. Carros militares abandonados bloqueiam quase toda a passagem.

Ao se aproximar, você percebe uma figura enorme parada entre os veículos — um {cores.verdeT("zumbi")} que ainda veste os restos de um uniforme militar, os ombros largos e os movimentos pesados.

Diferente dos outros que você enfrentou, esse {cores.verdeT("Zumbi Forte")} não se move até você chegar perto. Ele parece... guardar a passagem.

Não existe outro caminho visível para atravessar o rio.

O que você vai fazer?

1 - Atacar o zumbi forte de surpresa antes que ele reaja.
2 - Tentar se esgueirar por baixo dos carros enquanto ele não olha.
""")
    utils.mostrar_texto_com_delay(texto, 0.05)

    while True:
        escolha = utils.pedir_escolha(jogador=jogador)

        if escolha == "1":
            print("""
Você respira fundo e avança, tentando aproveitar o elemento surpresa antes que aquela massa de músculos e podridão perceba sua presença.
""")
            inimigo = classes.criar_inimigo("Zumbi Forte", 150, 30, 15, 40, 30)
            resultado = combate.iniciar_combate(jogador, inimigo)
            if resultado is True:
                print("\nO gigante finalmente desaba entre os carros. A ponte está livre.")
            elif resultado is False:
                print("\nSua jornada termina aqui.")
            elif resultado is None:
                print("\nVocê recua da ponte, os passos pesados do zumbi ainda ecoando atrás de você.")
            break
        elif escolha == "2":
            print("""
Você se abaixa e desliza por baixo de um dos caminhões enferrujados, tentando não fazer barulho.

O zumbi forte vira a cabeça lentamente, mas você já está do outro lado antes que ele reaja de verdade.

Ofegante, você atravessa o restante da ponte sem olhar para trás.
""")
            break
        else:
            print("Opção inválida. Tente novamente.")
            continue


def fase7(jogador):
    print("\nFASE 7 — OS ESGOTOS")
    texto = (f"""
Do outro lado da ponte, a estrada está completamente destruída, forçando você a descer por uma escotilha aberta que leva aos esgotos da cidade.

A água suja cobre seus tornozelos, e o eco de gotejamentos distantes é a única coisa que quebra o silêncio.

Algo se move na água à sua frente — devagar, quase deslizando. Quando finalmente emerge, você vê uma criatura que já não se parece mais com um ser humano.

Pele grudada aos ossos, membros alongados demais, uma {cores.verdeT("aberração")} nascida de tempo demais exposta ao vírus e à escuridão.

O que você vai fazer?

1 - Enfrentar a aberração antes que ela ataque primeiro.
2 - Recuar pela escotilha e procurar outra rota pela superfície.
""")
    utils.mostrar_texto_com_delay(texto, 0.05)

    while True:
        escolha = utils.pedir_escolha(jogador=jogador)

        if escolha == "1":
            print("""
Não há espaço para recuar nesse corredor estreito. Você segura sua arma com as duas mãos e avança.
""")
            inimigo = classes.criar_inimigo("Aberração", 180, 35, 12, 45, 25)
            resultado = combate.iniciar_combate(jogador, inimigo)
            if resultado is True:
                print("\nA criatura finalmente para de se mexer, afundando lentamente na água escura.")
            elif resultado is False:
                print("\nSua jornada termina aqui.")
            elif resultado is None:
                print("\nVocê se afasta pela água, sem saber se aquilo ainda está te seguindo.")
            break
        elif escolha == "2":
            print("""
Você não quer descobrir do que aquela coisa é capaz. Sobe de volta pela escotilha o mais rápido possível.

Vai ter que encontrar outro caminho pela superfície, mesmo que isso signifique mais exposição.
""")
            break
        else:
            print("Opção inválida. Tente novamente.")
            continue


def fase8(jogador):
    print("\nFASE 8 — A FAZENDA ISOLADA")
    texto = (f"""
Longe da cidade, você encontra uma fazenda isolada, cercas caídas e um celeiro ainda de pé no meio do campo.

Faminto e exausto, você se aproxima em busca de comida e um lugar seguro para descansar.

Dentro do celeiro, entre fardos de feno apodrecidos, algo se move pesadamente. Um som de respiração pesada, quase animal, mas errada demais para ser normal.

Uma {cores.verdeT("fera infectada")} — o que restou de um antigo animal da fazenda — ergue a cabeça na sua direção, os olhos injetados de sangue.

O que você vai fazer?

1 - Enfrentar a fera antes que ela avance sobre você.
2 - Sair devagar do celeiro e procurar comida em outro lugar da fazenda.
""")
    utils.mostrar_texto_com_delay(texto, 0.05)

    while True:
        escolha = utils.pedir_escolha(jogador=jogador)

        if escolha == "1":
            print("""
Não há tempo para hesitar. A fera já está avançando, o chão tremendo sob seu peso.
""")
            inimigo = classes.criar_inimigo("Fera Infectada", 200, 40, 18, 20, 35)
            resultado = combate.iniciar_combate(jogador, inimigo)
            if resultado is True:
                print("\nA fera finalmente cai no chão do celeiro, imóvel. Você se apoia na parede, exausto.")
                inventario.adicionar_item_inventario(
                    jogador["inventario"],
                    itens.criar_recurso("carne", "comida", "restaura 25 de fome", 2, restaura_fome=25, bonus_forca=1),
                )
            elif resultado is False:
                print("\nSua jornada termina aqui.")
            elif resultado is None:
                print("\nVocê consegue escapar do celeiro, o coração disparado.")
            break
        elif escolha == "2":
            print("""
Você recua devagar, sem tirar os olhos da criatura, até sair do celeiro.

A casa principal da fazenda ainda pode ter alguma comida guardada — vale a pena arriscar por ali.
""")
            break
        else:
            print("Opção inválida. Tente novamente.")
            continue


def fase9(jogador):
    print("\nFASE 9 — O POSTO MILITAR ABANDONADO")
    texto = (f"""
Nos limites da fazenda, você encontra um antigo posto de bloqueio militar — sacos de areia, barricadas e um portão de metal reforçado, tudo agora enferrujado e coberto de mato.

Esse tipo de posto costumava guardar armas, munição e suprimentos. Vale a pena arriscar entrar.

Ao forçar o portão, você percebe uma figura parada no centro do pátio, ainda vestindo o que resta de uma armadura militar pesada.

O {cores.vermelhoT("Zumbi Chefe")} — o que um dia foi o comandante daquele posto — ergue a cabeça devagar, como se ainda guardasse algum resquício de autoridade sobre aquele lugar.

O que você vai fazer?

1 - Enfrentar o comandante para ter acesso ao arsenal do posto.
2 - Recuar e abandonar a ideia de entrar no posto.
""")
    utils.mostrar_texto_com_delay(texto, 0.05)

    while True:
        escolha = utils.pedir_escolha(jogador=jogador)

        if escolha == "1":
            print("""
Você entra no pátio, sabendo que não há como negociar com aquilo em que o comandante se tornou.
""")
            inimigo = classes.criar_inimigo("Zumbi Chefe", 200, 40, 20, 50, 40)
            resultado = combate.iniciar_combate(jogador, inimigo)
            if resultado is True:
                print("\nO comandante finalmente desaba entre os sacos de areia. O posto está sob seu controle agora.")
                inventario.adicionar_item_inventario(
                    jogador["inventario"],
                    itens.criar_item("faca militar", "arma", 20, "dano alto", 1),
                )
            elif resultado is False:
                print("\nSua jornada termina aqui.")
            elif resultado is None:
                print("\nVocê recua do posto, sem conseguir vencer o comandante dessa vez.")
            break
        elif escolha == "2":
            print("""
Algo no olhar daquela criatura te faz recuar. Você fecha o portão devagar e se afasta do posto, decidindo não arriscar dessa vez.
""")
            break
        else:
            print("Opção inválida. Tente novamente.")
            continue


def fase10(jogador):
    print("\nFASE 10 — O BUNKER SUBTERRÂNEO")
    texto = (f"""
Um mapa encontrado no posto militar indica a entrada de um bunker subterrâneo nas proximidades — construído para abrigar sobreviventes durante o início do surto.

Talvez ainda haja pessoas vivas lá dentro. Talvez apenas respostas sobre o que realmente aconteceu.

A escotilha de entrada está parcialmente aberta, luzes de emergência piscando fracamente no túnel abaixo.

No meio da escuridão, bloqueando a passagem, está o que restou de alguém que morreu tentando proteger aquele lugar — um {cores.vermelhoT("Zumbi Supremo")}, maior e mais resistente que qualquer coisa que você já enfrentou.

O que você vai fazer?

1 - Enfrentar o Zumbi Supremo para conseguir entrar no bunker.
2 - Recuar e procurar outra entrada para o bunker.
""")
    utils.mostrar_texto_com_delay(texto, 0.05)

    while True:
        escolha = utils.pedir_escolha(jogador=jogador)

        if escolha == "1":
            print("""
Não existe espaço para hesitar. Você desce o túnel, sabendo que talvez essa seja a luta mais difícil até agora.
""")
            inimigo = classes.criar_inimigo("Zumbi Supremo", 300, 50, 25, 60, 50)
            resultado = combate.iniciar_combate(jogador, inimigo)
            if resultado is True:
                print("\nO Zumbi Supremo finalmente cai, e o silêncio do bunker toma conta do túnel. Você está exausto, mas vivo.")
            elif resultado is False:
                print("\nSua jornada termina aqui.")
            elif resultado is None:
                print("\nVocê recua do túnel, sem conseguir entrar no bunker dessa vez.")
            break
        elif escolha == "2":
            print("""
Você decide não arriscar contra aquela coisa agora. Rodeando a área, você procura outra forma de entrada, mesmo que isso tome mais tempo.
""")
            break
        else:
            print("Opção inválida. Tente novamente.")
            continue


def fase11(jogador):
    print("\nFASE 11 — O SINAL DE RÁDIO")
    texto = (f"""
Dentro do bunker, entre arquivos destruídos e terminais quebrados, você encontra uma anotação recente: um sinal de rádio ainda está sendo transmitido de uma torre nas montanhas próximas.

Pode ser um grupo de sobreviventes. Pode ser sua única chance de não estar mais sozinho neste mundo.

Você segue as coordenadas até encontrar a torre, alta e enferrujada, o sinal piscando fracamente no topo.

Na base da torre, um {cores.verdeT("zumbi sentinela")} está parado, imóvel, como se estivesse ali apenas para impedir a passagem de qualquer um que se aproximasse.

O que você vai fazer?

1 - Enfrentar o sentinela e subir até o topo da torre.
2 - Tentar contornar a base e subir pela escada externa, sem ser notado.
""")
    utils.mostrar_texto_com_delay(texto, 0.05)

    while True:
        escolha = utils.pedir_escolha(jogador=jogador)

        if escolha == "1":
            print("""
Você se aproxima devagar, arma em punho, sabendo que o topo da torre é a única coisa que importa agora.
""")
            inimigo = classes.criar_inimigo("Zumbi Sentinela", 120, 25, 15, 35, 25)
            resultado = combate.iniciar_combate(jogador, inimigo)
            if resultado is True:
                print("\nO sentinela cai ao pé da torre. O caminho até o topo está livre.")
            elif resultado is False:
                print("\nSua jornada termina aqui.")
            elif resultado is None:
                print("\nVocê se afasta da base da torre, ainda tenso, mas vivo.")
            break
        elif escolha == "2":
            print("""
Você se move rente à estrutura de metal, evitando qualquer barulho, e encontra uma escada externa do lado oposto da torre.

Devagar, sem chamar atenção do sentinela, você começa a subir.
""")
            break
        else:
            print("Opção inválida. Tente novamente.")
            continue

    if jogador_vivo(jogador):
        cliffhanger = (f"""
Você finalmente alcança o topo da torre, ofegante. O rádio ainda transmite, estático e fraco, um som quase humano tentando dizer alguma coisa.

Antes que consiga se aproximar do equipamento, um rugido profundo faz toda a estrutura da torre tremer.

Nas árvores ao redor, uma silhueta enorme observa você de longe. Não se move como os outros infectados. Não faz o mesmo som.

Ela é maior. Mais silenciosa. E, de alguma forma, parece estar esperando.

Uma palavra ecoa na sua mente, vinda de lugar nenhum:

"{cores.vermelhoT("Tchola")}"

A criatura não ataca. Apenas observa — como se soubesse que ainda não é a hora.

Você segura o rádio com as mãos trêmulas, sabendo que sua jornada está longe de terminar.

(CONTINUA...)
""")
        utils.mostrar_texto_com_delay(cliffhanger, 0.05)


def fase12(jogador):
    print("\nFASE 12 — A TRANSMISSÃO")
    texto = (f"""
No topo da torre, você finalmente consegue ajustar o rádio. Em meio ao chiado, uma mensagem se repete em intervalos curtos:

\"...sobreviventes, não sigam para Concórdia. A cura foi transferida para o {cores.amareloT('Complexo Éden')}. Coordenadas anexadas...\"

Antes que o sinal desapareça, outra voz interrompe a transmissão. Ela diz estar escondida em uma oficina próxima e pede ajuda para chegar ao complexo.

Ao descer a torre, você encontra a oficina indicada. A porta está aberta e um sobrevivente ferido está cercado por dois infectados.

O que você vai fazer?

1 - Ajudar o sobrevivente e enfrentar os infectados.
2 - Evitar o confronto e seguir sozinho rumo às coordenadas.
""")
    utils.mostrar_texto_com_delay(texto, 0.05)

    while True:
        escolha = utils.pedir_escolha(jogador=jogador)

        if escolha == "1":
            print("""
Você avança para afastar os infectados antes que eles percebam o sobrevivente.
""")
            inimigo = classes.criar_inimigo("Infectados da Oficina", 140, 28, 14, 25, 20)
            resultado = combate.iniciar_combate(jogador, inimigo)
            if resultado is True:
                print("\nO sobrevivente agradece e se apresenta como Caio. Ele diz conhecer uma entrada de serviço do Complexo Éden.")
                jogador["aliado"] = "Caio"
            elif resultado is False:
                print("\nSua jornada termina aqui.")
            elif resultado is None:
                print("\nVocê se afasta da oficina. O pedido de ajuda fica para trás junto com o sinal de rádio.")
            break
        elif escolha == "2":
            print("""
Você não pode correr o risco de ficar preso ali. Guarda as coordenadas e segue pela estrada secundária, sozinho.
""")
            jogador["aliado"] = None
            break
        else:
            print("Opção inválida. Tente novamente.")
            continue


def fase13(jogador):
    print("\nFASE 13 — A ROTA INTERDITADA")
    texto = (f"""
As coordenadas apontam para uma estrada de serviço fora da cidade. No caminho, um bloqueio feito de ônibus e carros abandonados impede a passagem.

Entre os veículos, você encontra um mapa militar rasgado. Nele está escrito: \"ÉDEN — Unidade principal. Acesso restrito.\"

Enquanto examina o mapa, passos rápidos começam a ecoar entre os carros. Um grupo de {cores.verdeT('zumbis corredores')} está vindo pelo outro lado do bloqueio.

O que você vai fazer?

1 - Enfrentar os corredores para vasculhar os veículos por suprimentos.
2 - Escalar o bloqueio e atravessar antes que eles cheguem.
""")
    utils.mostrar_texto_com_delay(texto, 0.05)

    while True:
        escolha = utils.pedir_escolha(jogador=jogador)

        if escolha == "1":
            print("""
Você escolhe não abandonar uma chance de conseguir recursos. Entre os veículos, não existe muito espaço para errar.
""")
            inimigo = classes.criar_inimigo("Grupo de Corredores", 170, 32, 24, 30, 25)
            resultado = combate.iniciar_combate(jogador, inimigo)
            if resultado is True:
                print("\nCom o caminho livre, você encontra água, bandagens e uma barra de energia em uma mochila militar.")
                inventario.adicionar_item_inventario(
                    jogador["inventario"],
                    itens.criar_recurso("barra de energia", "comida", "restaura 20 de fome", 2, restaura_fome=20),
                    mostrar=False,
                )
                inventario.adicionar_item_inventario(
                    jogador["inventario"],
                    itens.criar_recurso("bandagem", "cura", "restaura vida", 1, restaura_vida=15),
                    mostrar=False,
                )
                inventario.mostrar_inventario(jogador["inventario"])
            elif resultado is False:
                print("\nSua jornada termina aqui.")
            elif resultado is None:
                print("\nVocê abandona os veículos e encontra uma passagem estreita pelo acostamento.")
            break
        elif escolha == "2":
            print("""
Você sobe sobre os carros enferrujados e atravessa sem olhar para trás. O metal range, mas aguenta o seu peso até o outro lado.
""")
            break
        else:
            print("Opção inválida. Tente novamente.")
            continue


def fase14(jogador):
    print("\nFASE 14 — OS SAQUEADORES")
    texto = (f"""
Ao cair da tarde, uma antiga estação rodoviária surge ao lado da estrada. Ela parece vazia, mas luzes fracas acesas nos fundos denunciam que alguém está usando o local.

Você escuta homens falando sobre uma instalação de pesquisa e percebe que eles também conhecem o nome Projeto Éden.

Antes que consiga sair, um saqueador armado aparece na entrada e bloqueia seu caminho.

O que você vai fazer?

1 - Enfrentar o saqueador para abrir caminho.
2 - Se esconder entre os ônibus e esperar o grupo sair.
""")
    utils.mostrar_texto_com_delay(texto, 0.05)

    while True:
        escolha = utils.pedir_escolha(jogador=jogador)

        if escolha == "1":
            print("""
O saqueador avança, convencido de que você será apenas mais uma pessoa a entregar a mochila e fugir.
""")
            inimigo = classes.criar_inimigo("Saqueador Armado", 180, 35, 18, 35, 25)
            resultado = combate.iniciar_combate(jogador, inimigo, combate.OPCOES_CONFRONTO_DIRETO)
            if resultado is True:
                print("\nCom a passagem livre, você escuta o líder do grupo gritar: \"Peguem a amostra antes que ela saia de lá!\"")
            elif resultado is False:
                print("\nSua jornada termina aqui.")
            elif resultado is None:
                print("\nVocê consegue se afastar pela saída lateral, mas os saqueadores continuam procurando pela região.")
            break
        elif escolha == "2":
            print("""
Você se esconde entre dois ônibus e espera em silêncio. Depois de alguns minutos, o grupo parte em caminhonetes na direção do Complexo Éden.

Agora você sabe que está em uma corrida pela cura.
""")
            break
        else:
            print("Opção inválida. Tente novamente.")
            continue


def fase15(jogador):
    print("\nFASE 15 — BOSS: O GUARDIÃO")
    texto = (f"""
Pouco antes do Complexo Éden, a estrada termina em um túnel de manutenção. Na entrada há equipamentos científicos quebrados e uma placa: \"SETOR DE CONTENÇÃO\".

O rugido que você ouviu na torre volta a ecoar. Das sombras surge um infectado enorme, coberto por partes de uma antiga proteção de segurança.

Ele não se afasta da passagem. Parece ter sido deixado ali para impedir que qualquer pessoa chegue à instalação.

O que você vai fazer?

1 - Enfrentar o Guardião e atravessar o túnel.
2 - Procurar uma rota estreita pelas tubulações laterais.
""")
    utils.mostrar_texto_com_delay(texto, 0.05)

    while True:
        escolha = utils.pedir_escolha(jogador=jogador)

        if escolha == "1":
            print("""
Você usa as barreiras e as caixas espalhadas pelo túnel para manter distância da criatura enquanto procura uma abertura.
""")
            inimigo = classes.criar_inimigo("Guardião do Túnel", 360, 52, 18, 45, 45)
            resultado = combate.iniciar_combate(jogador, inimigo, combate.OPCOES_CONFRONTO_DIRETO)
            if resultado is True:
                print("\nO Guardião cai e a passagem finalmente fica livre. Próximo à entrada, você encontra um cartão de acesso com o símbolo de Éden.")
                inventario.adicionar_item_inventario(
                    jogador["inventario"],
                    itens.criar_item("cartão de acesso Éden", "chave", 0, "abre setores restritos", 1),
                )
            elif resultado is False:
                print("\nSua jornada termina aqui.")
            elif resultado is None:
                print("\nVocê escapa pelas tubulações, deixando para trás a entrada principal e o cartão de acesso.")
            break
        elif escolha == "2":
            print("""
Você se arrasta por uma tubulação estreita. O caminho demora mais, mas desemboca atrás dos muros do complexo.
""")
            break
        else:
            print("Opção inválida. Tente novamente.")
            continue


def fase16(jogador):
    print("\nFASE 16 — OS PORTÕES DE ÉDEN")
    texto = (f"""
Do outro lado do túnel, o Complexo Éden aparece diante de você: muros altos, câmeras desligadas e portas de metal parcialmente abertas.

Há sinais de uma batalha recente perto da entrada. Os saqueadores chegaram primeiro, mas nenhum deles está por perto agora.

Quando você entra, os alto-falantes ganham vida:

\"PROTOCOLO DE CONTENÇÃO ATIVADO. SETORES SERÃO SELADOS.\"

Um infectado com uniforme de segurança aparece no corredor, bloqueando a porta que leva aos laboratórios.

O que você vai fazer?

1 - Enfrentar o segurança e atravessar o corredor principal.
2 - Correr até a porta de manutenção antes que o setor seja fechado.
""")
    utils.mostrar_texto_com_delay(texto, 0.05)

    while True:
        escolha = utils.pedir_escolha(jogador=jogador)

        if escolha == "1":
            print("""
As luzes de emergência piscam enquanto você se prepara. A cada segundo, mais portas se fecham ao seu redor.
""")
            inimigo = classes.criar_inimigo("Segurança Infectado", 240, 42, 20, 40, 35)
            resultado = combate.iniciar_combate(jogador, inimigo)
            if resultado is True:
                print("\nVocê atravessa o corredor antes que as portas pesadas se fechem.")
            elif resultado is False:
                print("\nSua jornada termina aqui.")
            elif resultado is None:
                print("\nVocê usa a confusão para chegar à porta de manutenção por pouco.")
            break
        elif escolha == "2":
            print("""
Você corre pelo corredor e passa pela porta no último instante. Atrás de você, o sistema fecha o setor com um estrondo.
""")
            break
        else:
            print("Opção inválida. Tente novamente.")
            continue


def fase17(jogador):
    print("\nFASE 17 — A VERDADE DO PROJETO ÉDEN")
    texto = (f"""
Nos laboratórios, computadores de emergência ainda exibem relatórios do Projeto Éden.

Você descobre que os pesquisadores realmente criaram um composto capaz de interromper a infecção. Porém, havia poucas doses e os responsáveis decidiram escolher quem teria acesso a elas.

Éden nunca foi um plano para salvar todas as pessoas. Era um plano para selecionar quem mereceria um lugar depois do colapso.

Um terminal indica que a amostra original está na câmara central. Antes de chegar até ela, você encontra um pesquisador infectado vagando entre os equipamentos.

O que você vai fazer?

1 - Enfrentar o pesquisador para acessar os registros completos.
2 - Evitar a área e seguir direto para a câmara central.
""")
    utils.mostrar_texto_com_delay(texto, 0.05)

    while True:
        escolha = utils.pedir_escolha(jogador=jogador)

        if escolha == "1":
            print("""
Você precisa das respostas antes de decidir o que fazer com a cura. O pesquisador percebe sua presença e avança entre as bancadas.
""")
            inimigo = classes.criar_inimigo("Pesquisador Infectado", 260, 45, 18, 55, 30)
            resultado = combate.iniciar_combate(jogador, inimigo)
            if resultado is True:
                print("\nNos arquivos, você confirma: a amostra E-01 pode ser reproduzida e transformada em novas doses.")
            elif resultado is False:
                print("\nSua jornada termina aqui.")
            elif resultado is None:
                print("\nVocê se afasta dos terminais e segue para a câmara sem todos os detalhes.")
            break
        elif escolha == "2":
            print("""
Você não tem tempo para mais perguntas. A câmara central é a única coisa que importa agora.
""")
            break
        else:
            print("Opção inválida. Tente novamente.")
            continue


def fase18(jogador):
    print("\nFASE 18 — A TRAIÇÃO")
    aliado = jogador.get("aliado")
    if aliado:
        texto = (f"""
Você encontra {aliado} diante da porta da câmara central. Ele parece aliviado por você ter chegado até ali.

Então ele pega o cartão de acesso e aponta uma arma para você.

— Eu não vim procurar abrigo. Vim procurar a amostra. Você me ajudou a chegar até aqui, mas não preciso mais de você.

O que você vai fazer?

1 - Enfrentar {aliado} antes que ele entre na câmara.
2 - Correr por uma passagem lateral e tentar chegar primeiro à outra porta.
""")
        nome_inimigo = "Caio, o Traidor"
    else:
        texto = (f"""
Perto da câmara central, você encontra o líder dos saqueadores. Ele segura um cartão de acesso e sorri ao perceber que você chegou sozinho.

— Obrigado por abrir caminho. Agora a amostra é minha.

O que você vai fazer?

1 - Enfrentar o líder antes que ele entre na câmara.
2 - Correr por uma passagem lateral e tentar chegar primeiro à outra porta.
""")
        nome_inimigo = "Líder dos Saqueadores"

    utils.mostrar_texto_com_delay(texto, 0.05)

    while True:
        escolha = utils.pedir_escolha(jogador=jogador)

        if escolha == "1":
            print("""
Você não pode deixar que a única chance de criar uma cura fique nas mãos de alguém que pensa apenas em si mesmo.
""")
            inimigo = classes.criar_inimigo(nome_inimigo, 280, 48, 20, 45, 35)
            resultado = combate.iniciar_combate(jogador, inimigo, combate.OPCOES_CONFRONTO_DIRETO)
            if resultado is True:
                print("\nO caminho até a câmara está livre, mas o alarme de contenção começa a tocar por toda a instalação.")
            elif resultado is False:
                print("\nSua jornada termina aqui.")
            elif resultado is None:
                print("\nVocê se afasta e encontra a passagem lateral. O traidor segue para a câmara à sua frente.")
            break
        elif escolha == "2":
            print("""
Você dispara pela passagem lateral. O som do alarme aumenta, avisando que alguma coisa foi solta nos setores inferiores.
""")
            break
        else:
            print("Opção inválida. Tente novamente.")
            continue


def fase19(jogador):
    print("\nFASE 19 — A ÚLTIMA AMOSTRA")
    texto = (f"""
Você finalmente alcança a câmara refrigerada. Dentro dela, um pequeno recipiente está marcado como {cores.amareloT('AMOSTRA E-01')}.

No monitor ao lado, uma mensagem confirma que aquela amostra pode ser replicada. Ela não é apenas uma dose: é a possibilidade de fabricar uma cura novamente.

Antes que você consiga abrir a câmara, uma porta enorme começa a se destrancar. O sistema anuncia:

\"FALHA DE CONTENÇÃO. EXPERIMENTO E-00 LIBERADO.\"

Uma criatura de laboratório se aproxima entre as luzes de emergência, impedindo você de chegar ao recipiente.

O que você vai fazer?

1 - Enfrentar a criatura e proteger a amostra.
2 - Se esconder atrás das bancadas até encontrar uma chance de chegar à câmara.
""")
    utils.mostrar_texto_com_delay(texto, 0.05)

    while True:
        escolha = utils.pedir_escolha(jogador=jogador)

        if escolha == "1":
            print("""
Você se coloca entre a criatura e a câmara. O laboratório inteiro treme com as portas de segurança abrindo e fechando.
""")
            inimigo = classes.criar_inimigo("Experimento E-00", 330, 55, 25, 55, 40)
            resultado = combate.iniciar_combate(jogador, inimigo)
            if resultado is True:
                print("\nVocê alcança o painel e destrava a câmara. A amostra E-01 está ao seu alcance.")
                inventario.adicionar_item_inventario(
                    jogador["inventario"],
                    itens.criar_item("amostra E-01", "missão", 0, "pode ser replicada para criar uma cura", 1),
                )
            elif resultado is False:
                print("\nSua jornada termina aqui.")
            elif resultado is None:
                print("\nVocê encontra uma abertura e alcança a câmara, mas a criatura continua no laboratório.")
                inventario.adicionar_item_inventario(
                    jogador["inventario"],
                    itens.criar_item("amostra E-01", "missão", 0, "pode ser replicada para criar uma cura", 1),
                )
            break
        elif escolha == "2":
            print("""
Você se esconde entre as bancadas e espera a criatura se afastar. Quando ela muda de direção, você corre até o painel e pega a amostra.
""")
            inventario.adicionar_item_inventario(
                jogador["inventario"],
                itens.criar_item("amostra E-01", "missão", 0, "pode ser replicada para criar uma cura", 1),
            )
            break
        else:
            print("Opção inválida. Tente novamente.")
            continue


def fase20(jogador):
    print("\nFASE 20 — BOSS FINAL: TCHOLA")
    texto = (f"""
Com a amostra na mochila, você corre em direção à saída. Então as luzes se apagam por um instante.

Quando voltam, a silhueta que observava você da torre está no corredor: {cores.vermelhoT('Tchola')}.

Ele é o experimento mais antigo do Projeto Éden, mantido vivo após várias tentativas de cura. A criatura é rápida, silenciosa e parece reconhecer o recipiente que você carrega.

O sistema anuncia: \"AUTODESTRUIÇÃO INICIADA. EVACUEM A INSTALAÇÃO.\"

Não há mais como escapar sem abrir caminho.

O que você vai fazer?

1 - Enfrentar Tchola e garantir uma rota segura para sair do complexo.
2 - Tentar correr até a saída enquanto a instalação começa a desabar.
""")
    utils.mostrar_texto_com_delay(texto, 0.05)

    while True:
        escolha = utils.pedir_escolha(jogador=jogador)

        if escolha == "1":
            print("""
Você usa tudo o que aprendeu durante a jornada. O tempo está acabando, mas desistir agora significaria perder a última esperança de todos.
""")
            inimigo = classes.criar_inimigo("Tchola", 500, 60, 30, 70, 60)
            resultado = combate.iniciar_combate(jogador, inimigo, combate.OPCOES_CONFRONTO_DIRETO)
            if resultado is True:
                print("\nTchola finalmente cai. A rota até a saída fica livre entre os alarmes e as luzes de emergência.")
            elif resultado is False:
                print("\nSua jornada termina aqui.")
                break
            elif resultado is None:
                print("\nVocê consegue se afastar por alguns corredores, mas Tchola continua perseguindo você até a saída.")
            break
        elif escolha == "2":
            print("""
Você corre pelos corredores, desviando das portas que se fecham. Tchola vem logo atrás, mas você consegue alcançar a saída de emergência.
""")
            break
        else:
            print("Opção inválida. Tente novamente.")
            continue

    if jogador_vivo(jogador):
        final = (f"""
Do lado de fora, você olha para o Complexo Éden enquanto o sol começa a nascer.

Dentro da mochila está a {cores.amareloT('amostra E-01')}. Ela pode ser replicada. Pela primeira vez desde o início do apocalipse, existe uma chance real de criar uma cura.

Seu objetivo não é mais apenas sobreviver.

Agora é salvar quem ainda restou.

{cores.verdeT('FIM')}
""")
        utils.mostrar_texto_com_delay(final, 0.05)