# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arr, arrA, midArr, arrB):
    pass
    # leftArr = midArr - arrA + 1
    # rightArr = arrB - midArr

    # for i in range(len(leftArr)):
    #     leftArr[i] = arr[arrA + i]
    # for j in range(len(rightArr)):
    #     rightArr[j] = arr[midArr + 1, j]

    #     while i < leftArr and rightArr:
    #         if leftArr[i] <= rightArr[j]: 
    #             return arr 


    # Your code here


    # return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        #creat a  main is point where this arr is divided into subarrays
        mainArr = len(arr) / 2
        # set up left side subarr1
        LeftArr = arr[:int(mainArr)]
        # set up right side subarr2
        righArr = arr[int(mainArr):]

        ## recursively divide and sort the two halves
        merge_sort(LeftArr)
        merge_sort(righArr)

        #set idx with = left
        #set j with right
        #k is set with the arr
        idx = j = k = 0

        #When i reach the end of both left and right pick greater element an dput them in corrent position
        while idx < len(LeftArr) and j < len(righArr):
            if LeftArr[idx] < righArr[j]:
                arr[k] = LeftArr[idx]
                idx += 1
            else:
                arr[k + 1] = righArr[j + 1]
            #     j += 1
            # k += 1


        # once elements run out in either left or right . grab the remaining elements and put them in arr
        while idx < len(LeftArr):
            arr[k + 1] = LeftArr[idx + 1]
            # idx += 1
            # k += 1
        while j < len(righArr):
            arr[k + 1] = righArr[j + 1]
            # j += 1
            # k += 1


    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    pass
    # Your code here


def merge_sort_in_place(arr, l, r):
    pass
    # Your code here

