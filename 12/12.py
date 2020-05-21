#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://projecteuler.net/index.php?section=problems&id=12
# Copyright (c) 2010 Oliver Lau <oliver@ersatzworld.net>

from math import sqrt

def main():
    def make_primes(n):
        sieve = range(++n)
        sieve[:2] = [0, 0]
        for i in xrange(2, int(sqrt(n))+1):
            if sieve[i]:
                for j in xrange(i**2, n, i):
                    sieve[j] = 0
        return [ p for p in sieve if p ]

    primes = make_primes(1000000)

    def count_divisors(num):
        """
        http://mathforum.org/library/drmath/view/55843.html
        http://www.ehow.com/how_5169234_calculate-number-divisors.html
        """
        n = 1
        for prime in primes:
            if prime > num: break
            e = 1
            while num % prime == 0:
                num /= prime
                e += 1
            n *= e
        return n

    divisors = 1
    triangle = 0
    n = 1
    while divisors <= 500:
        triangle += n
        n += 1
        divisors = count_divisors(triangle)
    print "%d hat %d Teiler" % (triangle, divisors)

if __name__ == '__main__':
    main()