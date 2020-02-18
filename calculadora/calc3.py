
import sys
import operator

"""
CALCULADORA SIMPLE CON PYTHON VERSION 2
"""

if len(sys.argv) != 4:
    print("Usage Error: $calculadora.py OPERATION Number1 Number2")
else:
    operation = {"suma": operator.add(float(sys.argv[2]), float(sys.argv[3])),
                 "resta": operator.sub(float(sys.argv[2]), float(sys.argv[3])),
                 "multiplica": operator.mul(float(sys.argv[2]), float(sys.argv[3])),
                 "divide": operator.truediv(float(sys.argv[2]), float(sys.argv[3]))}

    print(operation.__getitem__(sys.argv[1]))
