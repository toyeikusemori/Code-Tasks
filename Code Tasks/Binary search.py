valuelist=[1,2,3,4,5,6,7,8,9,10] ## sorted list of numbers to be searched
searchvalue=int(input("Search for a value")) ## user input to search for a value in the list
midnum=0 ##intialise middle number variable. To be used to identify middle number in the list
def getlength(valuelist): ## function to get the length of the list and return it to the call
        lenvaluelist=len(valuelist)
        return lenvaluelist

def getmid(valuelist): ##function to find the middle number in the list. Assigned to midnum
        lenvaluelist=getlength(valuelist)
        midnum=lenvaluelist//2
        if lenvaluelist==3: ## since the division rounds up to 2 midnum has to be set to 1 to represent the middle number
                midnum=1
        return midnum
    
def BINARY_SEARCH(valuelist,searchvalue):## Binary search function defined using the list of numbers and the number to be searched
    lenvaluelist=getlength(valuelist) ## assigns the length of the list to this variable
    midnum=getmid(valuelist) ## assigns the index of the middle number in the list to midnum
    midnum=midnum-1 ## alligns the number to the way python indexes(from 0 instead of 1)
    
    while searchvalue!=valuelist[midnum]: ##searches the list if the number has not been found.
        if lenvaluelist > 1: ##only searches if the length of the list is bigger than 1 
                
            if searchvalue > valuelist[midnum]: ##if the search value is bigger than the middle number, search from the middle number to the end of the list
                valuelist=valuelist[midnum:] ## replaces the old list with the numbers from the middle to the end of the list
                lenvaluelist=getlength(valuelist)##retrives the new length of the list
                print(valuelist)##shows the current state of the list to the user
                midnum=getmid(valuelist)## Retrieves the middle number's index in the new list
        
            else:
                valuelist=valuelist[0:midnum]##search from 0 to the middle number if the search value is less than the middle number
                lenvaluelist=getlength(valuelist)
                print(valuelist)
                midnum=getmid(valuelist)        
        else:
            if searchvalue!=valuelist[midnum]:## since the list only has 1 value and that is not the search value, the number is not there
                 return("Number is not in list")##Message to show the value cannot be found
        
        
    return("Number is in list")##Message to show the value is in the list

     
    
print(BINARY_SEARCH(valuelist,searchvalue))##Calls the function and displays the result
