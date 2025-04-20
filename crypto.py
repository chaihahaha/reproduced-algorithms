import math
import sympy
import random

def fast_mod_exp(b, exp, m):
    res = 1
    while exp > 1:
        if exp & 1:
            res = (res * b) % m
        b = b ** 2 % m
        exp >>= 1
    return (b * res) % m

def is_prime_miller_riemann(n):
    if n % 2 == 0:
        return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in range(2, min(n - 2, int(2 * math.log(n)**2)) + 1):
        x = pow(a, d, n)
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

def isprime_rand_test():
    # 随机测试算法正确性
    max_n = 100000000
    odd = [2*i + 1 for i in range(1,max_n)]
    even = [2*i for i in range(1,max_n)]
    for i in range(10):
        n = random.choice(odd)
        assert sympy.isprime(n) == is_prime_bach1993(n)
    
    n = random.choice(even)
    assert sympy.isprime(n) == is_prime_bach1993(n)

def rand_bits(irrational, start, end):
    bits = []
    for i in range(end):
        irrational *= 2
        if i >= start:
            bits.append(int(irrational)%2)
    return bits
  
def rand_bits_test():
    irrational = 2**(sympy.sympify(1)/5)
    start = 200   # 从第100位开始
    end = 264     # 到164位结束
    bits = rand_bits(irrational, start, end)
    print(bits)
    print(sum(bits)/len(bits))

if __name__=='__main__':
    isprime_rand_test()
    rand_bits_test()
