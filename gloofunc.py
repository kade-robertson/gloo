import math
import operator

def add(stk):
    if len(stk) == 0:
        stk.append(input())
    k = stk.pop()
    if type(k) is list:
        if all(isinstance(i, (int, long, float)) for i in k):
            stk.append(sum(k))
        elif all(isinstance(i, str) for i in k):
            stk.append(''.join(k))
        else:
            stk.append(k)
    elif type(k) in (int, long, float):
        j = 0
        if len(stk) == 0:
            j = input()
            j,k = k,j
        else:
            j = stk.pop()
        if type(j) in (int, long, float):
            stk.append(k + j)
        else:
            stk.append(j)
            stk.append(k)
    elif type(k) is str:
        j = 0
        if len(stk) == 0:
            j = input()
            j,k = k,j
        else:
            j = stk.pop()
        if type(j) is str:
            stk.append(j + k)
        else:
            stk.append(j)
            stk.append(k)
    else:
        stk.append(k)

def subt(stk):
    if len(stk) == 0:
        stk.append(input())
    k = stk.pop()
    if type(k) is list:
        k = [i for i in k if (i and i != ' ')]
        stk.append(k)
    elif type(k) in (int, long, float):
        j = 0
        if len(stk) == 0:
            j = input()
            j,k = k,j
        else:
            j = stk.pop()
        if type(j) in (int, long, float):
            stk.append(j - k)
        else:
            stk.append(j)
            stk.append(k)
    elif type(k) is str:
        j = 0
        if len(stk) == 0:
            j = input()
            j,k = k,j
        else:
            j = stk.pop()
        if type(j) is str:
            stk.append(j.replace(k, ''))
        else:
            stk.append(j)
            stk.append(k)
    else:
        stk.append(k)

def mult(stk):
    if len(stk) == 0:
        stk.append(input())
    k = stk.pop()
    if type(k) is list:
        if all(isinstance(i, (int, long, float)) for i in k):
            stk.append(reduce(operator.mul, k, 1))
        else:
            stk.append(k)
    elif type(k) in (int, long, float):
        j = 0
        if len(stk) == 0:
            j = input()
            j,k = k,j
        else:
            j = stk.pop()
        if type(j) in (int, long, float):
            stk.append(j * k)
        elif type(k) in (int, long) and type(j) is str:
            stk.append(j * k)
        else:
            stk.append(j)
            stk.append(k)
    elif type(k) is str:
        j = 0
        if len(stk) == 0:
            j = input()
            j,k = k,j
        else:
            j = stk.pop()
        if type(j) in (int, long):
            stk.append(j * k)
        else:
            stk.append(j)
            stk.append(k)
    else:
        stk.append(k)

def divd(stk):
    if len(stk) == 0:
        stk.append(input())
    k = stk.pop()
    if type(k) in (int, long, float):
        j = 0
        if len(stk) == 0:
            j = input()
            j,k = k,j
        else:
            j = stk.pop()
        if type(j) in (int, long, float):
            stk.append(float(j) / float(k))
        else:
            stk.append(j)
            stk.append(k)
    else:
        stk.append(k)

def divint(stk):
    if len(stk) == 0:
        stk.append(input())
    k = stk.pop()
    if type(k) in (int, long, float):
        j = 0
        if len(stk) == 0:
            j = input()
            j,k = k,j
        else:
            j = stk.pop()
        if type(j) in (int, long, float):
            stk.append(int(j / k))
        else:
            stk.append(j)
            stk.append(k)
    else:
        stk.append(k)

def wrap(stk):
    newl = []
    while len(stk) > 0:
        newl = [stk.pop()] + newl
    stk.append(newl)

def uwrap(stk):
    if len(stk) == 0:
        stk.append(input())
    k = stk.pop()
    if type(k) is list:
        for item in k:
            stk.append(item)
    else:
        stk.append(K)

def inpt(stk):
    try: stk.append(input())
    except: return

def rinp(stk):
    try: stk.append(raw_input())
    except: return

def sort(stk):
    if len(stk) == 0:
        stk.append(input())
    k = stk.pop()
    if type(k) in (str, list): stk.append(sorted(k))
    elif type(k) in (int, long, float): stk.append(-1 * k)
    else: stk.append(k)

def fact(stk):
    if len(stk) == 0:
        stk.append(input())
    k = stk.pop()
    if type(k) in (int, long, float):
        if type(k) is float: k = math.gamma(k+1)
        else: k = math.factorial(k)
        stk.append(k)
    elif type(k) is list:
        if all(isinstance(i, (int, long, float)) for i in k):
            for a in xrange(0, len(k)):
                if type(k[a]) is float: k[a] = math.gamma(k[a]+1)
                else: k[a] = math.factorial(k[a])
            stk.append(k)
        else:
            stk.append(k)
    else:
        stk.append(k)

def drop(stk):
    if len(stk) == 0: return
    stk.pop()

def swap(stk):
    if len(stk) < 2: return
    k = stk.pop()
    j = stk.pop()
    stk.append(k)
    stk.append(j)

def minm(stk):
    if len(stk) == 0:
        stk.append(input())
    k = stk.pop()
    if type(k) is list:
        stk.append(min(k))
    else:
        j = 0
        if len(stk) == 0:
            j = input()
            j,k = k,j
        else:
            j = stk.pop()
        if type(j) is not list:
            stk.append(j < k)
        else:
            stk.append(j)
            stk.append(k)

def maxm(stk):
    if len(stk) == 0:
        stk.append(input())
    k = stk.pop()
    if type(k) is list:
        stk.append(max(k))
    else:
        j = 0
        if len(stk) == 0:
            j = input()
            j,k = k,j
        else:
            j = stk.pop()
        if type(j) is not list:
            stk.append(j > k)
        else:
            stk.append(j)
            stk.append(k)

def dupl(stk):
    if len(stk) == 0:
        stk.append(input())
    k = stk.pop()
    stk.append(k)
    stk.append(k)

def noop(stk):
    return
