# 04_fibonatch.pyを動的計画法で効率化する

# 動的計画法(1)
def fib_memo(n):
    memo = [None]*(n+1)
    def _fib(n):
        if n == 0 or n == 1:
            return 1
        if memo[n] != None:
            return memo[n]
        return _fib(n-1) + _fib(n-2)
    return _fib(n)
    
if __name__ == '__main__':
    for i in range(35):
        print(fib_memo(i))
        

# 動的計画法(2)
def fib_dp(n):
    memo = [None]*n
    memo[0] = 1
    memo[1] = 1
    for i in range(2, n):
        memo[i] = memo[i-1] + memo[i-2]
    return memo

if __name__ == '__main__':
    for i in fib_dp(35):
        print(i)