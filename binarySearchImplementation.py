#binary search Implementation in python
'''
it is simple  binary search and used to search a number position in given
sorted list

first list is sorted and then it do binary serch of given number position

break the sorted list in two half from index let say mid
first calculate mid
   
(start + end )/ 2 (start is 0 and end is n-1)

now if your key element is equal to mid = return mid position
unless
serch it on Start to mid -1 (if key is smaller them mid )
and serch it on mid+1 to end ( if key is greater then mid )

thats it

'''

#codes

 
def binary_sort(sorted_list, length, key):
    start = 0
    end = length-1
    while start <= end:
        mid = int((start + end)/2)
        if key == sorted_list[mid]:
            print("\nEntered number %d is present at position: %d" % (key, mid))
            return -1
        elif key < sorted_list[mid]:
            end = mid - 1
        elif key > sorted_list[mid]:
            start = mid + 1
    print("\nElement not found!")
    return -1
 
lst = []
 
size = int(input("Enter size of list: \t"))
 
for n in range(size):
    numbers = int(input("Enter any number: \t"))
    lst.append(numbers)
 
lst.sort()
print('\n\nThe list will be sorted, the sorted list is:', lst)
 
x = int(input("\nEnter the number to search: "))
 
binary_sort(lst, size, x)
