def binary_search(arr, x):
    return search(arr, x, 0, len(arr)-1)

def search(arr, x, low, high):
    if low > high:
        return -1
    mid = int(low + (high-low)/2)
    if arr[mid] > x:
        return search(arr, x, mid+1, high)
    elif arr[mid] == x:
        return mid
    else:
        return search(arr, x, low, mid-1)

if __name__ == '__main__':
    A = [3,7,6,5,5,5,34,56]
    print("Index of the search element is ", binary_search(A, 69))