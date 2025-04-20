import math
import sympy
import random
import time
import sympy
import matplotlib.pyplot as plt

def sieve_primes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0:2] = [False, False]
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [p for p, prime in enumerate(is_prime) if prime]

def is_prime_bach1993(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    logn = math.log(n)
    loglogn = math.log(logn)
    bound = int((1 / math.log(2)) * logn * loglogn) + 1
    bases = sieve_primes(bound)

    for a in bases:
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s):
            y = pow(x, 2, n)
            if y == 1 and x != 1 and x != n - 1:
                # x是1的非平凡模n平方根，提前终止
                return False
            x = y
        if y != 1:
            # 费马测试失败，提前终止
            return False
    return True

def timef(n, f):
    tik = time.time()
    print(f.__name__, f(n))
    dt = time.time() - tik
    return dt

def expr():
    mersenne_ks = [2,3,5,7,13,17,19,31,61,89,107,127,521,607,1279,2203,2281,3217,4253,4423,9689,9941,11213,19937,21701,23209,44497,86243,110503,132049,216091,756839,859433,1257787,1398269,2976221,3021377,6972593,13466917,20996011,24036583,25964951,30402457,32582657,37156667,42643801,43112609,57885161,74207281,77232917,82589933,136279841]
    ns = [2**k-1 for k in mersenne_ks[13:18]]
    #ns = [2**k-1 for k in mersenne_ks[17:18]]
    riemann_ts = [timef(n, is_prime_bach1993) for n in ns]
    sympy_ts = [timef(n, sympy.isprime) for n in ns]
    log_riemann_ts = [math.log(t, 2) for t in riemann_ts]
    log_sympy_ts = [math.log(t, 2) for t in sympy_ts]
    log_ns = [math.log(n, 2) for n in ns]
    plt.plot(log_ns, log_riemann_ts, label='log time of riemann miller')
    plt.plot(log_ns, log_sympy_ts, label='log time of sympy')
    plt.xlabel('log n')
    plt.ylabel('log T')
    plt.legend()
    plt.savefig('time_isprime.png')

expr()
