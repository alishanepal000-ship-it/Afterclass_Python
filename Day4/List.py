# empty=[]

# #list of integers
# scores = [85, 92, 78, 95, 60]

# #Mixed types
# mixed = [42, 3.14, 'hello', True, None]

# #Nested list (list of lists)
# matrix = [[1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]]

# print(scores)
# print(mixed)
# print(matrix[1])


# #indexing and slicing
# fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

# print(fruits[0]) #first item
# print(fruits[-1]) #last item
# print(fruits[1:4]) #slice: index 1 up to (not including) 4
# print(fruits[:3]) #first three
# print(fruits[::2]) #every other item

#list methods in action
nums = [3, 1, 4, 1, 5, 9, 2, 6]

nums.append(7)
print('append: ', nums)

nums.extend([4,8])
print('extend: ', nums)

nums.insert(2,9)
print('insert:', nums)

nums.insert(2,3)
print('insert: ', nums)

nums.remove(1)
print('remove: ', nums)

popped = nums.pop()
print('pop: ',nums, 'got:', popped)

print('index: ', nums.index(5))
print('count 8:', nums.count(8))

nums.sort()
print('sort: ', nums)
