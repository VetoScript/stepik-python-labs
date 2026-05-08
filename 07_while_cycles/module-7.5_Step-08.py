name = input()
while name != "Александра":
    name = input()

count = 0
name = input()  # Считываем следующего за Александрой
while name != "Левон":
    count += 1
    name = input()

print(count)
