import operator

def add(stk):
    if len(stk) == 0: return
    k = stk.pop()
    if type(k) is list:
        if all(isinstance(i, (int, long, float)) for i in k):
            stk.append(sum(k))
        elif all(isinstance(i, str) for i in k):
            stk.append(''.join(k))
        else:
            stk.append(k)
    elif type(k) in (int, long, float):
        if len(stk) == 0:
            stk.append(k)
            return
        j = stk.pop()
        if type(j) in (int, long, float):
            stk.append(k + j)
        else:
            stk.append(j)
            stk.append(k)
    elif type(k) is str:
        if len(stk) == 0:
            stk.append(k)
            return
        j = stk.pop()
        if type(j) is str:
            stk.append(j + k)
        else:
            stk.append(j)
            stk.append(k)
    else:
        stk.append(k)

def subt(stk):
    if len(stk) == 0: return
    k = stk.pop()
    if type(k) is list:
        k = [i for i in k if i]
        stk.append(k)
    elif type(k) in (int, long, float):
        if len(stk) == 0:
            stk.append(k)
            return
        j = stk.pop()
        if type(j) in (int, long, float):
            stk.append(j - k)
        else:
            stk.append(j)
            stk.append(k)
    elif type(k) is str:
        if len(stk) == 0:
            stk.append(k)
            return
        j = stk.pop()
        if type(j) is str:
            stk.append(j.replace(k, ''))
        else:
            stk.append(j)
            stk.append(k)
    else:
        stk.append(k)

def mult(stk):
    if len(stk) == 0: return
    k = stk.pop()
    if type(k) is list:
        if all(isinstance(i, (int, long, float)) for i in k):
            stk.append(reduce(operator.mul, k, 1))
        else:
            stk.append(k)
    elif type(k) in (int, long, float):
        if len(stk) == 0:
            stk.append(k)
            return
        j = stk.pop()
        if type(j) in (int, long, float):
            stk.append(j * k)
        elif type(k) in (int, long) and type(j) is str:
            stk.append(j * k)
        else:
            stk.append(j)
            stk.append(k)
    elif type(k) is str:
        if len(stk) == 0:
            stk.append(k)
            return
        j = stk.pop()
        if type(j) in (int, long):
            stk.append(j * k)
        else:
            stk.append(j)
            stk.append(k)
    else:
        stk.append(k)

def divd(stk):
    if len(stk) == 0: return
    k = stk.pop()
    if type(k) in (int, long, float):
        if len(stk) == 0:
            stk.append(k)
            return
        j = stk.pop()
        if type(j) in (int, long, float):
            stk.append(float(j) / float(k))
        else:
            stk.append(j)
            stk.append(k)
    else:
        stk.append(k)

def divint(stk):
    if len(stk) == 0: return
    k = stk.pop()
    if type(k) in (int, long, float):
        if len(stk) == 0:
            stk.append(k)
            return
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
    if len(stk) == 0: return
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

def noop(stk):
    return
