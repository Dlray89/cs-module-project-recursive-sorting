def merge(arrA, arrB):
    elements = arrA + arrB
    pivot = elements[0]
    arrA =[]
    arrB = []
    

    # Your code here
    for current in elements[1:]:
        print(current)
        if current < pivot:
            arrA.append(current)
        elif current > pivot:
            arrB.append(current)
            
            
        else:
            return 0
    
    
    return arrA, arrB
    
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
