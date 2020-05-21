#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://projecteuler.net/index.php?section=problems&id=4
# Copyright (c) 2010 Oliver Lau <oliver@ersatzworld.net>

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


def main():
    palindromes = []
    for i in xrange(1, 1000):
        for j in xrange(1, 1000):
            p = i * j
            if is_palindrome(p):
                palindromes.append([i, j, p])
    #for p in sorted(palindromes, cmp=lambda x, y: x[2] - y[2]):
    #    print "%d x %d = %d" % (p[0], p[1], p[2])
    print max(palindromes, key=lambda x: x[2])


if __name__ == '__main__':
    main()
