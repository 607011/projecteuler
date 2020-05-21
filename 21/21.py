#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://projecteuler.net/index.php?section=problems&id=21
# Copyright (c) 2010 Oliver Lau <oliver@ersatzworld.net>

from math import sqrt

def main(N):
    def make_primes(n):
        sieve = range(++n)
        sieve[:2] = [0, 0]
        for i in xrange(2, int(sqrt(n))+1):
            if sieve[i]:
                for j in xrange(i**2, n, i):
                    sieve[j] = 0
        return [ p for p in sieve if p ]

    primes = make_primes(N)

    def combinations(iterable, r):
        pool = tuple(iterable)
        n = len(pool)
        if r > n:
            return
        indices = range(r)
        yield tuple(pool[i] for i in indices)
        while True:
            for i in reversed(range(r)):
                if indices[i] != i + n - r:
                    break
            else:
                return
            indices[i] += 1
            for j in range(i+1, r):
                indices[j] = indices[j-1] + 1
            yield tuple(pool[i] for i in indices)

    def divisors(n):
        N = n
        f = [ 1 ]
        for p in primes:
            while n % p == 0:
                f.append(p)
                n /= p
        d = [ ]
        for i in xrange(1, len(f) + 1):
            d += map(lambda c: reduce(lambda a,b: a*b, list(c)), combinations(f, i))
        d = set(d)
        d.remove(N)
        return d

    div = range(N)
    div[0] = 0
    print "Generieren ... ",
    for i in xrange(1, N):
        print "%4d%%\b\b\b\b\b\b" % (100*i/N),
        div[i] = divisors(i)
    print

    def d(n):
        return sum(div[n])

    s = 0
    for a in xrange(1, N):
        for b in xrange(1, N):
            if a != b:
                if d(a) == b and d(b) == a:
                    print "%5d, %5d" % (a, b)
                    s += a
    print "Summe =", s

if __name__ == '__main__':
    main(10000)

"""
    220
+   284
+  1184
+  1210
+  2620
+  2924
+  5020
+  5564
+  6232
+  6368
-------
= 31626
"""