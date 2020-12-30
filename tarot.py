import numpy
import math
entities = 14

distributions = []
for first in range(entities + 1):
    next_range = entities - first
    for second in range(next_range + 1):
        if (second > first):
            continue
        next_range = entities - first - second
        for third in range(next_range + 1):
            if (third > second):
                continue
            next_range = entities - first - second - third
            for fourth in range(next_range + 1):
                if (fourth > third):
                    continue
                next_range = entities - first - second - third - fourth
                fifth = next_range
                if (fifth > fourth) or fifth == -1:
                    continue
                distributions.append([first, second, third, fourth, fifth])
print(distributions)

def weight(distribution):
    n_array = numpy.array(distribution)
    # print(numpy.unique(n_array, return_counts=True))
    print(distribution)
    unique, counts = numpy.unique(n_array, return_counts=True)
    total = 0
    cardinal = 1
    for item in counts:
        cardinal = cardinal * math.comb(5 - total, item)
        total += item
    print(cardinal)

print(len(distributions))
weight(distributions[10])
print(math.comb(18,14) / 120)