# -*- coding:utf-8 -*-
import random


def quick_sort(input, l, r):
    if (l >= r):
        return
    i, j, x = l, r, input[l]
    while (i < j):
        # 从右向左找第一个小于基元素的位置
        while (i < j and input[j] >= x):
            j = j - 1
        if (i < j):
            input[i] = input[j]
            i = i + 1
        # 从左向右找第一个大于等于基元素的数
        while (i < j and input[i] < x):
            i = i + 1
        if (i < j):
            input[j] = input[i]
            j = j - 1
    input[i] = x
    quick_sort(input, l, i - 1)
    quick_sort(input, i + 1, r)


def main():
    s = [x for x in range(10)]
    random.shuffle(s)
    quick_sort(s, 0, len(s) - 1)
    assert s == sorted(s)


if __name__ == "__main__":
    main()
