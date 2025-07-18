# pattern_drawing.py

# Prompt the user to input a positive integer for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to handle each row
while row < size:
    # For each row, print asterisks side by side
    for column in range(size):
        print("*", end="")
    # Move to the next line after completing a row
    print()
    # Increment the row counter
    row += 1
