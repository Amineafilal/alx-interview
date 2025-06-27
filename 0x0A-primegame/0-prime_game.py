#!/usr/bin/python3

def is_prime(n):
    """Check if a number is a prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(n):
    """Generate a list of prime numbers up to n"""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n + 1, i):
                sieve[j] = False
    primes = [i for i, is_p in enumerate(sieve) if is_p]
    return primes

def isWinner(x, nums):
    """Determine the winner of the prime game"""
    if x < 1 or not nums:
        return None

    max_num = max(nums)
    primes_up_to = [0] * (max_num + 1)
    prime_count = 0
    for i in range(1, max_num + 1):
        if is_prime(i):
            prime_count += 1
        primes_up_to[i] = prime_count

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if primes_up_to[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
