import random


lista = [0]
money = 0.0
np = 1
nc = 3

def print_layout(lidos, Q, r1, r2, r3, r4, g, np, nc, money):
    
    value = str(g)
    count = len(lista)-1
    
    imprime_00 = '\n \n \n'
    imprime_01 = '************************ Show do Milhão ***************************'
    imprime_02 = '                                                      AJUDA:'
    imprime_03 = '                                                         P. PULAR x'
    imprime_04 = '                                                         C. CARDS x'
    imprime_05 = 'D. Desistir                                   Saldo: R$'

    print(imprime_00)
    print(imprime_01)
    print('\n', count, Q)
    print(imprime_02)
    print(imprime_03, np)
    print(imprime_04, nc)
    print('\n', r1, r2, r3, r4)
    print('\n', imprime_05, money)
    
    while(1):
        IN = str(input('\n Resposta: '))
          
        if(IN == '1' or IN == '2' or IN == '3' or IN == '4'):
            if(int(g)== int(IN)):
                if( money < 5000.0):
                    money = money + 1000
                
                elif(money == 5000.0):
                    money = money + 5000
                                    
                elif(money < 50000.0):
                    money = money + 10000
                    
                elif(money < 500000.0):
                    money = money + 100000
                
                else:
                    money = money + 500000
                    
                certo(lidos, np, nc, money)
                
            else:
                errou(money)
                
            break
        
        elif(IN == 'd'):
            parou(money)
            break
        
        elif(IN == 'p' and np > 0):
            np = np-1
            proxima_pergunta(lidos, money)
            break
            
        elif(IN == 'c' and nc > 0):
            nc = nc-1
            c = random.randint(1, 4)
            print('carta: ', c)
def parou(money):
    print('\n PAROU: Você Leva R$', money)
    
def venceu():
    sucess = '                                           Parabéns: R$'
    print('\n PARABÉNS VOCÊ VENCEU!!!')
    print(sucess)
    
def errou(money):
    fail = '                                              Saldo: R$'
    
    print('\n ERROOOOOUU!!!')
    if (money < 500000):
        if(money != 0):
            money = money/2
    else:
        money = 0
        
    print('NÃO LEVA NADA!!!')
    print(fail, money)

def certo(lidos, np, nc, money):
    print('\n Certa Resposta.')
    proxima_pergunta(lidos, np, nc, money)
    
def manipula_arquivo(lidos, p, np, nc, money):
    arquivo = open('/sdcard/qpython/show/perguntas.txt', 'r')
    pergunta = arquivo.readlines()
    arquivo.close()

    r1 = open('/sdcard/qpython/show/respostas1.txt', 'r')
    p1 = r1.readlines()
    r1.close()
   
    r2 = open('/sdcard/qpython/show/respostas2.txt', 'r')
    p2 = r2.readlines()
    r2.close()

    r3 = open('/sdcard/qpython/show/respostas3.txt', 'r')
    p3 = r3.readlines()
    r3.close()

    r4 = open('/sdcard/qpython/show/respostas4.txt', 'r')
    p4 = r4.readlines()
    r4.close()

    gab = open('/sdcard/qpython/show/gabarito.txt', 'r')
    g = gab.readlines()
    gab.close()
    
    print_layout(lidos, pergunta[p], p1[p], p2[p], p3[p], p4[p], g[p], np, nc, money)
    
    return lidos

def check_list(lidos, R, np, nc, money):
    
    for item in lidos:
        if (item == R):
            proxima_pergunta(lidos, np, nc, money)
            
            break
    else:
        lidos.append(R)
        manipula_arquivo(lidos, R, np, nc, money)
        
    return R, lidos

def proxima_pergunta(lidos, np, nc, money):
    r = random.randint(0, 18)
    check_list(lidos, r, np, nc, money)
    
    return r, lidos

proxima_pergunta(lista, np, nc, money)
