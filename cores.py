import time
corT = 30

def cinzaT(p):
    return f"\033[1;{corT}m{p}\033[m"
def vermelhoT(p):
    return f"\033[1;{corT+1}m{p}\033[m"
def verdeT(p):
    return f"\033[1;{corT+2}m{p}\033[m"
def amareloT(p):
    return f"\033[1;{corT+3}m{p}\033[m"
def azulT(p):
    return f"\033[1;{corT+4}m{p}\033[m"
def rosaT(p):
    return f"\033[1;{corT+5}m{p}\033[m"
def cianoT(p):
    return f"\033[1;{corT+6}m{p}\033[m"
def brancoT(p):
    return f"\033[1;{corT+7}m{p}\033[m"


corF = 40
def cinzaF(p):
    return f"\033[1;{corF}m{p}\033[m"
def vermelhoF(p):
    return f"\033[1;{corF+1}m{p}\033[m"
def verdeF(p):
    return f"\033[1;{corF+2}m{p}\033[m"
def amareloF(p):
    return f"\033[1;{corF+3}m{p}\033[m"
def azulF(p):
    return f"\033[1;{corF+4}m{p}\033[m"
def rosaF(p):
    return f"\033[1;{corF+5}m{p}\033[m"
def cianoF(p):
    return f"\033[1;{corF+6}m{p}\033[m"
def brancoF(p):
    return f"\033[1;{corF+7}m{p}\033[m"

def iris(p):
    corI = 31
    i = 0
    while i < len(p):
        print(f"\033[1;{corI}m{p[i]}\033[m", end="", flush=True)
        time.sleep(0.13)
        i += 1
        corI += 1
        if corI > 37:
            corI = 31