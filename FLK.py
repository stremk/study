def print_array(a):  # колхозно вывести доску
    for i in range(len(a)):
        print(chr(ord('A') + i), a[i])

def check_kletka(a, let, num):  # проверить допустимая ли клетка для атаки и бить (+1)
    if let < 0 or let > 7 or num < 0 or num > 7:
        return 1
    if a[let][num] >= 0:
        a[let][num] += 1
        return 0
    else:
        return 1

def tura(a, t_let, t_num):  # ставит на доску ладью
    k = 0
    direction = 1
    while k == 0:
        k = check_kletka(a, t_let + direction, t_num)
        direction += 1
    k = 0
    direction = 1
    while k == 0:
        k = check_kletka(a, t_let - direction, t_num)
        direction += 1
    direction = 1
    k = 0
    while k == 0:
        k = check_kletka(a, t_let, t_num + direction)
        direction += 1
    direction = 1
    k = 0
    while k == 0:
        k = check_kletka(a, t_let, t_num - direction)
        direction += 1

def slon(a, t_let, t_num): # ставит на доску слона
    k = 0
    direction = 1
    while k == 0:
        k = check_kletka(a, t_let + direction, t_num + direction)
        direction += 1
    k = 0
    direction = 1
    while k == 0:
        k = check_kletka(a, t_let - direction, t_num - direction)
        direction += 1
    direction = 1
    k = 0
    while k == 0:
        k = check_kletka(a, t_let - direction, t_num + direction)
        direction += 1
    direction = 1
    k = 0
    while k == 0:
        k = check_kletka(a, t_let + direction, t_num - direction)
        direction += 1

def ferz(a, f_let, f_num):  # ставит на доску ферзя = ладью + слона
    tura(a, f_let, f_num)
    slon(a, f_let, f_num)

def kon(a, k_let, k_num):  # ставим на доску коня
    check_kletka(a, k_let + 1, k_num + 2)
    check_kletka(a, k_let + 2, k_num + 1)
    check_kletka(a, k_let - 1, k_num + 2)
    check_kletka(a, k_let - 2, k_num + 1)
    check_kletka(a, k_let + 1, k_num - 2)
    check_kletka(a, k_let + 2, k_num - 1)
    check_kletka(a, k_let - 1, k_num - 2)
    check_kletka(a, k_let - 2, k_num - 1)

def check_howmuch_exactly(a, k=3):  # проверяет сколько клеток бьется k фигурами
    num = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] == k:
                num += 1
    return num

def check_howmuch(a): # проверяет, сколько клеток бьется в принципе
    num = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] > 0:
                num += 1
    return num

def translate(a):  # переводит доску к виду +/- и фигуры
    for i in range(n):
        for j in range(n):
            if a[i][j] > 0:
                a[i][j] = '+'
            elif a[i][j] == -1:
                a[i][j] = 'F'
            elif a[i][j] == -2:
                a[i][j] = 'T'
            elif a[i][j] == -3:
                a[i][j] = 'K'
            else:
                a[i][j] = '-'
    return a


with open('input.txt') as f:
    n = int(f.readline())
    a = f.readline().split()
    f_let = ord(a[0][0]) - ord('A')
    f_num = int(a[0][1]) - 1
    t_let = ord(a[1][0]) - ord('A')
    t_num = int(a[1][1]) - 1
    k_let = ord(a[2][0]) - ord('A')
    k_num = int(a[2][1]) - 1

a = [[0]*n]

for i in range(n - 1):
    a.append([0]*n)
a[f_let][f_num] = -1
a[t_let][t_num] = -2
a[k_let][k_num] = -3

kon(a, k_let, k_num)
tura(a, t_let, t_num)
ferz(a, f_let, f_num)

print_array(a)

print(check_howmuch(a))

print_array(translate(a))
