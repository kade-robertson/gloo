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
        if program[pos] in allnums[:-1]: # number parse mode
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
        elif program[pos] == '"': # string parse mode
            sstr = ''
            pos += 1
            while pos < len(program) and program[pos] != '"':
                sstr += program[pos]
                pos  += 1
            stack.append(sstr)
        elif program[pos] == "'": # char parse mode
            pos += 1
            stack.append(program[pos])
        elif hex(ord(program[pos])) == "0x91": # foreach loop (mapping)
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
        elif hex(ord(program[pos])) == '0xb6': # 1-char mapping
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
        elif program[pos] == '|': # do action while len(list/str)>1
            pos += 1
            if not len(stack) == 0:
                k = stack.pop()
                if type(k) in (list, str):
                    while len(k) > 1:
                        temp, supprint = process(program[pos], [k], False)
                        k = temp[0]
                    stack.append(k[0])
                else:
                    stack.append(k)
        elif program[pos] == '<': # while top of stack is truthy, execute between
            nest = 1
            if not len(stack) == 0:
                k = stack
                mapprog = ""
                pos += 1
                while pos < len(program) and nest > 0:
                    if program[pos] == ">": nest += 1
                    elif program[pos] == "<": nest -= 1
                    if nest > 0:
                        mapprog += program[pos]
                        pos += 1
                while k[-1]:
                    k, supprint = process(mapprog, k, False)
                stack.append(k)
        else:
            codepage[hex(ord(program[pos]))](stack)
        if pos < len(program) and pos >= 1 and program[pos] in 'p' and program[pos-1] != "'":
            supprint = True
        if debug: print "DEBUG:: POS: %d, CHAR: '%s', STACK: %s"%(pos, program[pos], str(stack))
        pos += 1
    if not supprint and not nested and stack != []: print ''.join(map(str,stack))
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
    elif args.p is not None:
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
