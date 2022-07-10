import sys
import re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import deepcopy
from collections import Counter, deque, defaultdict
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

n = i_input()
co = []
for _ in range(n):
    x, y = i_map()
    co.append([x, y])

# print(co)
ans = 0
for v in combinations(co, 3):
    # x0,y0 x1,y1 x2,y2
    # print(*v)
    if (v[0][1]-v[1][1])*(v[0][0]-v[2][0]) != (v[0][1]-v[2][1])*(v[0][0]-v[1][0]):
        ans += 1
print(ans)
