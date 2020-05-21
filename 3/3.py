#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://projecteuler.net/index.php?section=problems&id=3
# Copyright (c) 2010 Oliver Lau <oliver@ersatzworld.net>

from __future__ import generators

def ints_from(i):
    while True:
        yield i
        i = i + 1


def skip_multiples(n, ints):
    for i in ints:
        if i % n: yield i
        

def sieve(ints):
    while True:
        prime = ints.next()
        yield prime
        ints = skip_multiples(prime, ints)


v = 600851475143
p = sieve(ints_from(2))
f = p.next()
while f <= v:
    if v % f == 0:
        print f,
        v = v / f
    f = p.next()
