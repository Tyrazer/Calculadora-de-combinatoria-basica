import math 
#Combinación sin repetición
def combinacion_sin_rep(n,k):
    if k>n:
         return 0
    else:
        return math.comb(n,k)
#Combinación con repetición
def combinacion_con_rep(n,k):
     if n==0 and k==0:
          return 1
     elif n==0:
          return 0
     else:
          return math.comb(n+k-1,k)
#Números de stirling de segunda clase
def stirling_second(n,k):
     if k==0 or k>n:
          return 0
     elif k==1 or k==n:
          return 1
     else:
          return k*stirling_second(n-1,k)+stirling_second(n-1,k-1)
#Permutación 
def permutacion(n,k):
     if k>n:
          return 0
     else:
          return math.perm(n,k)
#Permutación con frecuencias
def permutacion_con_rep(n, frecuencias):
     denom=1
     for f in frecuencias:
          denom*=math.factorial(f)
     return math.factorial(n)//denom
#Permuación con repeticiones ilimitadas(máximo k)
def permutacion_con_repetidos(n, k):
     if n < k:
          return 0
     else: 
          return n**k