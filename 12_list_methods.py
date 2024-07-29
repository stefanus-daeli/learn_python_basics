#List Methods

numbers = [1,2,3,4,5]
print(numbers)

numbers.append(6) #[1, 2, 3, 4, 5, 6]
print(numbers)
numbers.insert(0 , -1) #[-1, 1, 2, 3, 4, 5, 6]
print(numbers)
numbers.remove(3) #[-1, 1, 2, 4, 5, 6]
print(numbers)

print(len(numbers)) #6

numbers.clear() #[]
print(numbers)
