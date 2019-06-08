# -*- coding:utf-8 -*-
import heapq
import random


def main():
    input = [x for x in range(10)]
    random.shuffle(input)
    print(input)
    temp = input[:5]
    heapq.heapify(temp)
    for i in input[5:]:
        heapq.heappush(temp, i)
    print(temp)
    assert (0 in temp)
    assert (1 in temp)
    assert (2 in temp)
    assert (3 in temp)
    assert (4 in temp)


if __name__ == '__main__':
    main()
