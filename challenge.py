#The provided code stub reads two integers,  and , from STDIN.

#Add logic to print two lines. The first line should contain the result of integer division, a // b. The second line should contain the result of float division, a / b.

#No rounding or formatting is necessary.
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c=a//b
    d=a/b
    print(c)
    print(d)

    #The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

#The first line contains the sum of the two numbers.
#The second line contains the difference of the two numbers (first - second).
#The third line contains the product of the two numbers.
f __name__ == '__main__':
    a = int(input())
    b = int(input())
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)

    
    #The provided code stub reads and integer, , from STDIN. For all non-negative integers , print .
#Example
#The list of non-negative integers that are less than  is . Print the square of each number on a separate line.
if __name__ == '__main__':
    n = int(input())
    i=0
    while(i<n):
        print(i*i)
        i+=1
   #anothermethod
if __name__ == '__main__':
    n = int(input())
    for i in range(0,n):
        print(i*i)
        
#(4)Sample Input 0
#3
#Sample Output 0
#123

if __name__ == '__main__':
    n = int(input())
    for i in range(1,4):
        print(i,end="")
#anothermethod(4)
if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i,end="")

        #(5)Task 
#Given an integer, , perform the following conditional actions:

#If n is odd, print Weird
#If n is even and in the inclusive range of 2 to 5, print Not Weird
#If n is even and in the inclusive range of  6to 20, print Weird
I#f n is even and greater than 20, print Not Weird

if(n%2!=0):
    print("Weird")
else:
    if(n in range(2,6)):
        print("Not Weird")
    elif(n in range(6,21)):
        print("Weird")
    else:
        print("Not Weird")
