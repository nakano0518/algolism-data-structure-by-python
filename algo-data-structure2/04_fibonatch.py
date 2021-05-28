# フィボナッチ数列の第n項目の算出プログラム(一般化し、)
# 35項までの要素をすべて出力せよ

# 【ロジック】
# fib(n) = fib(n-1) + fib(n-2) 
# 上記のように関数の和の形で書ける ⇒　再帰関数
# fib(n)は、f(n-1)とfib(n-2)の部分問題に分割できるので統合して足し合わせreturn(分割統治法)
# 再帰は終了条件が必要

def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n-1)+fib(n-2)

for i in range(35):
    print(fib(i))