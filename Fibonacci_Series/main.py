'''Title : Generate Fibonacci Series
   Author : Nivedita Pagar
   Date : 09/04/2018
   Details : The code asks the user to provide the number of fibonacci numbers to be generated and generates a list
             of the provided length
             Fibonacci series : [1, 1, 2, 3, 5, 8, 13, .....] .. where each element is the addition of the two previous
             elements'''

def fibonacci(num):
    global a, b, sequence
    sequence.append(a)
    sequence.append(b)
    for i in range(1, num-1):
        temp = a + b
        sequence.append(temp)
        a = b
        b = temp
    return sequence

number = int(input("How many numbers do you want in your fibonacci sequence ? : "))
sequence = []
a = 1
b = 1
if number == 0:
    pass
elif number == 1:
    sequence.append(a)
elif number == 2:
    sequence.append(a)
    sequence.append(b)
else:
    fibonacci(number)
