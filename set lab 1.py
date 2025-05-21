#write a python program to get only unique items from two sets.
set1={10,20,30,40,50}
set2={30,40,50,60,70}
n=set1.union(set2)
print(n)

#write a python program to return a set of elements present in set A or B,but not both.
set1={10,20,30,40,50}
set2={30,40,50,60,70}
n=set1.symmetric_difference(set2)
print(n)

#write a python program to check if two sets have any elements in common.if ye,display the common elements.
set1={10,20,30,40,50}
set2={60,70,80,90,10}
n=set1.intersection(set2)
print(n)

#write a python proggram to remove itms from set1 that are not common to both set1 and set2.
set1={10,20,30,40,50}
set2={30,40,50,60,70}
n=set1.intersection_update(set2)
print(set1)
