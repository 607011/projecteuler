#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://projecteuler.net/index.php?section=problems&id=2
# Copyright (c) 2010 Oliver Lau <oliver@ersatzworld.net>

def main():
    prev, curr = 1, 2
    s = 2
    while True:
        prev, curr = curr, prev + curr
        if curr > 4000000:
            break;
        if curr % 2 == 0:
            s += curr
    print s


if __name__ == '__main__':
    main()
