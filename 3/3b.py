#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://projecteuler.net/index.php?section=problems&id=3
# Copyright (c) 2010 Oliver Lau <oliver@ersatzworld.net>

import sys

def main():
    v = 600851475143
    primes = [ ]

    def is_prime(n):
        for p in primes:
            if n % p == 0:
                return False
        return True

    def make_primes(n):
        for i in xrange(2, n):
            if is_prime(i):
                primes.append(i)

    def factors(n):
        return [ p for p in primes if n % p == 0 ]

    make_primes(100000)
    print factors(v)


if __name__ == '__main__':
    main()
