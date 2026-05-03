total = 0
num1 = int(input())
num2 = int(input())
for i in range(num1, num2 + 1):
    if (i**3) % 10 == 4 or (i**3) % 10 == 9:
        total += 1
print(total)
