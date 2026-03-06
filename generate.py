#!/usr/bin/env python3
"""Regenerate make24-puzzles.json from scratch.

Only needed if the solver algorithm changes. Run from the repo root:
    python generate.py
"""
import json
from fractions import Fraction
from itertools import permutations, product


def _apply(a_val, a_str, b_val, b_str, op):
    if op == '/':
        if b_val == 0:
            return None, None
        val = a_val / b_val
    elif op == '+':
        val = a_val + b_val
    elif op == '-':
        val = a_val - b_val
    else:
        val = a_val * b_val
    return val, f"({a_str} {op} {b_str})"


def _solve(numbers):
    target = Fraction(24)
    ops = ['+', '-', '*', '/']
    for perm in permutations(numbers):
        a, b, c, d = [Fraction(n) for n in perm]
        sa, sb, sc, sd = [str(n) for n in perm]
        for o1, o2, o3 in product(ops, repeat=3):
            r1, e1 = _apply(a, sa, b, sb, o1)
            if r1 is not None:
                r2, e2 = _apply(r1, e1, c, sc, o2)
                if r2 is not None:
                    r3, e3 = _apply(r2, e2, d, sd, o3)
                    if r3 == target:
                        return e3
            r1, e1 = _apply(b, sb, c, sc, o2)
            if r1 is not None:
                r2, e2 = _apply(a, sa, r1, e1, o1)
                if r2 is not None:
                    r3, e3 = _apply(r2, e2, d, sd, o3)
                    if r3 == target:
                        return e3
            r1, e1 = _apply(a, sa, b, sb, o1)
            r2, e2 = _apply(c, sc, d, sd, o3)
            if r1 is not None and r2 is not None:
                r3, e3 = _apply(r1, e1, r2, e2, o2)
                if r3 == target:
                    return e3
            r1, e1 = _apply(b, sb, c, sc, o2)
            if r1 is not None:
                r2, e2 = _apply(r1, e1, d, sd, o3)
                if r2 is not None:
                    r3, e3 = _apply(a, sa, r2, e2, o1)
                    if r3 == target:
                        return e3
            r1, e1 = _apply(c, sc, d, sd, o3)
            if r1 is not None:
                r2, e2 = _apply(b, sb, r1, e1, o2)
                if r2 is not None:
                    r3, e3 = _apply(a, sa, r2, e2, o1)
                    if r3 == target:
                        return e3
    return None


def build_pool():
    pool = []
    for a in range(1, 10):
        for b in range(a, 10):
            for c in range(b, 10):
                for d in range(c, 10):
                    solution = _solve([a, b, c, d])
                    if solution is not None:
                        pool.append([[a, b, c, d], solution])
    return pool


if __name__ == "__main__":
    pool = build_pool()
    with open("make24-puzzles.json", "w") as f:
        json.dump(pool, f, indent=2)
    print(f"Generated {len(pool)} puzzles → make24-puzzles.json")
