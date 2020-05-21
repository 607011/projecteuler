#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://projecteuler.net/index.php?section=problems&id=18
# Copyright (c) 2010 Oliver Lau <oliver@ersatzworld.net>


def main():
    values = [ ]
    file = open("input.txt")
    for line in file:
        values.append(map(lambda x: int(x), line.split(" ")))

    sum = 0
    i, j = 0, 0
    for row in values:
        print "%2d, %2d [%d..%d]" % (row[i], row[j], i, j)
        if row[i] > row[j]:
            sum += row[i]
        else:
            sum += row[j]
            j += 1
        i = j - 1
    print "Summe =", sum
            

if __name__ == '__main__':
    main()