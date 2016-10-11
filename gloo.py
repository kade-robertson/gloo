import sys
import argparse
from gloocode import *

def numparse(n):
    if '.' in n:
        return float(n)
    else:
        return int(n)

allnums = '0123456789.'

def process(program, stack=[], supprint=False):
    pos = 0
    while pos < len(program):
        if program[pos] in allnums[:-1]:
            numstr = program[pos]
            hasdot = False
            pos += 1
            while pos < len(program) and program[pos] in allnums:
                if program[pos] == '.':
                    if hasdot: break
                    else: hasdot = True
                numstr += program[pos]
                pos += 1
            pos -= 1
            stack.append(numparse(numstr))
        elif program[pos] == '"':
            sstr = ''
            pos += 1
            while pos < len(program) and program[pos] != '"':
                sstr += program[pos]
                pos  += 1
            stack.append(sstr)
        elif program[pos] == "'":
            pos += 1
            stack.append(program[pos])
        elif program[pos] == "|":
            if not len(stack) == 0:
                k = stack.pop()
                l = []
                if type(k) is list:
                    mapprog = ""
                    pos += 1
                    while pos < len(program) and program[pos] != "|":
                        mapprog += program[pos]
                        pos += 1
                    for i in xrange(0, len(k)):
                        l.append(process(mapprog, [k[i]], True)[0])
                    stack.append(l)
                else:
                    stack.append(k)
        else:
            codepage[hex(ord(program[pos]))](stack)
        pos += 1
    if not supprint: print ''.join(map(str,stack))
    return stack

def main():
    pargs = argparse.ArgumentParser( description = 'Interpreter for the Gloo programming language.' )
    pargs.add_argument('-f', nargs = '?', help='read Gloo program from a file')
    args, rest = pargs.parse_known_args()
    if args.f is not None:
        with open(args.f) as prog:
            process(prog.read())
    else:
        prog = raw_input("gloo # ")
        while prog != 'ungloo me!':
            process(prog)
            prog = raw_input("gloo # ")
        
if __name__ == '__main__':
    main()
