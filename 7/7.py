#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://projecteuler.net/index.php?section=problems&id=7
# Copyright (c) 2010 Oliver Lau <oliver@ersatzworld.net>

import sys

def main():
    primes = [ ];

    def is_prime(n):
        for p in primes:
            if n % p == 0:
                return False
        return True

    def make_primes(N):
        i = 2
        n = 0
        while n < N:
            if is_prime(i):
                primes.append(i)
                n = n + 1
            i = i + 1

    make_primes(10001)
    print primes[-1]


if __name__ == '__main__':
    main()
