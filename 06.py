# -*- coding: utf-8 -*-
"""06.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hZBd8Xjmxst3JPBU5rBF4VUcXyhl8NIw
"""

listOne = [3, 6, 9, 12, 15, 18, 21] 
listTwo = [4, 8, 12, 16, 20, 24, 28]
listTree = []
list1 = []
list2 =[]
lenOne = len(listOne)
lenTwo = len(listTwo)

for i in range( 0, lenOne):
  if ( i%2 != 0):
    listTree.append(listOne[i])
    list1.append(listOne[i])

for i in range( 0, lenTwo):
  if ( i%2 == 0):
    listTree.append(listTwo[i])
    list2.append(listTwo[i])


print(f"Element at odd-index positions from list one: {list1}")
print(f"Element at even-index positions from list two: {list2}")
print(f"Printing Final third list : {listTree}")