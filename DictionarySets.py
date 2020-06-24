#dictionaries

test = {"key1" : "value1", "key2" : "value2", "key3" : "value3"}

#prints all keys one by one
for x in test:
	print x

#prints all values one by one
for x in test.values():
	print x 

#prints through all values without using the values function
for y in test:
	print (test[y])

#prints the number of key-value pairs  (length of dictionary)
print len(test)

#update function changes the dictionary
test.update({"key4" : "value4"})

print test

#prints the key-value in paris (tuple form) --> easy to read
for x,y in test.items():
	print (x,y)

#assign a new key to a specific value (same as update?)
test["key5"] = "value5"

print test


#how to add dictionaries?



my_dict = {} 
  
#Insert composite key
x, y, z = 10, 20, 30
my_dict[x, y, z] = x + y - z; 

print my_dict 


name_grade_dict = {}

def name_grade(name, grade):
	for x in name:
		for y in grade:
			name_grade_dict.update({name:grade})


name_grade("Krish", "A")
name_grade("Anvi", "A+")
name_grade("Hippo", "C+")

print name_grade_dict



#create a set
my_set = {"apple", "banana", "cherry"}
other_set = {"apple","banana", 10, 3923.1, False, 10, 10, 10, 10, 10, 10}
other_set.add("orange")
print(my_set)
print(other_set)

print my_set.intersection(other_set)
print my_set.union(other_set)

