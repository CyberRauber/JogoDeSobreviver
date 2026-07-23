import classes

p = 25

def cadastro(mA):
    nome = input("Cadastro do Usuário \n Digite o nome: ")
    print(f"Bem-vindo(a), {nome}! \n seus atributos iniciais são: ")
    print(mA)

def AddP(p):
    pass

def mA():
    return f"""
        Vida: {classes.vida}
        Força: {classes.forca}
        Velocidade: {classes.velocidade}
        Inteligência: {classes.inteligencia}
        Resistência: {classes.resistencia}
"""

mA = mA()

cadastro(mA)