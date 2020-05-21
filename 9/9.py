#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://projecteuler.net/index.php?section=problems&id=9
# Copyright (c) 2010 Oliver Lau <oliver@ersatzworld.net>

import sys

def main():
    N = 1000
    found = False
    for c in xrange(N):
        c2 = c * c
        for b in xrange(c):
            b2 = b * b
            for a in xrange(b):
                if a*a + b2 == c2:
                    found = (a + b + c == N)
                    break
            if found: break
        if found: break
    print a * b * c

if __name__ == '__main__':
    main()
