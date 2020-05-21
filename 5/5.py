#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://projecteuler.net/index.php?section=problems&id=5
# Copyright (c) 2010 Oliver Lau <oliver@ersatzworld.net>

def main():
    x = 2
    divisible = True
    while divisible:
        for i in [ 11, 13, 14, 15, 16, 17, 18, 19, 20 ]:
            divisible = divisible and (x % i == 0)
            if not divisible: break
        if divisible:
            print x
            break
        x = x + 1
        divisible = True


if __name__ == '__main__':
    main()
