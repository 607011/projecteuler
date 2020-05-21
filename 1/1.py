#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://projecteuler.net/index.php?section=problems&id=1
# Copyright (c) 2010 Oliver Lau <oliver@ersatzworld.net>


from Stopwatch import Stopwatch

def main():
    w = Stopwatch()
    s = 0
    for i in range(3, 1000000):
        if i % 3 == 0 or i % 5 == 0:
            s += i
    print(s)
    w.stop()
    print("Zeit: %d" % (w.ms()))

if __name__ == '__main__':
    main()
