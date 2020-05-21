#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://projecteuler.net/index.php?section=problems&id=20
# Copyright (c) 2010 Oliver Lau <oliver@ersatzworld.net>


n = "93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000"

def main():
    sum = 0
    for i in xrange(len(n)):
        sum += int(n[i])
    print sum
    

if __name__ == '__main__':
    main()
