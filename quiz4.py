""""Question 4: Capitalize Words
Write a program that accepts a string as input, capitalizes the first letter of each word in the
string, and then returns the result string.
"""
def capitalize_words(sentence):
    return ' '.join(word.capitalize() for word in sentence.split())

print(capitalize_words("i love programming")) # returns "I Love Programming"