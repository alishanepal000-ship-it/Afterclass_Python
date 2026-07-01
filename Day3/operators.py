# floor division and modulo
a = 20
b =4

print(a/b) #remainder dinxa
print(a%b) 

# floor division floor towards -infinity, not toward zero
print(-a//b)
print(-a%b)

# exponnetial
print(2**10) #1024
print(2** -1) #negative exponnet = reciprocal
print(9** 0.5)
# ** bhaneko root hunxa

# arithemetic on string and lsits
#string concatenation nad repetition
first = "Hello"
second = "World"
greeting = first + second #concatenation bhaneko jodne
print (greeting)

line = '-' * 20 # repetition
print(line)

# we can not mix string and number with +
#print("Age: " + 25) #type error
print("Age: " +str(25))

#list concatenation and repetition
a = [1,2,3]
b= [4,5,6]
print(a+b) #concatenation
print(a*3) #repetition

# counter example
counter = 0
counter += 1 #same as :counter = counter +1
print(counter)

counter += 1
print(counter)

counter *= 10
print(counter)

counter //= 3
print(counter)

counter **= 2
print(counter)

# comparison operators
#== = true is equal to
#!= not true

# truth tables
# and ma duitai true bayo bhane matra true hunxa
# or ma euta true bhayo bhane ni true hunxa
# not ma not ture xa bhane false hunxa aani not false xa bhane true hunxa

# short-circuit evaluation
# x = 0
# result = (x!= 0 and (10 / x > 1) )#duitai condition false xa tyai bhayera false vako
# print(result) #false
# result = (x!= 0 & (10 / x > 1) )
# print(result)
# result = (x!= 0 and (10 / 0) )
# print(result)

# is le object ko memory herxa matlab address

# memebership operator in and not in

# in with strings (checks for substrings)
print("sa" in "Alisha") #true
print("zc" not in "Alisha") #true

# in with lists
nums = [ 1,2,3,4]
print(2 in nums) #true
print(5 not in nums) #true

# in with dicts -checks keys not values
info = {"name": "Alisha", "Age": 20}
print("name" in info) #true
print("Alisha" in info) #false kina ki Alisha key haina
print("Alisha" in info.values()) #tue kina ki info.values le value check garxa

# is le memory ko kun thauma object save bhako xa check garxa

a = "This is a string"
b = "This is a string"
a == b

a is b #false
a is not b #true

x = 20
y = 20
x == y #true