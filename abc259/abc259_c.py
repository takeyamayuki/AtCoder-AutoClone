import sys
import re
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement, permutations, groupby
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
MOD = 998244353
num_list = []
str_list = []
alp = 'abcdefghijklmnopqrstuvwxyz'

s = s_input()
t = s_input()
cs = Counter(s)
ct = Counter(t)
numsl = []
numtl = []
nums = 1
numt = 1
noflag = False
counts = 0
countt = 0
count = 0


def runLengthEncode(S: str):
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res


tmps = runLengthEncode(s)
tmpt = runLengthEncode(t)

if len(tmps) != len(tmpt):
    print('No')
    exit()

# print(tmps, tmpt)
for i in range(len(tmps)):
    if tmps[i][0] != tmpt[i][0]:
        print('No')
        exit()
    if tmps[i][1] >= 2:
        if tmps[i][1] > tmpt[i][1]:
            print('No')
            exit()
    elif tmps[i][1] == 1:
        if tmpt[i][1] != 1:
            print('No')
            exit()

print('Yes')
