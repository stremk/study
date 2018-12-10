# https://acmp.ru/index.asp?main=task&id_task=98

with open('input.txt') as f:
     n = int(f.readline())
     numbers = list(map(int, f.readline().split()))


vasya = 0
kolya = 0
for i in range(len(numbers)):
    if i % 2 == 0:
        if numbers[0] >= numbers[len(numbers) - 1]:
            vasya += numbers[0]
            numbers = numbers[1: len(numbers)]
        else:
            vasya += numbers[len(numbers) - 1]
            numbers = numbers[0: len(numbers) - 1]
    else:
        if numbers[0] >= numbers[len(numbers) - 1]:
            kolya += numbers[0]
            numbers = numbers[1: len(numbers)]
        else:
            kolya += numbers[len(numbers) - 1]
            numbers = numbers[0: len(numbers) - 1]

print(str(vasya) + ':' + str(kolya))
 