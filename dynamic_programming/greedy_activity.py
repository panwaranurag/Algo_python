#!/usr/local/bin/python2.7

from random import randint
import sys

def greedy_activity(start, finish, n_element):
  final = []
  final.append(1)
  k = 0
  for j in range(1,n_element):
    if start[j] >= finish[k]:
      final.append(start[j])
      k = j
  return final

if __name__ == "__main__" and len(sys.argv) != 2:
  print "must have 1 number arguments"

if __name__ == "__main__" and len(sys.argv) == 2:
  n_element = int(sys.argv[1])
  start = []
  finish = []
  print n_element
  for i in range(n_element):
    i = randint(0,20)
    j = randint(0,20)
    if i < j:
      start.append(i)
      finish.append(j)
    else:
      start.append(j)
      finish.append(i)
  start.sort()
  finish.sort()
  print start
  print finish
  print "Greedy activity selection is as follow", greedy_activity(start, finish, n_element)
