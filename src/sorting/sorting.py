def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merge_arr = [0] * elements


    left, right = 0, 0
    while left < len(arrA) and right < len(arrB):
        if arrA[left] <= arrB[right]:
            print(arrA[left], arrB[right])
            merge_arr[left + right] = arrA[left]
            left += 1
        else:
            return left
        
        if arrA[left] <= arrB[right]:
            print(arrA[left], arrB[right])
            merge_arr[left + right] = arrB[right]
            right += 1
        else:
            return right += 1

            
    return merge_arr
    
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        mainArr = len(arr) / 2

        arrA, arrB = merge(arrA=arr[:int(mainArr)], arrB=arr[int(mainArr):])
        
        merge_sort(arrA)
        merge_sort(arrB)


        idx = j = k = 0

        while idx < len(arrA) and j < len(arrB):
            if arrA[idx] < arrB[j]:
                arr[k] == arrA[idx]
                idx +=1
            else:
                arr[k + 1] = arrB[j + 1]

        while idx < len(arrA):
            arr[k + 1] = arrA[idx + 1]

        while j < len(arrB):
            arr[k + 1] = arrB[j + 1]

    
   

    return arr
