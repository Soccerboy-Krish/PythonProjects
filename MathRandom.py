#Write a Python function to find the Max of three numbers.

def max_number(a,b,c):
	if a > b and a > c:
		print ("a is the greatest")
	elif b > a and b > c:
		print ("b is the greatest")
	else:
		print ("c is the greatest")

max_number(1,43,34)


#Write a Python program to get the volume of a sphere with radius 6.

def volume_sphere(r):
	a = 4/3*(3.14)*r**3
	print a

volume_sphere(6)

#Write a Python program that will accept the base and height of a triangle and compute the area. 

base = input("Please enter a base for the triangle:")
height = input("Please enter a height for the triangle:")

def area_triangle(base,height):
	area = float(0.5*base*height)
	return area


print int(area_triangle(base,height))



#check leap year


Year = input("Enter a year to see if it is a leap year:")


if Year%4 == 0:
	print("A Leap Year. Yay!!")
else:
	print("Not a leap year!")




#10 % of marks scored from submission of Assignments
#70 % of marks scored from Test
#20 % of marks scored in Lab-Works

#1. score >= 90 : "A"
#2. score >= 80 : "B"
#3. score >= 70 : "C"
#4. score >= 60 : "D"


#calculate students average, student letter grade class average, and class letter grade



#Jack's dictionary 
jack = { "name":"Jack Frost", 
         "assignment" : [80, 50, 40, 20], 
         "test" : [75, 75], 
         "lab" : [78.20, 77.20] 
       } 

jack_assignment_list =  jack.get("assignment")

jack_assignment_total = 0
for grades in jack_assignment_list:
	jack_assignment_total = jack_assignment_total + grades


jack_final_assignments = jack_assignment_total/len(jack_assignment_list)*0.1



jack_test_list = jack.get("test")

jack_test_total = 0
for grades in jack_test_list:
	jack_test_total = jack_test_total + grades


jack_final_test = jack_test_total/len(jack_test_list)*0.7



jack_lab_list = jack.get("lab")

jack_lab_total = 0
for grades in jack_lab_list:
	jack_lab_total = jack_lab_total + grades


jack_final_lab = jack_lab_total/len(jack_lab_list)*0.2


jack_final_grade = jack_final_lab + jack_final_test + jack_final_assignments

print jack_final_grade

if jack_final_grade >= 90:
	print "Jack's final grade is A"
elif jack_final_grade >= 80:
	print "Jack's final grade is B"
elif jack_final_grade >= 70:
	print "Jack's final grade is C"
elif jack_final_grade >= 60:
	print "Jack's final grade is D"
else:
	print "Jack's final grade is F" 


#program to find the square root


number_you_want = input("Please enter a number to find the square root of:")


def square_root(number_you_want):
	square_root = number_you_want**0.5
	return square_root

print square_root(number_you_want)


number_x = input("Please enter a number to find the cube root of:")
def cube_root(number_x):
	cube_root = (number_x**0.333333333)
	return cube_root

print cube_root(number_x)

#convert celsius to fahrenheit

def convert_temp(celsius_degree):
	fahrenheit = (celsius_degree * 1.8) + 32 
	return fahrenheit

print convert_temp (42)


from numpy import random
xm = random.randint(100)
print (xm)



#Python program to print negative numbers in a list


def negative_numbers(given_list):
	for nums in given_list:
		if nums < 0:
			print nums


my_list = [-3,12,123,4123,-592,-34]
print negative_numbers(my_list)


