# Linear Search algorithm

def linear_search(list,item):
    i=0
    found=False
    while i<len(list):
        if list[i]==item:
            found=True
            break
        else:
            i=i+1
    return found

print(linear_search([1,2,3,4,5,6],7))