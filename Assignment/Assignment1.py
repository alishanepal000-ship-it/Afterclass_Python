# Find the sum of all numbers: nums = [3, 6, 1, 8, 4]

nums = [3, 6, 1, 8, 4]
sum = 0

for num in  nums:
    sum+= num
    print(sum)


# Count even numbers: nums = [2, 5, 8, 11, 14]
nums = [2, 5, 8, 11, 14]

count = 0

for num in nums:
    if num % 2 == 0:
        count += 1

print(count)

