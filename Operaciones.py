import math 

def combinacion(n,k):
    if k>n:
         return 0
    else:
        return math.comb(n,k)

def stirling_second(n,k):
     if k==0 or k>n:
          return 0
     elif k==1 or k==n:
          return 1
     else:
          return k*stirling_second(n-1,k)+stirling_second(n-1,k-1)

def permutacion(n,k):
     if k>n:
          return 0
     else:
          return math.perm(n,k)