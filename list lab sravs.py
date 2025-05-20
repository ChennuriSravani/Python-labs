#Write a python program to sum all the items in the list.
list=[10,20,30,40,50]
sum=0
for i in list:
    sum+=i
print(sum)

#Write a python program to get the largest and smallest number from a list without builtin functions.
list=[10,20,30,40,50]
maximum=minimum=list[0]
for n in list[1:]:
    if n>maximum:
        maximum=n
    if n<minimum:
        minimum=n
print("Largest:",maximum)
print("Smallest:",minimum)

#Write a python program to find the duplicate values from a list and display those. 
list=[1,2,3,4,5,5,7,8,7]
unique=[]
duplicate=[]
for n in list:
    if n in unique and n not in duplicate:
        duplicate.append(n)
    else:
        unique.append(n)
print(duplicate)

#write a python program to split a given list into two parts where the length of the first part of the list is given.
#original list [1,1,2,3,4,4,5,1]
#length of the first part of the list:3
#splitted the said list into two parts
#([1,1,2),(3,4,4,5,1])
list=[1,1,2,3,4,4,5,1]
split=3
part1=list[:split]
part2=list[split:]
print("Part1:",part1)
print("Part2:",part2)

#write a python program to traverse a given list in reverse order,and print the output.
list=[10,20,30,40,50]
for list2 in reversed(list):
    print(list2)
