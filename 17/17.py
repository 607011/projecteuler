#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://projecteuler.net/index.php?section=problems&id=16
# Copyright (c) 2010 Oliver Lau <oliver@ersatzworld.net>


digits = [ "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
           "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
           "seventeen", "eighteen", "nineteen", "twenty" ]

tens = [ "", "ten", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy",
         "eighty", "ninety", "hundred" ]


def speak(i):
    i = int(i)
    if i == 0:
        return ""
    elif i <= 20:
        return digits[i]
    elif i < 100:
        return tens[i/10] + speak(i%10)
    elif i < 1000:
        hundreds = speak(i/100) + "hundred"
        if (i%100 != 0):
            return hundreds + "and" + speak(i%100)
        else:
            return hundreds
    else:
        pass

def main():
    sum = 0
    for i in xrange(1, 1000):
        n = speak(i)
        print "%d: >%s< (%d)" % (i, n, len(n))
        sum += len(n)
    sum += len("onethousand")
    print sum
    

if __name__ == '__main__':
    main()
