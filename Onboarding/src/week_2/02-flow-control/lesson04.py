""" While Loops """

# A while loop repeats a block of code **as long as a condition is True**.
# It is useful when the number of iterations is unknown beforehand.

# Example: Print numbers from 0 to 4
count = 0
while count < 5:
    print(count)
    count += 1  # Increment count by 1

# Example: Print numbers from 5 to 0
count = 5
while count >= 0:
    print(count)
    count -= 1  # Decrement count by 1

# Example: Reading a file line by line using a while loop
# This is helpful when working with large files

# with open('example.txt', 'r') as file:
#     line = file.readline()  # Read the first line
#     while line:             # Continue while there are lines to read
#         print(line.strip())  # Print the line without extra whitespace
#         line = file.readline()  # Read the next line
