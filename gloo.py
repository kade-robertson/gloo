# -*- coding: utf-8 -*-

import sys
import argparse
from gloocode import *

def numparse(n):
    if '.' in n:
        return float(n)
    else:
        return int(n)

allnums = '0123456789.'

def process(program, stack=[], supprint=False, debug=False):
    nested = stack != []
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
        elif hex(ord(program[pos])) == "0x91":
            nest = 1
            if not len(stack) == 0:
                k = stack.pop()
                l = []
                if type(k) in (str, list):
                    mapprog = ""
                    pos += 1
                    while pos < len(program) and nest > 0:
                        if hex(ord(program[pos])) == "0x91": nest += 1
                        elif hex(ord(program[pos])) == "0x92": nest -= 1
                        if nest > 0:
                            mapprog += program[pos]
                            pos += 1
                    for i in xrange(0, len(k)):
                        s, supprint = process(mapprog, [i, k[i]], False)
                        l += s[-1:]
                    stack.append(l)
                else:
                    stack.append(k)
        elif hex(ord(program[pos])) == '0xb6':
            pos += 1
            if not len(stack) == 0:
                k = stack.pop()
                l = []
                if type(k) in (str, list):
                    for i in xrange(0, len(k)):
                        s, supprint = process(program[pos], [i, k[i]], False)
                        l += s[-1:]
                    stack.append(l)
                else:
                    stack.append(k)
        else:
            codepage[hex(ord(program[pos]))](stack)
        if pos < len(program) and pos >= 1 and program[pos] in 'p' and program[pos-1] != "'":
            supprint = True
        pos += 1
        if debug: print "DEBUG: " + str(stack)
    if not supprint and not nested: print ''.join(map(str,stack))
    return stack, supprint

def main():
    pargs = argparse.ArgumentParser( description = 'Interpreter for the Gloo programming language.' )
    pargs.add_argument('-f', nargs = '?', help='read Gloo program from a file')
    pargs.add_argument('-d', action='store_true', help='enable debug printing of stack')
    pargs.add_argument('-p', nargs = '?', help='runs Gloo program from argument') 
    args, rest = pargs.parse_known_args()
    if args.f is not None:
        with open(args.f) as prog:
            process(prog.read(), stack=[], debug=args.d)
    if args.p is not None:
        process(args.p, stack=[], debug=args.d)
    else:
        prog = raw_input("gloo # ")
        while prog != 'ungloo me!':
            if prog == "quine": print "quine"
            elif prog == "": print "Hello, world!"
            else: process(prog, stack=[], debug=args.d)
            prog = raw_input("gloo # ")
        
if __name__ == '__main__':
    main()
