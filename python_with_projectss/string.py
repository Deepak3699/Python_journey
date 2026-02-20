'''text = input("Enter a sentence: ")

print("Total characters:", len(text))
print("Lowercase:", text.lower())
print("Uppercase:", text.upper())
print("Number of words:", len(text.split()))
vowels = "aeiou"
vowels_count = 
print("Count of letter 'a , e , i , o , u ':", text.count('a,e,i,o,u'))
print(" count spaces ",text.count(' '))'''

text = input("Enter a sentence: ")

print("Total characters:", len(text))
print("Lowercase:", text.lower())
print("Uppercase:", text.upper())
print("Number of words:", len(text.split()))

# Count vowels
vowels = "aeiou"
count = 0

for char in text.lower():
    if char in vowels:
        count += 1

print("Total vowels:", count)

# Count spaces
print("Spaces:", text.count(' '))

# Check if 'python' exists
if "python" in text.lower():
    print("The word 'python' is present")
else:
    print("The word 'python' is not present")