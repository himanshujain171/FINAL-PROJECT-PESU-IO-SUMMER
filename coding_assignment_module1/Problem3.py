numbers=[int(i) for i in input("Enter numbers seperated by space = ").split()]
key=int(input("Enter the number to search = "))

def binary_search(num,low,high,key):
    if low<=high:
        mid=(low+high)//2
        if num[mid] == key:
            return mid
        elif num[mid]>key:
            return binary_search(num,low,mid-1,key)
        else:
           return binary_search(num,mid+1,high,key)
    else:
        return -1
index=binary_search(numbers,0,len(numbers)-1,key)
if(index!=-1): print(key,"found at index",index)
else :print(key,"not found")
