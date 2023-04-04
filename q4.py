# Task a
d = {i: (i-1)*i for i in range(1, 31)}
print(d)

# Task b
for k, v in d.items():
    print(k, v)

# Task c
total = 0
for v in d.values():
    total += v
print("Total sum of values:", total)

# Task d
num = input("Enter a number to remove from the dictionary: ")
if num.isdigit():
    num = int(num)
    if num in d:
        del d[num]
        print(f"Dictionary after removing {num}: {d}")
    else:
        print(f"{num} is not a key in the dictionary.")
else:
    print("Invalid input. Please enter a number.")