# -*- coding:utf-8 -*-
import random


def bucket_sort(input):
    max = input[0]
    min = input[0]
    for num in input:
        if num >= max:
            max = num
        if num <= min:
            min = num
    span = max - min
    internal = span / (len(input) - 1)
    temp = [[] for x in range(len(input))]
    for num in input:
        temp[int((num - min) / internal)].append(num)
    for i, t in enumerate(temp):
        temp[i] = sorted(t)
    result = []
    for t in temp:
        for tt in t:
            result.append(tt)
    return result


def main():
    input = [random.random() * random.randint(1, 2) * 10 for x in range(10)]
    # print(sorted(input))
    # print(bucket_sort(input))
    assert bucket_sort(input) == sorted(input)


if __name__ == '__main__':
    main()
