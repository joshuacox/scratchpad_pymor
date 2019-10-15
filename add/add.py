#!/usr/bin/env python
def my_adder(list1, list2):
    if len(list1) == len(list2):
        pass
    else:
        raise ValueError("Given matrices are not the same size.")
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
          raise ValueError("Given matrices are not the same size.")
      else:
        raise NameError('listB is not a list')
    else:
      raise NameError('listA is not a list')
    matrixadded = list()
    for x in range (len(listA)):
        matrixadded.append( my_adder(listA[x], listB[x]))
    return matrixadded

def add(*args):
    resultmatrix = list()
    for x in range (len(args)):
        if x == 0:
          resultmatrix = args[x]
        else:
          resultmatrix = matrix_adder(resultmatrix, args[x])
        #print (resultmatrix)
    return resultmatrix

def matrix_printer(listx):
    my_printer(listx)
