def fibo(n) :
    if n == 1 or n == 2 :
        return 1
    else :
        return fibo(n-2) + fibo(n-1)
print(fibo(1))
print(fibo(2))
print(fibo(3))
print(fibo(4))
print(fibo(5))