def binary_search(arr, low, high, x):
    if high >= low:

        mid = (high + low) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        return -1


input_array = input('Enter the array: ')
array_values= input_array.split(' ')
array = []
for values in array_values:
    array.append(int(values))
array.sort()
print(array)
number=int(input("enter the number: "))
result=binary_search(array,0,len(array)-1,number)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")