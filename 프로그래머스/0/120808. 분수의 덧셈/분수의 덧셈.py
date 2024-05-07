import math

def solution(numer1, denom1, numer2, denom2):
    sum_denom = denom1 * denom2
    sum_numer = numer1 * denom2 + numer2 * denom1
    gcd = math.gcd(sum_denom, sum_numer)
    return [sum_numer/gcd, sum_denom/gcd]