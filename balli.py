# https://acmp.ru/index.asp?main=task&id_task=213

with open('input.txt') as f:
    nTest = int(f.readline())
    testCost = list(map(int, f.readline().split()))
    add = int(f.readline())
    numTrials = int(f.readline())
    trials = []
    a_balli = []
    balli = 0
    temp = 0
    for i in range(numTrials):
        trials.append(list(map(int, f.readline().split())))
print(nTest)
print(testCost)
print(trials)

if trials[0] == [1]*nTest:
    balli = sum(testCost) + add
else:
    for i in range(numTrials):
        for k in range(nTest):
            temp = temp + testCost[k]*trials[i][k]

        a_balli.append(temp)
        temp = 0
    balli = max(a_balli)
print(balli)

