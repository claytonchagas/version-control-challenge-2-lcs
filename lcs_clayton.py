import sys
import diff_cores_saida_terminal

#implementacao lcs com programacao dinamica

#calculo da matriz de comprimento de lcs
def comprimento_lcs(x, y):
    m = [[0 for a in range(len(y) + 1)] for b in range(len(x) + 1)]

    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] == y[j]:
                m[i][j] = 1 + m[i-1][j-1]
            else:
                m[i][j] = max(m[i][j-1], m[i-1][j])
    return m

#percorre a matriz de comprimento de lcs
#para imprimir a diferenca das linhas dos arquivos
def print_diff(m, x, y, i, j):
    if i < 0 and j < 0:
        return ""
    elif i < 0:
        print_diff(m, x, y, i, j-1)
        print(diff_cores_saida_terminal.VERDE + y[j], end='')
    elif j < 0:
        print_diff(m, x, y, i-1, j)
        print(diff_cores_saida_terminal.VERMELHA + riscar(x[i]), end='')
    elif x[i] == y[j]:
        print_diff(m, x, y, i-1, j-1)
        print(diff_cores_saida_terminal.BRANCA + x[i], end='')
    elif m[i][j-1] >= m[i-1][j]:
        print_diff(m, x, y, i, j-1)
        print(diff_cores_saida_terminal.VERDE + y[j], end='')
    elif m[i][j-1] < m[i-1][j]:
        print_diff(m, x, y, i-1, j)
        print(diff_cores_saida_terminal.VERMELHA + riscar(x[i]), end='')

def diff_lcs(x, y):
    m = comprimento_lcs(x, y)
    return print_diff(m, x, y, len(x)-1, len(y)-1)

def erro():
    print("Utilize a chamada e os parametros corretamente:")
    print("$ python3 lcs_clayton.py arquivo1 arquivo2")

def riscar(text):
    return (''.join([u'\u0336{}'.format(m) for m in text]))

def main():
    if len(sys.argv) != 3:
        erro()
        sys.exit(1)

    with open(sys.argv[1], 'r') as a1, open(sys.argv[2], 'r') as a2:
        diff_lcs(a1.readlines(), a2.readlines())

if __name__ == '__main__':
    main()
