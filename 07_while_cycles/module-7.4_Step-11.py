n = int(input())
current_val = 1
next_val = 1
counter = 0
while counter < n:
    print(current_val, end=" ")
    new_val = current_val + next_val
    current_val = next_val
    next_val = new_val
    counter += 1
