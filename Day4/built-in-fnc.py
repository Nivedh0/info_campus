# Create list
numbers = [10, 20, 30, 40, 20]

# Add elements
numbers.append(50)          # add at end
numbers.insert(1, 15)       # add at index

# Update element
numbers[2] = 25

# Delete elements
numbers.remove(20)          # removes first occurrence
numbers.pop()               # removes last element

# Traverse list
print("List elements:")
for n in numbers:
    print(n, end=" ")
print()

# Search element
key = 30
if key in numbers:
    print(key, "found in list")
else:
    print(key, "not found")

# Remove duplicates using set
unique_numbers = list(set(numbers))
print("Unique list:", unique_numbers)

# Length, min, max, sum
print("Length:", len(numbers))
print("Min:", min(numbers))
print("Max:", max(numbers))
print("Sum:", sum(numbers))

# Create tuple
t = (10, 20, 30, 20, 40)

# Access elements
print("First element:", t[0])
print("Last element:", t[-1])

# Traverse tuple
print("Tuple elements:")
for x in t:
    print(x, end=" ")
print()

# Count and index
print("Count of 20:", t.count(20))
print("Index of 30:", t.index(30))

# Convert tuple to list (to modify)
t_list = list(t)
t_list.append(50)
t = tuple(t_list)

print("Updated tuple:", t)



# Create dictionary
student = {
    "id": 101,
    "name": "Nived",
    "course": "MCA"
}

# Add new key
student["age"] = 22

# Update value
student["course"] = "MCA Final"

# Delete key
del student["age"]

# Traverse dictionary
print("Student details:")
for key, value in student.items():
    print(key, ":", value)

# Check key existence
if "name" in student:
    print("Name exists")

# Nested dictionary
students = {
    1: {"name": "Rohan", "place": "CLT"},
    2: {"name": "Sulafa", "place": "KSD"}
}

print("Nested dictionary:", students)

# Create set
s = {10, 20, 30, 20, 40}

# Add elements
s.add(50)
s.update([60, 70])

# Remove elements
s.remove(30)      # error if not present
s.discard(100)    # no error if not present

# Traverse set
print("Set elements:")
for x in s:
    print(x, end=" ")
print()

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)

# Remove duplicates from list
lst = [1, 2, 2, 3, 4, 4]
unique_lst = list(set(lst))
print("Unique list:", unique_lst)

# Create string
s = "python programming"

# Length
print("Length:", len(s))

# Access characters
print("First char:", s[0])
print("Last char:", s[-1])

# Traverse string
print("Characters:")
for ch in s:
    print(ch, end=" ")
print()

# String methods
print("Upper:", s.upper())
print("Lower:", s.lower())
print("Title:", s.title())
print("Replace:", s.replace("python", "Python"))

# Reverse string
rev = s[::-1]
print("Reversed:", rev)

# Palindrome check
word = "madam"
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# Count vowels
vowels = "aeiouAEIOU"
count = 0
for ch in s:
    if ch in vowels:
        count += 1
print("Vowel count:", count)
