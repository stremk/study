#https://acmp.ru/index.asp?main=task&id_task=596

def is_availiable(operator, user):
    return ((operator[1][0] - user[0]) ** 2 + (operator[1][1] - user[1]) ** 2) <= (operator[1][2] ** 2)


with open('input.txt') as f:
    n = int(f.readline())
    operators = list()
    for i in range(n):
        operators.append(tuple((f.readline()[:-1], list(map(int, f.readline().split())))))

    user = list(map(int, f.readline().split()))

    operators_avaliable = dict()
    operators_unavaliable = dict()
    for operator in operators:
        if is_availiable(operator, user):
            if operator[0] in operators_avaliable:
                operators_avaliable[operator[0]] += 1
            else:
                operators_avaliable.update({operator[0]: 1})
        else:
            if operator[0] not in operators_avaliable:
                operators_unavaliable.update({operator[0]: 0})

    operators = operators_avaliable
    operators.update(operators_unavaliable)
    operators.update(operators_avaliable)

with open('output.txt', 'w') as f:
    f.writelines([str(len(operators)) + '\n'] + ['{} {}\n'.format(operatorname, str(avaliability))
                                                 for operatorname, avaliability in operators.items()])
