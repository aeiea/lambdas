'''
Just-for-fun lambda functions for any use. If you liked this project, please contribute/star it!
gh: https://github.com/aeiea/lambdas
Copyright © 2000 aeiea <dpthn at proton dot me>
This work is free. You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To Public License, Version 2,
as published by Sam Hocevar. See http://www.wtfpl.net/ for more details.
'''
import sys
sys.setrecursionlimit(2147483647)
factorial = lambda n: 1 if n == 1 else factorial(n - 1) * n
binom = lambda n, r: factorial(n)/(factorial(n - r) * factorial(r))
iseven = lambda n: True if n // 2 == 0 else False
rangelist = lambda strt, stop, step = 1: [strt] if stop - step == strt else [strt] + rangelist(strt + step, stop, step)
convertnumbertobase = lambda n, b: int(str(convertnumbertobase(n // b, b)) + str(n % b)) if n >= b else n
fib = lambda n: 1 if n == 1 or n == 2 else fib(n - 1) + fib(n)