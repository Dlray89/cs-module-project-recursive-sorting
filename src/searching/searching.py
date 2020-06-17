# TO-DO: Implement a recursive implementation of binary search

'''
binarySearch(arr, target, first, last)
        if first > last
            i want to return false
        else 
            set mid point = first + last / 2
                if target is equal to arr[midpoint]
                    return midpoint
                else if target < data[mid]
                    return binarySearch(arr, target, mid + 1, last)
                else
                return binarySearch(arr, target,last, mid - 1)

'''
def binary_search(arr, target, first, last):
    # Your code here
    if last >= first:
        midpoint = first + (last - first) // 2

        #if found at mid point then return
        if arr[midpoint] == target:
            return midpoint
        
        # search through the left
        elif arr[midpoint] > target:
            return binary_search(arr, target, first, midpoint - 1)
        # search through the right
        else:
            return binary_search(arr, target, midpoint + 1, last)

    else:
         return -1




# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
#     pass
    # Your code here

