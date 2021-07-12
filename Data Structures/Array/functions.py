# import array for array operations
import array
import sys

# initializing array with array values
# initializes array with signed integers

# 1. array(data type, value list)
arr = array.array('i', [1,2,3,4])

print('Size:', sys.getsizeof(arr))

# printing created array
def print_array(arr, txt):
    print(txt , end=' ')
    for i in range(len(arr)):
        print(arr[i], end=' ')
    print('\r')

print_array(arr, 'The created array is: ')

# 2. append():- This funtion is used to add the value mentioned in its argument at the end of the array.
arr.append(5)
print_array(arr, 'Array after append 5: ')

# 3. insert(i, x):- This function is used to add value(x) at the ith position specified in its argument.
arr.insert(5, 6)
print_array(arr,'Array after insert 6 at 5th position: ')

# 4. pop():- This function removes the element at the position mentioned in its argument and returns it.
arr.pop(5)
print_array(arr, 'Array after pop the 5th position element: ')

# 5. remove():- This function is used to remove the first occurance of the value mentioned in its argument.
arr.remove(5)
print_array(arr, 'Array after remove first occurance of 5: ')

# 6.reverse():- This function reverse the array.
arr.reverse()
print_array(arr, 'Array after reversing the array: ')

# 7. index():- This function returns ths index of the first occurance of value mentioned in argument.
print('index of first occurance of element 3: ', arr.index(3))

print('')

# 8. typecode :- This function returns the datatype by which array is initialized.
print('The datatype of array is: ', end='')
print(arr.typecode)

# 9. itemsize :- This function returns size in bytes of a single array element.
print('Itensize of array is: ', end='')
print(arr.itemsize)

# 10. buffer_info():- Returns a tuple representing the address in which array is stored and number of elements in it.
print('The buffer info of array is: ', end='')
print(arr.buffer_info())

# 11. count():- This function counts the number of occurances of argument mentioned in array.
print('The number of occurance of 1 in array is: ', end='')
print(arr.count(1))

# 12. extended(arr):- This function appends the whole array mentioned in its arguments ti the specified array.
arr1 = array.array('i', [10,11,12])
arr.extend(arr1)
print_array(arr, 'The array after extending with arr1: ')

# 13. fromlist(list):- This function is to append a list mentioned in its argument to end of array.
lst = [13,14,15]
arr.fromlist(lst)
print_array(arr, 'The array after appending the list to the array: ')

# 14. tolist():- This function is used to transform as array into a list.
lis = arr.tolist()
print('The list from the array is: ', lis)
