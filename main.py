import random
import os
from matplotlib import pyplot as plt

def randomSolve():
    answer = {}
    count = [0, 0, 0, 0, 0, 0]

    random.seed(os.urandom(125))

    tries = 100000
    problems = 25

    for i in range(tries):
        temp = {}

        for j in range(problems):
            temp[j] = random.randint(1, 5)

        answer[i] = temp

    random.seed(os.urandom(125))

    for i in answer:
        for j in answer[i]:
            if answer[i][j] == random.randint(1, 5):
                count[0] += 1

        for j in answer[i]:
            if answer[i][j] == 1:
                count[1] += 1

        for j in answer[i]:
            if answer[i][j] == 2:
                count[2] += 1

        for j in answer[i]:
            if answer[i][j] == 3:
                count[3] += 1

        for j in answer[i]:
            if answer[i][j] == 4:
                count[4] += 1

        for j in answer[i]:
            if answer[i][j] == 5:
                count[5] += 1

    total = 0

    for k, v in enumerate(count):
        if k == 0:
            continue
        total += v

    if not total == tries * problems:
        exit(1)

    for k, v in enumerate(count):
        count[k] = v / (tries * problems) * 100


    return count
'''
plt.subplot(221)
plt.plot(randomSolve())
plt.subplot(222)
plt.plot(randomSolve())
plt.subplot(223)
plt.plot(randomSolve())
plt.subplot(224)
plt.plot(randomSolve())
plt.show()
'''
