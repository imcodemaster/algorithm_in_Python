
#Creating list of alphabets
list =['q','w','e','r','t','y','g','h','j','k','l','u','i','o','p','a','s','d','f','g','h','m','n','b','c','x','z','v']
print ("initial List :", list) #print initial list (unsorted)
#creating function of Bubble sort
def bubbleSort(list): 
    l = len(list)  
    print ('lenght of list : ', l) 
    for i in range(0, l-1): 
         for j in range(l-1-i): # for loop to get value of 1 and 2 element to compare 
             if list[j] > list[j+1]: # comaprision
                 temp = list[j] #swapping of 2nd element to left if its bigger (swapping via third variable)
                 list[j] = list[j+1]
                 list[j+1] = temp
#calling function 
bubbleSort(list)
'''for i in range(len(list)):'''
#print sorted list 
print ('Sorted list : ', list)


#Task Completed
