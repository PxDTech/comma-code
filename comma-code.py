# Write a function that takes a list value as an argument and returns
# a string with all the items separated by a comma and a space, with and
# inserted before the last item.

def comma_code(list):
    if len(list) == 0:
            return "Empty list!"
    string = ""
    for i in list:
           string = string + ", " + i
           print(string)

spam = ['apples', 'bananas', 'tofu', 'cats']

print(comma_code(spam))
#print(comma_code([]))



