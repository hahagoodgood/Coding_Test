# Difference between uppercase and lowercase ASCII codes
CASE_DIFF = 32

i_str = input()
result = ""

for char in i_str:
    if char.isupper():
        # Convert uppercase to lowercase
        result += chr(ord(char) + CASE_DIFF)
    else:
        # Convert lowercase to uppercase
        result += chr(ord(char) - CASE_DIFF)

print(result)