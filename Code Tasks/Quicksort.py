unsorted=[5,9,6,7,8] ##array to be sorted
print("This is the unsorted list: "+ str(unsorted)) ##display the list to be sorted
def findmiddle(unsorted): ##function to find the middle value in the list
    length=len(unsorted) #get the current length of the list
    total=0 #intialise total used to calculate the total of the items in the list
    j=0#used to iterate through the list to find the middle value's index
    i=0#used to iterate through the list to calculate the total
    
    for i in range(0,length):#iterate through the numbers in the list and add them to the total
        total=total+unsorted[i]
    middle=total//length #calculate the median/middle value of the list. divide the total by the amount of numbers in the list

    for j in range(0,length): # iterate through the list and return the index of the median
        if middle == unsorted[j]:
            return j 

   
        
            
def quicksort(unsorted): ##intialise the quicksort function using the array to be sorted
    
    smaller = []##list for the numbers smaller than the pivot
    larger = []##list for the numbers larger than the pivot
    equal = [] ## list for numbers equal to the pivot
   
    if unsorted==[]: ##return the empty list to stop the algorithm is theres no more numbers to sort
        return []

    
    middleval=findmiddle(unsorted)##calculate middle value to be used as the pivot
    pivot = unsorted[middleval] #find the middle value and assign it as the pivot
    print("Pivot is : " + str(pivot)) #present the pivot number to the user

    for x in unsorted:  ## iterate through the array of numbers
        if x < pivot:  ## if the current number is less than the pivot append it to the smaller list
            smaller.append(x)
        if x==pivot: #if the current number is equal to the pivot append it to the equal list
            equal.append(x) 
        if x > pivot:## if the current number is bigger than the pivot append it to the larger list
            larger.append(x)
        
    return quicksort(smaller)+equal+quicksort(larger) ##return the result and recurse with the smaller and larger list

print(quicksort(unsorted))  ##call and display the result of the quicksort using the unosorted array
