# Problem 1:
# Create code and define the variable below outside of any function. After you create the list variable write a function called stupid_array_tricks that takes an array as a parameter, and performs the functions listed below in the instructions.
person_array = ["Kenn", "Kevin", "Erin", "Autumn"]
def stupid_array_tricks():
# person_array = ["Kenn", "Kevin", "Erin", "Autumn"]
# a) Print the 2nd and 3rd elements of the person_array using a range
    print(person_array[1:3])
# b) Print the last 2 elements of the person_array using a range
    print (person_array[2:4])
# c) Insert the new element Chuck between the 2nd (Kevin) and 3rd (Erin) elements
    person_array.insert(2, 'Chuck')
    print(person_array)
# d) Take out the 2nd element (Kevin) from the list
    person_array.pop(1)
    print(person_array)
stupid_array_tricks()

# Problem 2:
# We will keep having this problem until EVERYONE gets it right without help
# Create a function that has a loop that quits with ‘q’. If the user doesn't enter 'q', ask them to input another string.
def problem2():
    userInput = ""
    while(userInput != 'q'):
        userInput = input("Enter another string:  ")
problem2()

# Problem 3:
# Create a function that uses the data list below.
# ['GOOD_DATA',
# 'DECENT_DATA',
# 'BAD_DATA',
# 'DECENT_DATA',
# 'GOOD_DATA'
# 'BAD_DATA',
# 'GOOD_DATA',
# 'DECENT_DATA',
# 'BAD_DATA',
# 'GOOD_DATA']
# Write the code to do the following:
# Print the length of the original DATA list/array (ex. Starting length of data list is 10)
dumb_data_array =['GOOD_DATA',
                  'DECENT_DATA',
                  'BAD_DATA',
                  'DECENT_DATA',
                  'GOOD_DATA',
                  'BAD_DATA',
                  'GOOD_DATA',
                  'DECENT_DATA',
                  'BAD_DATA',
                  'GOOD_DATA']
print (len(dumb_data_array))
# Remove all BAD_DATA from the DATA list/array
# Print the length of the final DATA list/array (ex. Ending length of data list is 7)
dumb_data_array.remove('BAD_DATA') # !! : this only removes the fisrt instance of BAD_DATA
print(dumb_data_array)

# Problem 4:
# Use the following list of 5 numbers. score_list = [21,14,6,8,28,42,21]
# Write the code to do the following:
# Print the sum of the numbers (ex. The SUM of the numbers is 140)
# Print the maximum value from the numbers (ex. The MAX of the numbers is 140)
# Print the minimum value from the numbers (ex. The MIN value of the numbers is 6)
score_list = [21,14,6,8,28,42,21]
print(score_list) # !! : no need to print the array
print(sum('The SUM of the numbers is '{score_list})) # !! : f'string {variable} string {variable}'
print(max('The MAX value of the numbers is '{score_list})) # !! : max(myArray) min(myArray) sum(myArray)
print(min('The MIN value of the numbers is 6'{score_list}))
score_list() # !! : score_list is not a function 
