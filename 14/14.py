#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://projecteuler.net/index.php?section=problems&id=14
# Copyright (c) 2010 Oliver Lau <oliver@ersatzworld.net>


def main():

    def rollercoaster(n):
        l = 1
        while n != 1:
            if n % 2 == 0:
                n /= 2
            else:
                n = 3 * n + 1
            l += 1
        return l
           

    maxl = 0
    n = 0
    for i in xrange(1, 1000000):
        l = rollercoaster(i)
        if l > maxl:
            maxl, n = l, i
    print "%d hat eine Kettenlänge von %d" % (n, maxl)    
    

if __name__ == '__main__':
    main()