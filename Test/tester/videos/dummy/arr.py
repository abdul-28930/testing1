# # arr = [3,5,2,6,9,1]
# # print("Array Elements:")
# # for i in arr:
#     # print(i)
#     # print("\n")
    
# def main():
#     # Creating an array of 4 integers
#     int_array = [None] * 4
#     int_array[0] = 5
#     int_array[1] = 6
#     int_array[2] = 7
#     int_array[3] = 8

#     print("Array Elements: ", end='')
#     for j in range(4):
#         print(int_array[j], end=' ')
#     print()

# if __name__ == "__main__":
#     main()

# def main():
#     # Declare the array with the size and the array elements
#     array = [1, 2, 6,3,2,4,2,2,9,5, 7, 8, 9, 10]
    
#     # Declare a flag variable and initialize it to 0
#     flag = 0

#     # Iterate through the array and compare each element of the array to the item
#     for i in range(10):
#         print(array[i], end=' ')

# if __name__ == "__main__":
#     main()

# def main():
#     arr = [1,2,3,4,5,6,7,8,9,10]
#     flag = 0
#     print("Elements in the array : \n")
#     for i in range(10):
#         print(arr[i], end=' ')

#     print("\n\nEnter the element to search: ")
#     item = int(input())
#     index = 0

#     for i in range(len(arr)):
#         if arr[i] == item:
#             flag = 1
#             index = i
#             break
    
#     if flag == 1:
#         print(f"Element '{item}' found in the array at index:{index}")
#     else:
#         print("Element not found in the array")

# if __name__ == "__main__":
#     main()

# def main():
#     size = 5
#     arr = [1,2,3,4,5]
#     print("Array Elements: ")
#     for i in arr:
#         print(i, end=' ')
    
#     pos = int(input("\nEnter the position to insert the element: "))
#     ele = int(input("Enter the element to insert: "))
    

#     if 0 <= pos <= size:
#         arr.append(0)
#         for i in range(size, pos, -1):
#             arr[i] = arr[i-1]
#         arr[pos] = ele
#         for i in range(size+1):
#             print(arr[i], end=' ')
#     else:
#         print("Invalid position")

# if __name__ == "__main__":
#     main()  

# def main():
#     arr = [1,2,3,4,5]
#     size = len(arr)
#     ele = int(input("enter element to delete : \n"))

#     index = 0
#     for i in range(size):
#         if ele == arr[i]:
#             index = i
#             break
    
#     if index != 0:
#         for i in range(index, size - 1):
#             arr[i] = arr[i + 1]

#         size = size - 1
#         print("New Array:", end=' ')
#         for i in range(size):
#             print(arr[i], end=' ')
#     else:
#         print("Element Not Found")

# if __name__ == "__main__":
#     main()
