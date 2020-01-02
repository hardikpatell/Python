# Binary Search algorithm to find value in list
def binary_seaarch( list,item):
    first=0
    last=len(list)-1
    found=False
    
    while(first<=last and not found):
        mid=(first+last)//2
        if list[mid] == item:
            found =True
        else:
            if item<list[mid]:
                last=mid-1
            else:
                first=mid+1
    return found
found = binary_seaarch([1,2,3,4,5,6],5)
if found==True:
    print("Number is found")
else:
    print("Number is not there")

        
