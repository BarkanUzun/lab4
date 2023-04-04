# Part a
divided = {'Tony': 41, 'Rhodey': 43, 'Nat': 35}
we_fall = {'Steve': 39, 'Clint': 35, 'Wanda': 28}
united_we_stand = {**divided, **we_fall}

print("Name\tAge")
for name, age in united_we_stand.items():
    print(f"{name}\t{age}")

# Part b
if 'Nat' in united_we_stand:
    del united_we_stand['Nat']
print("\nAfter removing 'Nat':")
print("Name\tAge")
for name, age in united_we_stand.items():
    print(f"{name}\t{age}")

# Part c
print("\nSorted by key:")
print("Name\tAge")
for name, age in sorted(united_we_stand.items()):
    print(f"{name}\t{age}")

# Part d
values = united_we_stand.values()
print(f"\nMaximum value: {max(values)}")
print(f"Minimum value: {min(values)}")