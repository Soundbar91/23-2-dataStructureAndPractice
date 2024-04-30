import time

def fib(n):
    if n == 0 :
        return 0
    
    elif n == 1 :
        return 1
    
    else :
        return fib(n - 2) + fib(n - 1)

def fib_iter(n):
    
    result = 0
    pre1_fib_iter = 1
    pre2_fib_iter = 0

    if n == 0 :
        return 0
    
    elif n == 1 :
        return 1

    for i in range(2, n + 1):
        result = pre2_fib_iter + pre1_fib_iter
        pre2_fib_iter = pre1_fib_iter
        pre1_fib_iter = result
    return result

print('Fibonacci순환(5) : ', fib(5))
print('Fibonacci반복(5) : ', fib_iter(5))

for i in range (1, 40):

    start_fib = time.time()
    fib(i)
    end_fib = time.time()

    start_fib_iter = time.time()
    fib_iter(i)
    end_fib_iter = time.time()

    print('n = %2d' %(i), end = " ")
    print('반복 : ', end_fib_iter - start_fib_iter, end="")
    print(' 순환 : ', end_fib - start_fib)

for i in range (1, 40):
    print('n = %2d 반복 : %8d 순환 : %8d' %(i, fib(i), fib_iter(i)))