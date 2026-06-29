stu_names = "Archana Singh, Vikash Gupta, Navaya Singh, Rajen Mondal"

# (a) Extract the first name of the first student
first_name = ""
for char in stu_names:
    if char == " ":
        break  # Stop when we reach the first space
    first_name += char

# (b) Count the total number of students
count = 1  # Start with 1 because there is at least one student
for char in stu_names:
    if char == ",":
        count += 1  # Increase count whenever a comma is found

# (c) Print all names in uppercase
print("Names in uppercase:")
for char in stu_names:
    if 'a' <= char <= 'z':  # Convert lowercase to uppercase using ASCII
        print(chr(ord(char) - 32), end="")
    else:
        print(char, end="")
    if char == ",":  # Move to a new line after a comma
        print()

# Print results
print("First name of first student:", first_name)
print("Total number of students:", count)
