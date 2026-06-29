s = input()  # Original string
index = int(input())    # Index to change
new_char = input()  # New character

new_s = ""  # Initialize an empty string

for i in range(len(s)):  # Loop through each character
    if i == index:
        new_s = new_s + new_char  # Replace the character at the given index
    else:
        new_s = new_s + s[i]  # Copy original characters

print(new_s)  # Output: "hallo"
