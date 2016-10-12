import math
import operator

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

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

def modul(stk):
    if len(stk) == 0:
        stk.append(input())
    k = stk.pop()
    if type(k) in (int, long):
        j = 0
        if len(stk) == 0:
            j = input()
            j,k = k,j
        else:
            j = stk.pop()
        if type(j) in (int, long):
            stk.append(int(j % k))
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

def isprm(stk):
    if len(stk) == 0:
        stk.append(input())
    k = stk.pop()
    if type(k) in (long, int):
        if k == 2:
            stk.append(True)
            return
        if k <= 1 or k % 2 == 0:
            stk.append(False)
            return
        i = 3
        m = int(k**.5)
        while i <= m:
            if k % i == 0:
                stk.append(False)
                return
            i += 2
        stk.append(True)
        return
    else:
        stk.append(k)

def lowr(stk):
    if len(stk) == 0:
        stk.append(input())
    k = stk.pop()
    if type(k) is str:
        stk.append(k.lower())
    else:
        stk.append(k)

def highr(stk):
    if len(stk) == 0:
        stk.append(input())
    k = stk.pop()
    if type(k) is str:
        stk.append(k.upper())
    else:
        stk.append(k)

def rotr(stk):
    if len(stk) == 0: return
    k = stk.pop()
    stk = [k] + stk

def rotl(stk):
    if len(stk) == 0: return
    k = stk.pop(0)
    stk.append(k)

def cond(stk):
    if len(stk) == 0:
        return
    k = stk.pop()
    if type(k) is bool and len(stk) >= 2:
        if len(stk) >= 2:
            b = stk.pop()
            a = stk.pop()
            if k: stk.append(a)
            else: stk.append(b)
        elif len(stk) == 1:
            if not k: stk.pop(); stk.append(False)
        else:
            stk.append(k)
    elif type(k) in (list, str): stk.append(k[::-1])
    elif type(k) in (int, long, float): stk.append(type(k)(str(k)[::-1]))
    else:
        stk.append(k)

def sjoin(stk):
    if len(stk) < 1:
        return
    k = stk.pop()
    if type(k) is str:
        j = stk.pop()
        if type(j) is list:
            stk.append(k.join(map(str,j)))
        else:
            stk.append(j)
            stk.append(k)
    elif type(k) is list:
        stk.append('\n'.join(map(str,k)))
    else:
        stk.append(k)

def exrg(stk):
    if len(stk) == 0:
        stk.append(input())
    k = stk.pop()
    if type(k) is list and len(k) == 2:
        if all(isinstance(i, (int, long)) for i in k):
            stk.append(range(*k))
        else:
            stk.append(k)
    elif type(k) in (int, long):
        stk.append(range(k))
    else:
        stk.append(k)

def inrg(stk):
    if len(stk) == 0:
        stk.append(input())
    k = stk.pop()
    if type(k) is list and len(k) == 2:
        if all(isinstance(i, (int, long)) for i in k):
            stk.append(range(k[0],k[1]+1))
        else:
            stk.append(k)
    elif type(k) in (int, long):
        stk.append(range(1,k+1))
    else:
        stk.append(k)

def prnt(stk):
    print ''.join(map(str,stk))

def upal(stk): stk.append(alphabet)

def lwal(stk): stk.append(alphabet.lower())

def toup(stk):
    if len(stk) == 0:
        stk.append(raw_input())
    k = stk.pop()
    if type(k) is str:
        stk.append(k.upper())
    else:
        stk.append(k)

def tolw(stk):
    if len(stk) == 0:
        stk.append(raw_input())
    k = stk.pop()
    if type(k) is str:
        stk.append(k.lower())
    else:
        stk.append(k)

def zips(stk):
    if len(stk) == 0:
        return
    k = stk.pop()
    if type(k) in (str,list):
        if len(stk) == 0:
            if all(isinstance(i, (str,list)) for i in k):
                stk.append(zip(*k))
            else:
                stk.append(k)
        else:
            j = stk.pop()
            if type(j) in (str,list):
                stk.append(zip(j, k))
            else:
                stk.append(j)
                stk.append(k)
    else:
        stk.append(k)

def zipl(stk):
    if len(stk) == 0:
        return
    k = stk.pop()
    if type(k) in (str,list):
        if len(stk) == 0:
            if all(isinstance(i, (str,list)) for i in k):
                stk.append(map(None, *k))
            else:
                stk.append(k)
        else:
            j = stk.pop()
            if type(j) in (str,list):
                stk.append(map(None, j, k))
            else:
                stk.append(j)
                stk.append(k)
    else:
        stk.append(k)

def equl(stk):
    if len(stk) == 0:
        stk.append(input())
    k = stk.pop()
    if len(stk) == 0:
        stk.append(input())
    j = stk.pop()
    stk.append(k == j)

def evlt(stk):
    if len(stk) == 0:
        stk.append(raw_input())
    k = stk.pop()
    if type(k) is str:
        stk.append(eval(k))
    elif type(k) in (int, long):
        stk.append(~k)
    else:
        stk.append(k)
        

def noop(stk):
    return
