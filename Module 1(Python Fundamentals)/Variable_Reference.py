# STEP 1: Variables point to objects in memory

print("=" * 50)
print("STEP 1: Variables are References")
print("=" * 50)

# Basic example
x = 42
y = x  # y points to SAME object as x

print(f"x = {x}, id(x) = {id(x)}")
print(f"y = {y}, id(y) = {id(y)}")
print(f"Same object? {id(x) == id(y)}")  # True
print()

# Lists demonstrate reference behavior
list1 = [1, 2, 3]
list2 = list1  # Both point to same list

print(f"Before modification:")
print(f"  list1: {list1}")
print(f"  list2: {list2}")

list2.append(4)  # Modify through list2

print(f"After modifying list2:")
print(f"  list1: {list1}")  # [1, 2, 3, 4] - Changed!
print(f"  list2: {list2}")  # [1, 2, 3, 4]
print()

# Copy to avoid modification
list3 = [1, 2, 3]
list4 = list3.copy()  # New independent copy

print(f"Before modification (copy):")
print(f"  list3: {list3}")
print(f"  list4: {list4}")

list4.append(4)

print(f"After modifying list4:")
print(f"  list3: {list3}")  # [1, 2, 3] - Unchanged ✅
print(f"  list4: {list4}")  # [1, 2, 3, 4]
print()