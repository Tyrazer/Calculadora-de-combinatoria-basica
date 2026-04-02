import math
def combinacion(n,k):
    if k>n:
         return 0
    return math.comb(n,k)
