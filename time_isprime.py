import math
import sympy
import random
import time
import sympy
import matplotlib.pyplot as plt
from crypto import is_prime_bach1993

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
