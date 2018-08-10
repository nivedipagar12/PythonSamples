''' FizzBuzz
Author : Nivedita Pagar
Date : 10/08/2018
Task : A program that prints numbers from 1 to 100
       Exception : If the number is a multiple of 3, print "Fizz"
                   If the number is a multiple of 5, print "Buzz"
                   If the number is a multiple of 3 and 5, print "FizzBuzz"

Example: 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz...'''


def fizzbuzz():
    count = 1
    while(count <= 100):
        if count%3 == 0 and count%5 == 0:
            print("FizzBuzz")
        elif count%5 == 0:
            print("Buzz")
        elif count%3 == 0:
            print("Fizz")
        else:
            print(count)
        count += 1


fizzbuzz()
