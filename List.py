#Write a Python function that takes two lists and returns True if they have at least one common member. 

fruits = ["apple", "banana", "cherry"]
number_list = [1, 2, 4, "cherry"]


for x in fruits:
	for z in number_list:
		if x == z:
			print ("True")


#Write a Python program to print the numbers of a specified list after removing even numbers from it. 

num_list = [1,2,3,4,5,6,7,8,9,10,11]

even_list = []

for numbers in num_list:


	if numbers%2 == 0:
		even_list.append(numbers)

print even_list


random_list = [12,809]

x = random_list[1]
random_list[1] = 122

print random_list

#function to multiply all items in a list

mylist = [1,2,3,4,5]

def multiply_list(x):
	answer = 1
	for objects in x:
		answer = answer*objects
	return answer
		

print multiply_list(mylist)


#Python program to find smallest number in a list
the_list = [3412,123423,7,8,9,24,5,2345]
x = min(the_list)
print x
y = max(the_list)
print y 




my_list = [1,3,5,2,11,4,34]

print sorted(my_list, reverse = True)

