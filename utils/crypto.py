#!/usr/bin/env python3
# Some code from https://shainer.github.io/crypto/math/2017/10/22/chinese-remainder-theorem.html, with minor changes

def gcd(a, b):
    '''
    Greatest common divisor, using euclidian algorithm (not extended)
    '''
    r_old = a # reminder before the previous one
    r_prev = b # previous reminder
    r = r_old % r_prev # current reminder
    while (r != 0):
        r_old = r_prev
        r_prev = r
        r = r_old % r_prev
    return r_prev

def extended_euclid(x, y):
    '''
    Extended euclid:
    x0 * x + y0 * y = gcd(x,y)
    x0 and y0  are the solution to the Bézout's identity.
    '''
    x0, x1, y0, y1 = 1, 0, 0, 1

    while y > 0:
        q, x, y = x // y, y, x % y # same as gcd over
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1 # look at wikipdia

    return x, x0, y0  # gcd and the two coefficients

def chinese_remainder_gauss(n, a):
    '''
    n = factor, what to do modulus with
    a = rest

    x % n = a for all n and a or on matematic terms:

    x congruent a[0] (mod n[0])
    x congruent a[1] (mod n[1])
    ....
    '''
    result = 0
    N = 1
    for i in n:
        N *= i
    for i in range(len(n)):
        ai = a[i]
        ni = n[i]
        bi = N // ni
        result += ai * bi * invmod(bi, ni)
    return result % N

def invmod(a, m):
    '''
    inverse module:
    finds x so that (a * x) % m = 1
    '''
    g, x, y = extended_euclid(a, m)
    if g != 1:
        raise ValueError('modular inverse does not exist')
    else:
        return x % m
