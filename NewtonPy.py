#!/usr/bin/python
# mejor_aprox =  (aprox + n/aprox)/2

import sys
from optparse import OptionParser
parser = OptionParser()

uso = "\n %prog [numero]"
parser = OptionParser(usage=uso)


def raizq(x):
     aprox = x
     i = 0;
     while i <= x:
          aprox =  (aprox + x/aprox)/2.0
          i += 1
     print aprox


if(sys.argv[1:] == []):
#    parser.print_help()
     print("\n NewtonPy 0.1  -  by MarcoSouza\n\n")
     n=raw_input("Numero para calcular sua raiz quadrada: ")
     raizq(int(n))
elif (sys.argv[1] == '-h'):
     parser.print_help()
else:
     print("\n NewtonPy 0.1  -  by MarcoSouza\n\n")
     arg=sys.argv[1]
     raizq(int(arg))

