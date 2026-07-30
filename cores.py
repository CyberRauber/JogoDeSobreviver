import time
cor = 30
def coresT(p):
    def cinza(p):
        return f"\033[1;{cor}m{p}\033[m"
    def vermelho(p):
        return f"\033[1;{cor+1}m{p}\033[m"
    def verde(p):
        return f"\033[1;{cor+2}m{p}\033[m"
    def amarelo(p):
        return f"\033[1;{cor+3}m{p}\033[m"
    def azul(p):
        return f"\033[1;{cor+4}m{p}\033[m"
    def rosa(p):
        return f"\033[1;{cor+5}m{p}\033[m"
    def ciano(p):
        return f"\033[1;{cor+6}m{p}\033[m"
    def branco(p):
        return f"\033[1;{cor+7}m{p}\033[m"

def coresF(p):
    cor = 40
    def cinza(p):
        return f"\033[1;{cor}m{p}\033[m"
    def vermelho(p):
        return f"\033[1;{cor+1}m{p}\033[m"
    def verde(p):
        return f"\033[1;{cor+2}m{p}\033[m"
    def amarelo(p):
        return f"\033[1;{cor+3}m{p}\033[m"
    def azul(p):
        return f"\033[1;{cor+4}m{p}\033[m"
    def rosa(p):
        return f"\033[1;{cor+5}m{p}\033[m"
    def ciano(p):
        return f"\033[1;{cor+6}m{p}\033[m"
    def branco(p):
        return f"\033[1;{cor+7}m{p}\033[m"

def iris(p):
    cor = 31
    i = 0
    while i < len(p):
        print(f"\033[1;{cor}m{p[i]}\033[m", end="", flush=True)
        time.sleep(0.13)
        i += 1
        cor += 1
        if cor > 37:
            cor = 31