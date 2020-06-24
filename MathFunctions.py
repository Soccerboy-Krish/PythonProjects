

#given a list of numbers
#loop through all of them to find out which one is even
#append the even ones to a list called even_list
#all the remaining ones have to be odd, as they are not even and add them to a list called odd_list
#add the items in both lists by looping through the numbers in the list and adding them to a sum variable
#return out the difference between the lists
#call the function by passing a list

def sums_odd_minus_sums_even(number_list):
	even_list = []
	odd_list = []
	for n in number_list:
		if n%2 == 0:
			even_list.append(n)
		else:
			odd_list.append(n)

	odd_sum = 0
	for odd_nums in odd_list:
		odd_sum = odd_sum + odd_nums

	even_sum = 0
	for even_nums in even_list:
		even_sum = even_sum + even_nums


	return odd_sum - even_sum

l2 = [3,5,7,8]
#print sums_odd_minus_sums_even(l2)

#given a number
#use the range function to make a factor_list between the numbers 2 and 1000
#loop through all factor_list and see if the given number divided by that number in factor_list is equivalent to 0
#if it is append to a list with all the factors of the number
#loop thorugh the list with all_factors
#if the number in all_factor gives a remainder (%), then append to odd_factors
#add the items in odd_list by looping through the numbers in the list and adding them to a sum variable
#make sure the sum variable is 1, becuase 1 is odd and a factor of all numbers
#why not use the range 1-1000?
#return the sum of the numbers in odd_list
#call the function by passing a number

def sum_odd_factors(given_number):
	if given_number == 0:
	 return 0
	factor1_list = range(1,1000,2)
	
	total_sum = 0
	for num in factor1_list:
		if given_number % num == 0:
				total_sum = total_sum + num
	
	return total_sum


#print sum_odd_factors(33)

#given two numbers
#we areusing the range function 1,1000, so any number in that rancge
#when divided from given number and produces a remainder of zero will append to a factor list
#using the sorted function, sort the list in desceding order
#loop thorugh the first list, then using a nested loop, loop through the other number's factors
#we do this to find the greatest common factor
#if a match is found store that in a variable called GCF 
#return the variable GCF 
#call the function by passing two integers

def GCF(num1, num2):
	list_of_factors = range(1,1000)
	num1_list = []
	num2_list = []
	for items in list_of_factors:
		if num1%items == 0:
			num1_list.append(items)
		if num2%items == 0:
			num2_list.append(items)

			sorted1 = sorted(num1_list, reverse = True)
			sorted2 = sorted(num2_list, reverse = True)

	for factor1 in sorted1:
		for factor2 in sorted2:
			if factor2 == factor1:
				return factor1

#print GCF (15,20)


#given a number
#make a list which uses the range 1,1000, so any number in that rancge
#when the given number is divided by produces a remainder of zero will append to a factor list
#to find the number of divisors, find the length of this factor list
#return even if the length is even, else return odd
#call the function by passing an integer


def count_of_divisors(num):
	all_factors = []
	factor_list = range(1,1000)
	for factor in factor_list:
		if num% factor == 0:
			all_factors.append(num)
	x = len(all_factors)
	if x%2 == 0:
		return "even"
	return "odd"

#print count_of_divisors(4)


def finding_average(given_list):
	total_sum = 0
	length = len(given_list)
	for items in given_list:
		 total_sum = total_sum + items
	average = total_sum/length
	return average

l2 = [1,2,3,4,5,6,7,8,9,10]
#print finding_average(l2)

class student:
  def __init__(self, name, age, ID):
    self.name = name
    self.age = age
    self.__id = ID

  def get_id(self):
  	return self.__id

  def info(self):
    print self.name
    print self.age

s3 = student("Jeff",6,475)
s1 = student("Krish", 14, 7563)
s2 = student("Amit", 13, 563)

s2.info()

print(s1.name)
s1.name = "kapil"
print(s1.name)
print(s2.age)
print(s2.get_id())
#print(Krish.ID)

