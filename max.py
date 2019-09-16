numbers= [-5, 23, 0, -9, 12, 99, 105, -43]
max=numbers[0]

for i in range(len(numbers)):
    if numbers[i]>=max:
        max=numbers[i]

print(max)