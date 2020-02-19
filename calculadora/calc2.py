#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

"""
CALCULADORA SIMPLE CON PYTHON VERSION 2
"""

if len(sys.argv) != 4:
    print("Usage Error: $calculadora.py OPERATION Number1 Number2")
else:

    try:
        operation ={"suma": float(sys.argv[2])+float(sys.argv[3]),
                    "resta": float(sys.argv[2])-float(sys.argv[3]),
                    "multiplica": float(sys.argv[2])*float(sys.argv[3]),
                    "divide": float(sys.argv[2])/float(sys.argv[3])}

        print(operation.__getitem__(sys.argv[1]))

    except ZeroDivisionError:
        print("Usage Error: You try to divide by zero")
    except ValueError:
        print("could not convert string to float:", sys.argv[1], sys.argv[2], sys.argv[3])
