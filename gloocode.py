# -*- coding: utf-8 -*-

from gloofunc import *

codepage = {
     '0x0': noop,
     '0x1': noop,
     '0x2': noop,
     '0x3': noop,
     '0x4': noop,
     '0x5': noop,
     '0x6': noop,
     '0x7': noop,
     '0x8': noop,
     '0x9': noop,
     '0xa': noop,
     '0xb': noop,
     '0xc': noop,
     '0xd': noop,
     '0xe': noop,
     '0xf': noop,
    '0x10': noop,
    '0x11': noop,
    '0x12': noop,
    '0x13': noop,
    '0x14': noop,
    '0x15': noop,
    '0x16': noop,
    '0x17': noop,
    '0x18': noop,
    '0x19': noop,
    '0x1a': noop,
    '0x1b': noop,
    '0x1c': noop,
    '0x1d': noop,
    '0x1e': noop,
    '0x1f': noop,
    '0x20': noop,
    '0x21': fact,    # ! - factorial function, single numbers and list mapping
    '0x22': noop,
    '0x23': noop,
    '0x24': sort,    # $ - sort list or string, negates number
    '0x25': modul,   # % - modulus
    '0x26': noop,
    '0x27': noop,    # ' - read single char
    '0x28': noop,
    '0x29': noop,
    '0x2a': mult,    # * - multiply function / reduce, string multiply
    '0x2b':  add,    # + - addition function / reduce, string join, append
    '0x2c': drop,    # , - pop last
    '0x2d': subt,    # - - subtract function, string remove, false filter
    '0x2e': noop,    # . - used for floats
    '0x2f': divd,    # / - division function
    '0x30': noop,    # 0 - reserved for int/float
    '0x31': noop,    # 1 - reserved for int/float
    '0x32': noop,    # 2 - reserved for int/float
    '0x33': noop,    # 3 - reserved for int/float
    '0x34': noop,    # 4 - reserved for int/float
    '0x35': noop,    # 5 - reserved for int/float
    '0x36': noop,    # 6 - reserved for int/float
    '0x37': noop,    # 7 - reserved for int/float
    '0x38': noop,    # 8 - reserved for int/float
    '0x39': noop,    # 9 - reserved for int/float
    '0x3a': rotl,    # : - rotate stack left
    '0x3b': swap,    # ; - swap top two items
    '0x3c': noop,  
    '0x3d': noop,
    '0x3e': noop,
    '0x3f': cond,    # ? - conditional, reverse string/list/number
    '0x40': rotr,    # @ - rotate stack right
    '0x41': highr,   # A - str to upper case
    '0x42': noop,
    '0x43': noop,
    '0x44': noop,
    '0x45': noop,
    '0x46': noop,
    '0x47': noop,
    '0x48': noop,
    '0x49': rinp,    # I - raw input
    '0x4a': noop,
    '0x4b': noop,
    '0x4c': noop,
    '0x4d': maxm,    # M - greater-than compare, maximum of list
    '0x4e': noop,
    '0x4f': noop,
    '0x50': noop,
    '0x51': noop,
    '0x52': inrg,    # R - inclusive range function
    '0x53': noop,
    '0x54': noop,
    '0x55': noop,
    '0x56': noop,
    '0x57': noop,
    '0x58': noop,
    '0x59': noop,
    '0x5a': zipl,    # Z - zip by longest
    '0x5b': wrap,    # [ - wrap stack in list
    '0x5c': divint,  # \ - division function (integer)
    '0x5d': uwrap,   # ] - unwrap list at top of stack
    '0x5e': noop,
    '0x5f': dupl,    # _ - duplicate top item
    '0x60': noop,
    '0x61': lowr,    # a - str to lower case
    '0x62': noop,
    '0x63': noop,
    '0x64': noop,
    '0x65': noop,
    '0x66': noop,
    '0x67': noop,
    '0x68': noop,
    '0x69': inpt,    # i - eval'd input
    '0x6a': sjoin,   # j - joing by string/char
    '0x6b': noop,
    '0x6c': noop,
    '0x6d': minm,    # m - less-than compare, minimum of list
    '0x6e': noop,
    '0x6f': noop,
    '0x70': prnt,    # p - prints stack, suppresses end-of-program print
    '0x71': noop,
    '0x72': exrg,    # r - exclusive range function
    '0x73': noop,
    '0x74': noop,
    '0x75': noop,
    '0x76': noop,
    '0x77': noop,
    '0x78': noop,
    '0x79': noop,
    '0x7a': zips,    # z - standard python zip
    '0x7b': noop,
    '0x7c': noop,
    '0x7d': noop,
    '0x7e': noop,
    '0x7f': noop,
    '0x80': noop,
    '0x81': noop,
    '0x82': noop,
    '0x83': noop,
    '0x84': noop,
    '0x85': noop,
    '0x86': noop,
    '0x87': noop,
    '0x88': noop,
    '0x89': noop,
    '0x8a': noop,
    '0x8b': noop,
    '0x8c': noop,
    '0x8d': noop,
    '0x8e': noop,
    '0x8f': noop,
    '0x90': noop,
    '0x91': noop,    # ‘ - reserved for list mapping (begin)
    '0x92': noop,    # ’ - reserved for list mapping (end)
    '0x93': noop,
    '0x94': noop,
    '0x95': noop,
    '0x96': noop,
    '0x97': noop,
    '0x98': noop,
    '0x99': noop,
    '0x9a': noop,
    '0x9b': noop,
    '0x9c': noop,
    '0x9d': noop,
    '0x9e': noop,
    '0x9f': noop,
    '0xa0': noop,
    '0xa1': noop,
    '0xa2': noop,
    '0xa3': noop,
    '0xa4': noop,
    '0xa5': noop,
    '0xa6': noop,
    '0xa7': noop,
    '0xa8': noop,
    '0xa9': noop,
    '0xaa': noop,
    '0xab': noop,
    '0xac': noop,
    '0xad': noop,
    '0xae': noop,
    '0xaf': noop,
    '0xb0': noop,
    '0xb1': noop,
    '0xb2': noop,
    '0xb3': noop,
    '0xb4': noop,
    '0xb5': noop,
    '0xb6': noop,    # ¶ - reserved for single operation mapping
    '0xb7': noop,
    '0xb8': noop,
    '0xb9': noop,
    '0xba': noop,
    '0xbb': noop,
    '0xbc': noop,
    '0xbd': noop,
    '0xbe': noop,
    '0xbf': noop,
    '0xc0': noop,
    '0xc1': noop,
    '0xc2': noop,
    '0xc3': noop,
    '0xc4': toup,    # Ä - converts top string to uppercase
    '0xc5': upal,    # Å - pushes uppercase alphabet to stack
    '0xc6': noop,
    '0xc7': noop,
    '0xc8': noop,
    '0xc9': noop,
    '0xca': noop,
    '0xcb': noop,
    '0xcc': noop,
    '0xcd': noop,
    '0xce': noop,
    '0xcf': noop,
    '0xd0': noop,
    '0xd1': noop,
    '0xd2': noop,
    '0xd3': noop,
    '0xd4': noop,
    '0xd5': noop,
    '0xd6': noop,
    '0xd7': noop,
    '0xd8': noop,
    '0xd9': noop,
    '0xda': noop,
    '0xdb': noop,
    '0xdc': noop,
    '0xdd': noop,
    '0xde': isprm,   # Þ - primality test
    '0xdf': noop,
    '0xe0': noop,
    '0xe1': noop,
    '0xe2': noop,
    '0xe3': noop,
    '0xe4': tolw,    # ä - converts top string to lowercase
    '0xe5': lwal,    # å - pushes uppercase alphabet to stack
    '0xe6': noop,
    '0xe7': noop,
    '0xe8': noop,
    '0xe9': noop,
    '0xea': noop,
    '0xeb': noop,
    '0xec': noop,
    '0xed': noop,
    '0xee': noop,
    '0xef': noop,
    '0xf0': noop,
    '0xf1': noop,
    '0xf2': noop,
    '0xf3': noop,
    '0xf4': noop,
    '0xf5': noop,
    '0xf6': noop,
    '0xf7': noop,
    '0xf8': noop,
    '0xf9': noop,
    '0xfa': noop,
    '0xfb': noop,
    '0xfc': noop,
    '0xfd': noop,
    '0xfe': noop,
    '0xff': noop,
}
