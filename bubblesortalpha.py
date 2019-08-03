
#Creating list of alphabets
list =['q','w','e','r','t','y','g','h','j','k','l','u','i','o','p','a','s','d','f','g','h','m','n','b','c','x','z','v']
print ("initial List :", list) #print initial list (unsorted)
#creating function of Bubble sort
def bubbleSort(list): #list ko dalo argument me
    l = len(list) # list ki lenght ka pata karo or print karewao list ki lenght ko 
    print ('lenght of list : ', l) 
    for i in range(0, l-1): #for loop 0 se le kar lenght of list se 1 kam (to know how much time loop will run)
         for j in range(l-1-i): # for loop to get value of 1 and 2 element to compare 
             if list[j] > list[j+1]: # comaprision
                 temp = list[j] #swapping of 2nd element to left if its bigger (swapping via third variable)
                 list[j] = list[j+1]
                 list[j+1] = temp
#calling function 
bubbleSort(list)
#ye for loop chalane pr lenght of list (28 ) 28 bar output ara hai ko ki same hi hai  isily doc string bana dia 
'''for i in range(len(list)):'''
#print sorted list 
print ('Sorted list : ', list)


#Task Completed
