# save as sol.py and place validation_input.txt in same folder
MOD = 10**9 + 7
from math import gcd, isqrt
from functools import lru_cache
import random

# Deterministic Miller-Rabin for 64-bit range
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    small_primes = [2,3,5,7,11,13,17,19,23,29]
    for p in small_primes:
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    bases = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]
    for a in bases:
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        composite = True
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                composite = False
                break
        if composite:
            return False
    return True

def pollards_rho(n: int) -> int:
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    # make deterministic-ish
    while True:
        x = random.randrange(2, n - 1)
        y = x
        c = random.randrange(1, n - 1)
        d = 1
        while d == 1:
            x = (x * x + c) % n
            y = (y * y + c) % n
            y = (y * y + c) % n
            d = gcd(abs(x - y), n)
            if d == n:
                break
        if d > 1 and d < n:
            return d

def factorize_pollard(n: int, out: dict):
    if n == 1:
        return
    if is_prime(n):
        out[n] = out.get(n, 0) + 1
        return
    d = pollards_rho(n)
    factorize_pollard(d, out)
    factorize_pollard(n // d, out)

def factorize(n: int) -> dict:
    out = {}
    if n <= 1:
        return out
    factorize_pollard(n, out)
    return out

def gen_divisors_from_factors(factors: dict):
    items = list(factors.items())
    res = [1]
    for p, e in items:
        cur = []
        powp = 1
        for i in range(e + 1):
            for r in res:
                cur.append(r * powp)
            powp *= p
        res = cur
    return res

def vp_factorial(n: int, p: int) -> int:
    cnt = 0
    div = p
    while div <= n:
        cnt += n // div
        if div > n // p:
            break
        div *= p
    return cnt

# caches for small factorials and inverse factorials
fact_cache = {0: 1}
inv_fact_cache = {}

def ensure_fact(k):
    if k in fact_cache:
        return
    cur = max(fact_cache.keys())
    val = fact_cache[cur]
    for i in range(cur + 1, k + 1):
        val = (val * i) % MOD
        fact_cache[i] = val
    inv_fact_cache[k] = pow(fact_cache[k], MOD - 2, MOD)
    for i in range(k, cur, -1):
        inv_fact_cache[i - 1] = (inv_fact_cache[i] * i) % MOD

@lru_cache(None)
def comb_large_n_small_k(n: int, k: int) -> int:
    if k < 0:
        return 0
    if k == 0:
        return 1
    # if binomial divisible by MOD -> zero
    vp = vp_factorial(n, MOD) - vp_factorial(k, MOD) - vp_factorial(n - k, MOD)
    if vp > 0:
        return 0
    # numerator product of k terms: (n-k+1)..n mod MOD
    start = n - k + 1
    num = 1
    for i in range(k):
        num = (num * ((start + i) % MOD)) % MOD
    ensure_fact(k)
    den_inv = inv_fact_cache[k]
    return num * den_inv % MOD

@lru_cache(None)
def ways_from_factors_tuple(factors_tuple, N):
    res = 1
    for (_, exp) in factors_tuple:
        res = (res * comb_large_n_small_k(N - 1 + exp, exp)) % MOD
        if res == 0:
            return 0
    return res

def ways_of_number(k: int, N: int):
    if k == 1:
        return 1
    f = factorize(k)
    t = tuple(sorted(f.items()))
    return ways_from_factors_tuple(t, N)

def solve_file(
    input_path=r"C:\Users\dell\Desktop\MetaHackerCup\p4\final_product_chapter_2_input.txt",
    output_path=r"C:\Users\dell\Desktop\MetaHackerCup\p4\validation_output.txt"
):

    random.seed(0)  # helps reproducibility of Pollard-Rho choices
    with open(input_path, "r") as fin:
        data = fin.read().strip().split()
    it = iter(data)
    t = int(next(it))
    out_lines = []
    for case in range(1, t + 1):
        N = int(next(it)); A = int(next(it)); B = int(next(it))
        B_factors = factorize(B)
        divs = gen_divisors_from_factors(B_factors)
        total = 0
        for x in divs:
            if x <= A:
                wx = ways_of_number(x, N)
                wbx = ways_of_number(B // x, N)
                total = (total + wx * wbx) % MOD
        out_lines.append(f"Case #{case}: {total}")
    with open(output_path, "w") as fout:
        fout.write("\n".join(out_lines) + "\n")
    print("Saved to", output_path)

if __name__ == "__main__":
    solve_file()
