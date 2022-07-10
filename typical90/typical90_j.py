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


n = i_input()
p1 = [0]*n
p2 = [0]*n
for i in range(n):
    tc, tp = i_map()
    if tc == 1:
        p1[i] = tp
    else:
        p2[i] = tp

s1 = [0]*(n+1)
s2 = [0]*(n+1)
for i in range(n):
    s1[i+1] = s1[i]+p1[i]
    s2[i+1] = s2[i]+p2[i]

q = i_input()
for i in range(q):
    l, r = i_map()
    #s1[i]=p1[0]+...p1[i-1]
    print(s1[r]-s1[l-1], s2[r]-s2[l-1])
