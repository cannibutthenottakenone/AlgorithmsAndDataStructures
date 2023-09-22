# Check if a given list of numbers represents a max-heap or not
#


# Returns true if the array is a max-heap
#level order from highest to lowest level, from right to left
def _isMaxHeap(arr):
    for i in range(len(arr)-1, 1, -1):
        if arr[i//2]<arr[i]:
            return False
        
    return True


def isMaxHeap(arr):
    if _isMaxHeap(arr):
        print("Yes")
    else:
        print("No")


# Driver Code
if __name__ == '__main__':
    arr1 = [None, 90, 36, 18, 8, 25, 7, 1]   # expected answer: YES
    isMaxHeap(arr1)

    arr2 = [None, 90, 36, 18, 98, 25, 7, 1]  # expected answer: NO
    isMaxHeap(arr2)

    arr3 = [None, 90, 36, 18, 8, 25, 7, 20]  # expected answer: NO
    isMaxHeap(arr3)
