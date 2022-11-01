# fact e fibc são funções recursivas que fornecem
# fatorial e posição na seqência de Fibonacci de
# um número inteiro

def fact(x):
    if (x == 0 or x == 1):
        return 1
    if (x >= 2):
        return x*fact(x-1)

# Consideram-se 0, 1 os termos iniciais de
# posições 1, 2 na sequência de Fibonacci.

def fibc(x):
    if (x == 1):
        return 0
    if (x == 2):
        return 1
    if (x >= 3):
        return fibc(x-1) + fibc(x-2)

# Leitura do arquivo input.dat, cujo conteúdo é
# repassado à string input

input = ''

f = open("input.dat", "r")
for x in f:
    input += x
f.close()

# O conteúdo de input é transformado em lista file, dividido com
# split por caracteres espaço. Depois a lista é separada por \n
# e repassada à lista arq.

file = input.split('\n')
x = len(file)
arq = []

i = 0
while (i < x):
    y = file[i].split(' ')
    arq += y
    i += 1

i = 0
n = len(arq)
n -= 1
output = ''

out = [0]*n

# A lista arq recebe fibonacci de posições pares e fatorial
# de posições ímpares de arq.

while(i < n):
    out[i]   = fibc(int(arq[i]))
    out[i+1] = fact(int(arq[i+1]))
    i += 2

# A string output recebe os valores de arq é formatada como
# arquivo de saída output.dat.

i = 0
j = 1
while (i < n):
    output += 'Linha ' + str(j) + ':Fib=' + str(out[i]) + '\tFact=' + str(out[i+1]) + '\n'
    j += 1
    i += 2

g = open("output.dat", "w")
g.write(output)
g.close()
