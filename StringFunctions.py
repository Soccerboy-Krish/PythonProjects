#given a string

#we move -1 space each time
#we will start at the end and end at position zero
#call the function by passign a string to reverse

def print_reversed(x):
  return x[::-1]

reversing = print_reversed("Hippo Rastogi")

#print(reversing)


#given three strings
#we want to print out only docs.google.com
#not https://docs.google.com/krish
#the first one is the big string
#using the find index we name index1 which will be zero, because a match will be found right away
#then, index2 would be where / is present but we want the one after docs.google.com, 
#so we add the len(str2) so that will be where the find method starts its search
#now, we have found the starting index of what we have to find
#index two is where the / is so we slice str1 from start index: index2 and return this
#finally, we call the function by passing three strings


def string_slicing(str1,str2,str3):
	index1 = str1.find(str2)
	index2 = str1.find(str3,index1+len(str2))
	startIndex = index1+len(str2)

	return str1[startIndex:index2]

#print string_slicing("https://c/krish", "https://", "/")	



#given a string
#we find the index of the "@" symbol using the find method
#we want the username of the person
#so we slice from the beginning to the @ symbol and store this slice in a variable called username
#we return the username 
#we call the function by passing a string


def email_checker(str9):
	index = x.find("@")
	username = x[:index]
	return username

#print email_checker("krish12313123@nothing.com")



#given a string
#we predifine a set of vowels cointaing the five vowels
#we will loop through weach element of the string
#and see if any of the characters in the string is in vowels
#we do this for every character in the given string so that we don't just stop at the first vowel we see
#then we make a variable called total_vowels and if a character in the word is in vowels we incrememnt total vowels
#we return total vowels
#finally, we call the function by passing a tring

def vowels_in_string(word_to_check):
	total_vowels = 0
	vowels = "aeiou"
	
	for letter in word_to_check:
		if letter in vowels:
				total_vowels = total_vowels + 1

	return total_vowels
	

#print vowels_in_string("rastogi")
#print vowels_in_string("aeifoo")


#given a string
#we assign the leftmost and rightmost indexes
#we use a while loop to say while the left index is less than the right index
#which will be all the time unless the right index meets the left index in which that part of the string has been checked by the other index
#if the character leftmost index does not equal the character rightmost index, then return false right away
#Because the first and last letter must be the same for it to be a palindrome
#However, if this is not the case, keep going and incrememnt the indexes 
#so next time they go thorugh the loop the do it for the second letter and second to last latter
#outside the loop, if you have not returned false, then you will return true
#call the function by passing a string or number
#you will return True if it is a palidrome and False if not


def check_palindrome(string1):
	left=0
	right=len(string1)-1

	while left<right:
		if string1[left] != string1[right]:
			return False
		left=left+1
		right=right-1
	return True

				
#print check_palindrome("abc")
#print check_palindrome("abba")



#given a string 
#make an empty list which will store the even length words from the string
#define the being index - beg
#use while true loop
#and define end to start the search from beg [0] and find all the spaces from then on
#now the word will be from [beg:end] because end is where the space is and beg is 0, where the slice started
#if end == -1 then break, becuae you have reached the last index
#should you use len(str) - 1, instead? does it matter?
#to make sure you slice all the words, you have to make beg = end + 1
#this is beccuae right now, end is wehre the space is at and beg is 0
#if beg = end + 1, beg will be the start of the new word, and end will find the space after the new word has began
#otherwise, the find method will just keep finding the fist space it sees
#now, if any of the words length (use len function) when divided by two leaves no remainder
#it should be append to an even word list
#return even_list as it will have all the even length words
#finally, call the function by passing a string. would passing a list also work?
#you will return all even length words in a string except for the last one


def even_length_words(given_string):
	
		even_list = []	
		beg = 0
		while True:
			end = given_string.find(" ", beg)
			if end == - 1:
				break
			word = given_string[beg:end]
			if len(word)%2 == 0:
				even_list.append(word)
			beg = end+1
			
		return even_list

#print even_length_words("I am a case casa")



def using_split(str5):
	split_list = []
	splited = str5.split('i')
	for word1 in splited:
		split_list.append(word1)
	return split_list	

#print using_split("Hellio my niame is krish aibc def ghi")



#given a string and a separator, telling us wehre to separate the string from.
#make an word list which will be the splited version of the string
#define the being index - beg (0)
#use while true loop
#and define end to start the search from beg [0] and find the first separator from there
#but if end == -1, then break out of the loop
#now, slice the word from index 0 to where right before the separator
#now the word will be from [beg:end] because end is where the separator is and beg is 0, where the slice started
#append all the words you have found to a list, you now have the splited version
#to make sure you slice all the words, you have to make beg = end + 1
#this is beccuae right now, end is wehre the space is at and beg is 0
#if beg = end + 1, beg will be the start of the new word, and end will find the space after the new word has began
#otherwise, the find method will just keep finding the fist space it sees
#finally, return word_list
#you have created a user defined function which does the same task, as the built in fucntion, split.


def my_split(string2, separator):
	
		beg = 0
		word_list = []
		while True:
			end = string2.find(separator, beg)
			if end == -1:
				break
			word = string2[beg:end]
			word_list.append(word)
			beg = end+1
			
		return word_list

#print my_split("Hellio my niame is krish aibc def ghi","i")




