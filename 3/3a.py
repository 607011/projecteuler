#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://projecteuler.net/index.php?section=problems&id=3
# Copyright (c) 2010 Oliver Lau <oliver@ersatzworld.net>

from math import sqrt

def primes(n):
    sieve = range(++n)
    sieve[:2] = [0, 0]
    for i in xrange(2, int(sqrt(n))+1):
        if sieve[i]:
            for j in xrange(i**2, n, i):
                sieve[j] = 0
    return [ p for p in sieve if p ]


def factors(n):
    return [ p for p in primes(n) if n % p == 0 ]


v = 600851475143
print max(factors(v))
