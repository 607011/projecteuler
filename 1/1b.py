#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://projecteuler.net/index.php?section=problems&id=1
# Copyright (c) 2010 Oliver Lau <oliver@ersatzworld.net>


from Stopwatch import Stopwatch

def main():
	w = Stopwatch()
	print(sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(1000000))))
	w.stop()
	print("Zeit: %d" % (w.ms()))

if __name__ == '__main__':
    main()
