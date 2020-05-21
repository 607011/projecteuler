# -*- coding: utf-8 -*-
# coding=utf-8
# Copyright (c) 2010 Oliver Lau <oliver@ersatzworld.net>
# $Id: Stopwatch.py d3da6811729d 2011/01/07 07:07:18 Oliver Lau <oliver@ersatzworld.net> $


from time import clock


class Stopwatch:
    t0 = None
    elapsed = None
    
    def __init__(self):
        self.start()
        
    def start(self):
        self.t0 = clock()

    def stop(self):
        self.elapsed = clock() - self.t0

    def ms(self):
        return 1000 * (self.elapsed)
