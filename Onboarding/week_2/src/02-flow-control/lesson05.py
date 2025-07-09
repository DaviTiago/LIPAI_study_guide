"""Control Flow Tools: break, continue, and pass"""

# These statements are used to alter the flow of loops:
# 1. `break`: Immediately exits the loop.
# 2. `continue`: Skips the current iteration and continues to the next.
# 3. `pass`: Does nothing – it’s used as a placeholder.

# --- Example 1: break ---
# Stops the loop when a specific condition is met

for i in range(10):
    if i == 5:
        print("Breaking at", i)
        break  # Exit loop
    print("Value:", i)

# --- Example 2: Finding the position of a number in a list ---
# Search for a number and stop as soon as it's found

search = 5
numbers = [1, 5, 9, 7, 3, 3, 2, 1, 7]
position = -1  # Default position if number is not found

counter = 0
for number in numbers:
    print("Checking position:", counter)
    if number == search:
        position = counter
        break  # Exit loop after finding
    counter += 1

print("Found at position:", position)

# --- Example 3: continue ---
# Skips specific values in the loop

print("Skipping number 3 in the list:")
for number in numbers:
    if number == 3:
        continue  # Skip number 3
    print(number)

# --- Example 4: pass ---
# Used as a placeholder when no action is required (often for future code)

print("Using pass as a placeholder:")
for i in range(5):
    if i == 2:
        pass  # Do nothing for now
    print("Current number:", i)
