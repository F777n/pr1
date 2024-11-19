def count_characters_without_spaces(s):
 
    return len(s.replace(" ", ""))

result = count_characters_without_spaces("hello world")
print(result) 