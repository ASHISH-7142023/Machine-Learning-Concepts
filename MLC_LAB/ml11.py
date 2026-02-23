def is_prime(n):
    if n<=1:
       return False
    i=2
    while i*i<=n:
       if n%i==0:
          return False
       i=i+1
    return True
test_vals=[2,4,17,18,19]
i=0
while i<5:
    v=test_vals[i]
    print(v,"->",is_prime(v))
    i=i+1