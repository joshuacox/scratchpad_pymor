#!/usr/bin/env python

from add import add
from add import my_adder
from add import matrix_adder

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

c = my_adder( a, b )
#my_printer(c)

matrix1 = [[1, -2], [-3, 4]]
matrix2 = [[2, -1], [0, -1]]

matrix3 = matrix_adder( matrix1, matrix2 )
#matrix_printer(matrix3)

print("Here is the desired answer")
print (add( matrix1, matrix2 ))

print("Here is the answer for bonus 1")
print (add([[1, 9], [7, 3]], [[5, -4], [3, 3]], [[2, 3], [-3, 1]]))

print("And finally the desired error state for bonus 2\n\n")
print (add([[1, 9], [7, 3]], [[1, 2], [3]]))
