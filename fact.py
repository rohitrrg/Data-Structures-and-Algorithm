def fact(n):
    count = 1
    while n!=0:
        count = count*n
        n= n-1
    return count

n = int(input('Enter any number: '))
print('The factorial of {} is {}'.format(n, fact(n)))