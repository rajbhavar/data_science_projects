str_array = input("Enter a string value: ")
Text = {}

for char in str_array:
    if char in Text:
        Text[char] += 1
    else:
        Text[char] = 1

result = -1

for char in str_array:
    if Text[char] == 1:
        result = char
        break

print(result)