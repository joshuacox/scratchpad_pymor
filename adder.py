#!/usr/bin/env python
def my_adder(list1, list2):
    if len(list1) == len(list2):
        pass
    else:
        raise NameError('Unequal list length')
    added = list()
    for x in range (len(list1)):
        added.append( list1[x] + list2[x] )
    return added

def my_printer(listx):
    for x in range (len(listx)):
        print( listx[x])


def matrix_adder(listA, listB):
    if isinstance(listA, list):
      if isinstance(listB, list):
        if len(listA) == len(listB):
          pass
        else:
          raise NameError('Unequal list length')
      else:
        raise NameError('listB is not a list')
    else:
      raise NameError('listA is not a list')
    matrixadded = list()
    for x in range (len(listA)):
        matrixadded.append( my_adder(listA[x], listB[x]))
    return matrixadded

def matrix_printer(listx):
    my_printer(listx)

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

c = my_adder( a, b )
#my_printer(c)

matrix1 = [[1, -2], [-3, 4]]
matrix2 = [[2, -1], [0, -1]]

matrix3 = matrix_adder( matrix1, matrix2 )
#matrix_printer(matrix3)

print (matrix_adder( matrix1, matrix2 ))
