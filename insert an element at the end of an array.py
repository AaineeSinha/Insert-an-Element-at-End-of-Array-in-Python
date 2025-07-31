# Insert-an-Element-at-End-of-Array-in-Python
n = int(input("Enter size of array: "))
arr = list(map(int, input("Enter array elements: ").split()))
x = int(input("Enter element to insert at end: "))
arr.append(x)
print("New array:", arr)
