#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://projecteuler.net/index.php?section=problems&id=6
# Copyright (c) 2010 Oliver Lau <oliver@ersatzworld.net>

def main():
    sumsq = 0
    sum = 0
    for i in xrange(1, 101):
        sumsq += i * i
        sum += i
    sum = sum * sum
    print "%d - %d = %d" % (sum, sumsq, sum-sumsq)


if __name__ == '__main__':
    main()
