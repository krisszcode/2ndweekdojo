numbers= [-5, 23, 0, -9, 12, 99, 105, -43]
min=numbers[0]

for i in range(len(numbers)):
    
    if numbers[i]<=min:
        min=numbers[i]

print(min)