import string

user_string = input("Enter a string: ")
new_string = ''
punctuation = set(string.punctuation)
result = ''

for elem in user_string:
    if elem in punctuation:
        continue
    else:
        new_string += elem

new_string = new_string.split()
for elem in new_string:
    result += elem.capitalize()
print(result)
