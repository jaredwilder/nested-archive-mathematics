#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Recomputes the results this repository states in its own voice.

    python verify.py

Standard library only. Exit 0 means everything reproduced.
"""
from __future__ import annotations

import math
import sys
from itertools import combinations, permutations
from math import comb, factorial, isqrt

FAILURES = []


def check(label, got, want):
    ok = got == want
    print("  %-56s %s" % (label, "PASS" if ok else "FAIL got=%r want=%r" % (got, want)))
    if not ok:
        FAILURES.append(label)


def test_integral_four():
    print("Four points, six integral distances, no 3 collinear, not concyclic")
    P = [(-12, 0), (12, 0), (0, 5), (0, -9)]
    ds = []
    for a, b in combinations(P, 2):
        q = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
        r = isqrt(q)
        check("  d((%d,%d),(%d,%d)) is an integer" % (a + b), r * r, q)
        ds.append(r)
    check("distance multiset", sorted(ds), [13, 13, 14, 15, 15, 24])

    def cross(a, b, c):
        return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

    check("no three collinear",
          any(cross(*t) == 0 for t in combinations(P, 3)), False)

    M = [[x, y, x * x + y * y, 1] for x, y in P]
    det = 0
    for perm in permutations(range(4)):
        sgn, pl = 1, list(perm)
        for i in range(4):
            for j in range(i + 1, 4):
                if pl[i] > pl[j]:
                    sgn = -sgn
        pr = 1
        for i in range(4):
            pr *= M[i][perm[i]]
        det += sgn * pr
    check("not concyclic (circle determinant nonzero)", det != 0, True)


def test_ngon():
    print("A regular n-gon has exactly floor(n/2) distinct distances")
    bad = []
    for n in range(3, 65):
        vals = {round(4 * math.sin(math.pi * k / n) ** 2, 9) for k in range(1, n)}
        if len(vals) != n // 2:
            bad.append(n)
    check("mismatches for n = 3..64", bad, [])


def powerful(n):
    if n < 1:
        return False
    m, d = n, 2
    while d * d <= m:
        if m % d == 0:
            e = 0
            while m % d == 0:
                m //= d
                e += 1
            if e < 2:
                return False
        d += 1
    return m == 1


def test_powerful():
    print("Powerful values in three families")
    check("n! + 1 powerful, 2 <= n <= 7",
          [n for n in range(2, 8) if powerful(factorial(n) + 1)], [4, 5, 7])
    check("  the values", [factorial(n) + 1 for n in (4, 5, 7)], [25, 121, 5041])
    check("2^n + 1 powerful, 2 <= n <= 11",
          [n for n in range(2, 12) if powerful(2 ** n + 1)], [3])
    check("2^n - 1 powerful, 2 <= n <= 11",
          [n for n in range(2, 12) if powerful(2 ** n - 1)], [])


def test_divisibility():
    print("n(n-1)(n-2) divides C(2n,n)")
    for n in (2480, 3478):
        check("n = %d" % n, comb(2 * n, n) % (n * (n - 1) * (n - 2)), 0)


def totient(n):
    r, m, d = n, n, 2
    while d * d <= m:
        if m % d == 0:
            while m % d == 0:
                m //= d
            r -= r // d
        d += 1
    if m > 1:
        r -= r // m
    return r


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def test_totient_family():
    print("m_n (least m with n | phi(m)) versus p_n (least prime = 1 mod n)")

    def m_of(n):
        m = 1
        while totient(m) % n:
            m += 1
        return m

    def p_of(n):
        p = 2
        while not (is_prime(p) and (p - 1) % n == 0):
            p += 1
        return p

    check("n in 1..24 with m_n < p_n",
          [n for n in range(1, 25) if m_of(n) < p_of(n)], [1, 8, 20, 24])
    check("  (m_8, p_8)", (m_of(8), p_of(8)), (15, 17))
    check("  (m_20, p_20)", (m_of(20), p_of(20)), (25, 41))
    check("  (m_24, p_24)", (m_of(24), p_of(24)), (35, 73))
    check("m_{p-1} = p_{p-1} = p for every odd prime p <= 29",
          all(m_of(p - 1) == p and p_of(p - 1) == p
              for p in (3, 5, 7, 11, 13, 17, 19, 23, 29)), True)


def test_mian_chowla():
    print("Mian-Chowla A005282: the estate held 155 and 134, an audit chose 134")
    A = [1]
    while len(A) < 14:
        c = A[-1] + 1
        while True:
            T = A + [c]
            sums = [x + y for x, y in combinations(T, 2)]
            if len(sums) == len(set(sums)):
                A.append(c)
                break
            c += 1
    check("the first 14 terms", A,
          [1, 2, 3, 5, 8, 13, 21, 30, 39, 53, 74, 95, 128, 152])
    check("a(13)", A[12], 128)
    print("     => 155 is wrong, 134 is wrong, and the audit's correction was wrong")


def main():
    for fn in (test_integral_four, test_ngon, test_powerful, test_divisibility,
               test_totient_family, test_mian_chowla):
        fn()
        print()
    if FAILURES:
        print("FAILED: %d check(s)" % len(FAILURES))
        for f in FAILURES:
            print("   " + f)
        return 1
    print("ALL CHECKS PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
