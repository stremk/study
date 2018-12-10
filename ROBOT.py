# https://acmp.ru/index.asp?main=task&id_task=235

with open('input.txt') as f:
    s = f.readline()

direction = 0
posx = [0]
posy = [0]
xyi = 0
N = 0
numstep = 0
fail = -1
for i in range(len(s)):
    if s[i] == 'S':
        if direction == 0:
           # print(i, len(posy), posy[len(posx) - 1])
            posx.append(posx[len(posx) - 1])
            posy.append(posy[len(posy) - 1] + 1)
           # print(posy)
           # print(posx[len(posx) - 1], '  ' , posy[len(posx) - 1])
         #   print(posy[len(posx) - 1])
            numstep += 1
        if direction == 1:
            posx.append(posx[len(posx) - 1] + 1)
            posy.append(posy[len(posy) - 1])
            numstep += 1
        if direction == 2:
            posx.append(posx[len(posx) - 1])
            posy.append(posy[len(posy) - 1] - 1)
            numstep += 1
        if direction == 3:
            posx.append(posx[len(posx) - 1] - 1)
            posy.append(posy[len(posy) - 1])
            numstep += 1
        for k in range(len(posx) - 1):
            if posx[len(posx) - 1] == posx[k] and posy[len(posx) - 1] == posy[k]:
                fail = 1
    if fail == 1:
        N = numstep
        break

    if s[i] == 'R':
        direction = (direction + 1) % 4
    if s[i] == 'L':
        if direction == 0:
            direction = 3
        else:
            direction -= 1
print(posx)
print(posy)
if fail == -1:
    print(-1)
else:
    print(N)



