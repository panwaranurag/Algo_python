#!/usr/local/bin/python2.7

from random import randint
import sys

if __name__ == "__main__" and len(sys.argv) != 3:
  print "must have 2 number arguments"

if __name__ == "__main__" and len(sys.argv) == 3:
  numInputLists = int(sys.argv[1])
  inputListLen = int(sys.argv[2])
  inputLists = []
  '''inputLists.append([1,2,3,4,5,6,7,8,9,10])
  inputLists.append([11,12,13,14,15,16,17,18,19,20])
  inputLists.append([21,22,23,24,25,26,27,28,29,30])
  '''
  
  for i in range(numInputLists):
    inputLists.append([])
    for j in range(inputListLen):
      inputLists[i].append(randint(0,100))
    inputLists[i].sort()  
  numInputLists = len(inputLists)
  inputListLen = len(inputLists[0])
  solutionLen = numInputLists * inputListLen // 2
  
  print "Solution length will be:",solutionLen
  print
  print("Generated Input Lists:")
  for inputList in inputLists: print inputList
  print
  
  allInput = []
  for inputL in inputLists:
    allInput.extend(inputL)
  longSolution = sorted(allInput)[-solutionLen:]
  
  
  solution = []
  base = []
  while len(solution) < solutionLen:
    # remove empty inputLists:
    while [] in inputLists:
      inputLists.remove([])
    
      
    solLeft = solutionLen - len(solution)
    partIndex = solLeft // len(inputLists)
    partIndex = max(partIndex, 1)
    
    minParts, maxParts = [], []
    for inputList in inputLists:
      if len(inputList) <= partIndex:
        minParts.append(inputList[-1])
        maxParts.append(inputList[0])
      else:
        minParts.append(inputList[partIndex-1])
        maxParts.append(inputList[-partIndex])
    
    print "partition Lists:", 
    print minParts, " and ", maxParts
    
    minListIndex = minParts.index(min(minParts))
    maxListIndex = maxParts.index(max(maxParts))
    
    toAdd = inputLists[maxListIndex][-partIndex:]
    solution.extend(toAdd)
    
    inputLists[minListIndex] = inputLists[minListIndex][partIndex:]
    inputLists[maxListIndex] = inputLists[maxListIndex][:-partIndex]
    
    print "inputLists are now:"
    for inputList in inputLists: print inputList
    print "Added:", toAdd
    print "Solution:", solution
    print
    
  solution.sort()
  print "My Solution:"
  print solution
  print
  print "Long Solution:"
  print longSolution
  print
  
  works = True
  
  if len(solution) != len(longSolution):
    works = False
  else:
    for i in range(len(solution)):
      if solution[i] != longSolution[i]:
        works = False
        break
      
  if works:
    print "IT WORKS!!!!"
  else:
    print "FAILFAILFAILFAILFAILFAILFAILFAILFAIL"