import sys
import re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext
# input = sys.stdin.readline
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_row(n): return [i_input() for _ in range(n)]
def i_row_list(n): return [i_list() for _ in range(n)]
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())
def s_row(n): return [s_input() for _ in range(n)]
def s_row_str(n): return [s_list() for _ in range(n)]
def s_row_list(n): return [list(s_input()) for _ in range(n)]
def lcm(a, b): return a * b // gcd(a, b)
def printt(a): print(a, end="")


INF = float('inf')
MOD = 10**9+7
num_list = []
str_list = []
alp = 'abcdefghijklmnopqrstuvwxyz'

h, w = i_map()
a = i_row_list(h)

# 行のsum
sum_gyou = []
for i in range(h):
    sum_gyou.append(sum(a[i]))

# 列のsum
sum_retu = []
for i in range(w):
    tsum = 0
    for j in range(h):
        tsum += a[j][i]
    sum_retu.append(tsum)

for i in range(w):
    for j in range(h):
        a[j][i] = sum_gyou[j]+sum_retu[i]-a[j][i]

for i in range(h):
    print(*a[i])
# print(sum_gyou)
# print(sum_retu)
