import time
import math
import random

cache = []
cache = [-1 for _ in range(100)]

def fibonacci_rec(n):
    if n in (0, 1):
        return 1
    return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)
    
def fibonacci_dp(n):
    if n in (0, 1):
        return 1
    if cache[n] != -1:
        return cache[n]
    result = fibonacci_dp(n - 1) + fibonacci_dp(n - 2)
    cache[n] = result
    return result
    
    
def fibonacci_iter(n):
    if n in (0, 1):
        return 1
    prev, curr = 1, 1
    for _ in range(n - 1):
        next = prev + curr
        prev = curr
        curr = next
    return curr
    
    
if __name__ == '__main__':
    start_time = time.time()
    print("result iter = {result}".format(result=fibonacci_iter(40)))
    end_time = time.time()
    print('iter speed = {time} s'.format(time=(end_time - start_time)))            
    
    start_time = time.time()
    print("result dp = {result}".format(result=fibonacci_dp(40)))
    end_time = time.time()
    print('dp speed = {time} s'.format(time=(end_time - start_time)))        
    
    start_time = time.time()
    print("result rec = {result}".format(result=fibonacci_rec(40)))
    end_time = time.time()
    print('rec speed = {time} s'.format(time=(end_time - start_time)))        
    
    
