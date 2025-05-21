#write a python program and calculate the mean of the below dictionary.
#test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}

test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}
mean_value = sum(test_dict.values()) / len(test_dict)
print(mean_value)

#write a python script to concatenate the following dictionaries to create a new one.
#dict1 = {1: 10, 2: 20}
#dict2 = {3: 30, 4: 40}
#dict3 = {5: 50, 6: 60}

dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}
result = {**dict1, **dict2, **dict3}
print(result)

#write a python program to get the key,value and item in a dictionary.
#input:dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
for key, value in dict_num.items():
    print(key,value)
    
#write a python program to get the key,value and item in a dictionary.
#INPUT: input_dict={1:10,2:20,3:None,4:40,5:None,6:60}  

dict1={1:10,2:20,3:None,4:40,5:None,6:60}
for i,j in dict1.items():
    if j is None:
        dict1[i]=0
    print(i,dict1[i])
