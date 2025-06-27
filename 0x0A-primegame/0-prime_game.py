#!/usr/bin/python3
"""
Prime Game Module
"""


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game for multiple rounds.

    Args:
    x (int): The number of rounds.
    nums (list): An array of n for each round.

    Returns:
    str: Name of the player that won the most rounds (Maria or Ben).
         Returns None if the winner cannot be determined.
    """
    if not nums or x < 1:
        return None

    max_num = max(nums)

    # Create a list of boolean values to represent prime numbers
    primes = [True for _ in range(max(max_num + 1, 2))]
    primes[0] = primes[1] = False

    # Use the Sieve of Eratosthenes to mark non-prime numbers
    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if primes[i]:
            for j in range(i * i, max_num + 1, i):
                primes[j] = False

    # Count the number of primes less than or equal to each number in nums
    prime_counts = [0] * (max_num + 1)
    for i in range(2, max_num + 1):
        prime_counts[i] = prime_counts[i - 1]
        if primes[i]:
            prime_counts[i] += 1

    maria_wins = 0
    for n in nums:
        if prime_counts[n] % 2 == 1:
            maria_wins += 1

    if maria_wins * 2 == len(nums):
        return None
    if maria_wins * 2 > len(nums):
        return "Maria"
    return "Ben"
