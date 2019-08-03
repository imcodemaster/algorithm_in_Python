#interpolation search
#creating function give parameter arr, x, n
#array for array
#x = element going to found
# n is a size of array

#funda
#interpolation is doe in a array which is uniformily distributed
#to get the position of founding element with formula
#if uniformity is distured no of step will increase and time complexity will
#also effected far bettter than binary search in uniformily distrubuted array to search '''
#set lower pointer
#set higher pointer     
#checking basic condition
#lower pointer should be lower than higher pointer
#x is should be greater than lower pointer
#and x is also be a smaller than a higher pointer
#but

#if lower == higher
#so compare the x value with lower one
    #if founded similiar than return value of x ulesss go to find the position


#explanation of geeting position        
#getting position
        #position is calculated by given formula
'''
 l + x - arr[l] * h - l / arr[h] - arr[l]
 coe below :
'''
#if position is get the element 
# unless if x is smaller than pos : - search in lower bound 
#unless if x isgreater than pos than found in higher bound
    
def InterpolationSearch (arr, x, n):
    l = 0
    h = n-1
    while l <= h and x >= arr[l] and x<= arr[h] :
        if l == h:
            if x == arr[l]:
                print ('at index ' , l)
            return -1
        pos = l + int(((float(h - l)  / (arr[h] - arr[l])) * (x - arr[l])))
        if arr[pos] == x :
            print('at index : ', pos)
        if arr[pos] < x :
            h = pos - 1    
        else :
            l = pos + 1

    return -1

        #driver code

arr = [1,2,3,4,5,6,7,8,9]
n = len(arr)
x = 9
index = InterpolationSearch (arr, x, n )









            


        
        
        
