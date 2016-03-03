"""
Sieve of Erastosthenes implementation based on this BitArray implementation
"""
from bitarray import BitArray

MAX = 1024

bits = BitArray(MAX, default=True)
bits[0] = False
bits[1] = False

for x in range(2, MAX):
    if not bits[x]:  # Already marked as not prime
        continue

    # Start at the square of this number
    i = x*x

    while i <= MAX:
        bits[i] = False
        i += x

primes = [idx for (idx, bit) in enumerate(bits) if bit]
print(primes)
