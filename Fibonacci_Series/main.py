'''Title : Generate Fibonacci Series
   Author : Nivedita Pagar
   Date : 09/04/2018
   Details : The code asks the user to provide the number of fibonacci numbers to be generated and generates a list
             of the provided length
             Fibonacci series : [1, 1, 2, 3, 5, 8, 13, .....] .. where each element is the addition of the two previous
             elements'''

def fibonacci():
    num = int(input('Enter the number of fibonacci numbers you want to generate : '))   # Ask the user
    mylist = [1,1]  # Give the first two elements to start
    counter = 0
    index = 0
    while counter <= num:
        sum = mylist[index] + mylist[index+1]   # Add the first two elements in the list
        mylist.append(sum)  # Add the sum to the end of the list
        counter += 1
        index += 1  # Go to the next element
    print(mylist)
fibonacci()
