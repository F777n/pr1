def count_words(input_string):
    
    words = input_string.strip().split()
    return len(words)


result = count_words("Hello world from Python")
print(result) 