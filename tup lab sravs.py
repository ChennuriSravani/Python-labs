#Write a python program to find the number of times 4 appears in the tuple.
#Input:tuplex(2,4,5,6,2,3,4,4,7)
tuple = (2,4,5,6,2,3,4,4,7)
print(tuple.count(4))

#Write a python program to convert a list to a tuple.
#Input:listx=[5,10,7,4,15,3]
list1=[5,10,7,4,15,3]
tup=tuple(list1)
print(tup)

#Write a python program to calculate the sum of the numbers in a given tuple.
#Input tuples_list = [(1, 2), (3, 4), (5, 6)]
tuples_list = [(1, 2), (3, 4), (5, 6)]
total = sum(sum(t) for t in tuples_list)
print(total)


#Write a python program and Iterate the given tuples.
#Input employee1 = ("John Doe", 101, "Human Resources", 60000)
#employee2 = ("Alice Smith", 102, "Marketing", 55000)
#employee3 = ("Bob Johnson", 103, "Engineering",75000) 
employee1 = ("John Doe", 101, "Human Resources", 60000)
employee2 = ("Alice Smith", 102, "Marketing", 55000)
employee3 = ("Bob Johnson", 103, "Engineering",75000)
list1=[employee1,employee2,employee3]
for emp in list1:
    name,id,dep,salary=emp
    print("name:",name,"id: ",id," Department:",dep,"salary",salary)
