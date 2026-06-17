raw = input('Enter a number:')
print(type(raw))

number=int(raw)
print(type(number))
print(number * 2)




#inline conversion
age = int(input('Enter your age: '))
height = float(input('Enter your height in meters: '))

print(f'In 10 years you will be {age + 10} years old.')
print(f'Height: {height:.2f} m')