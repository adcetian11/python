#List
List=[1,2,'third',5,8,'box']
print(List)
print(List[1])
print(List[-2])
print(len(List))
List.append(6)
List.append(8)
print(List)
List.insert(4,"paper")
print(List)
List.reverse()
print(List)
List.remove(2)
print(List)
List.pop()
print(List)
sliced_list=List[4:]
print(sliced_list)
print("---------------------------------------------------")
#Tuple
tuple1=(1,2,3,4,5,5,"pen")
tuple2=(7,78,4)
print(tuple1)
#print(cmp(tuple1,tuple2))
print(len(tuple1))
print(max(tuple2))
print(min(tuple2))
print(tuple1.count(5))
print(tuple1)
print("---------------------------------------------------")
#Dictionary
dict1={ 1:"one",2:"two",3:"three",4:"four"}
print(dict1.get(1))
print(dict1.keys())
print(dict1.values())
print(dict1.pop(2))
print(dict1)
print("---------------------------------------------------")
#sets
sets1={1,2,3,4,5,7}
sets2={6,7,8,9,10,4,2}
print(sets1)
print(sets2)
print(sets1.union(sets2))
print(sets1.intersection(sets2))
print(sets1.difference(sets2))
sets1.add(11)
print(sets1)
print(sets1.isdisjoint(sets2))
sets1.clear()
print(sets1)
print("---------------------------------------------------")