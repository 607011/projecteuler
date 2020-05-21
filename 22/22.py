#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://projecteuler.net/index.php?section=problems&id=22
# Copyright (c) 2010 Oliver Lau <oliver@ersatzworld.net>


def alpha_value(name):
    sum = 0
    offset = ord('A') - 1
    for i in xrange(len(name)):
        sum += ord(name[i]) - offset
    return sum

def main():
    names = [ ]
    file = open("names.txt")
    for line in file:
        names += sorted(map(lambda name: name.rstrip('"').lstrip('"'), line.split(",")))
    sum = 0
    for i in xrange(len(names)):
        name_score = (i+1) * alpha_value(names[i])
        sum += name_score
    print sum


if __name__ == '__main__':
    main()
