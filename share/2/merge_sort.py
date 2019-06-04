# -*- coding:utf-8 -*-
import random


def merge_sort(input):
    dived(input, 0, len(input) - 1)


def dived(input, l, r):
    if (l >= r):
        return
    mid = (l + r) >> 1
    dived(input, l, mid)
    dived(input, mid + 1, r)
    merge(input, l, mid, r)


def merge(input, l, mid, r):
    i, j, t = l, mid + 1, 0
    temp = [None] * len(input)
    while (i <= mid and j <= r):
        if (input[i] <= input[j]):
            temp[t] = input[i]
            t = t + 1
            i = i + 1
        else:
            temp[t] = input[j]
            t = t + 1
            j = j + 1

    if (i <= mid):
        start = i
        end = mid
    else:
        start = j
        end = r
    while (start <= end):
        temp[t] = input[start]
        t = t + 1
        start = start + 1
    for i in range(len(input)):
        if temp[i] is None:
            break
        input[l + i] = temp[i]


def main():
    s = [x for x in range(10)]
    random.shuffle(s)
    print(s)
    merge_sort(s)
    print(s)
    assert s == sorted(s)


if __name__ == '__main__':
    main()
