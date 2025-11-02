#  append() - Adds an element to the end
fruits = ['apple', 'banana']
fruits.append('mango')
print("1. append:", fruits)

#  extend() - Adds multiple elements
fruits.extend(['grapes', 'cherry'])
print("2. extend:", fruits)

#  insert(index, element) - Inserts at position
fruits.insert(2, 'orange')
print("3. insert:", fruits)

#  remove(element) - Removes first occurrence
numbers = [1, 2, 3, 2, 4]
numbers.remove(2)
print("4. remove:", numbers)

#  pop([index]) - Removes and returns element
numbers = [10, 20, 30, 40]
print("5. pop (no index):", numbers.pop())  # removes last
print("   pop (with index 1):", numbers.pop(1))
print("   after pop:", numbers)

#  clear() - Removes all elements
temp = [1, 2, 3]
temp.clear()
print("6. clear:", temp)

#  index(element, [start], [end]) - Find index
letters = ['a', 'b', 'c', 'b']
print("7. index of 'b':", letters.index('b'))

#  count(element) - Counts occurrences
nums = [1, 2, 2, 3, 2]
print("8. count of 2:", nums.count(2))

#  sort(reverse=False, key=None) - Sort list
nums = [4, 1, 3, 2]
nums.sort()
print("9. sort ascending:", nums)
nums.sort(reverse=True)
print("   sort descending:", nums)

# Using key parameter
words = ['apple', 'banana', 'kiwi']
words.sort(key=len)
print("   sort by length:", words)

#  reverse() - Reverse list
nums = [1, 2, 3, 4]
nums.reverse()
print("10. reverse:", nums)

#  copy() - Copy list
a = [1, 2, 3]
b = a.copy()
b.append(4)
print("11. original:", a)
print("    copy:", b)

#  len() - Count elements
a = [10, 20, 30]
print("12. length:", len(a))

#  max(), min(), sum()
nums = [3, 5, 1, 9]
print("13. max:", max(nums))
print("    min:", min(nums))
print("    sum:", sum(nums))

#  del - Delete by index
a = [10, 20, 30, 40]
del a[1]
print("14. del index 1:", a)

#  Slicing
a = [1, 2, 3, 4, 5]
print("15. slicing [1:4]:", a[1:4])
print("    reversed:", a[::-1])

#  List Comprehension
squares = [x**2 for x in range(6)]
print("16. list comprehension:", squares)

#  Nested Lists
matrix = [[1, 2], [3, 4], [5, 6]]
print("17. nested list element:", matrix[0][1])

#  Membership Operators (in / not in)
a = ['apple', 'banana', 'cherry']
print("18. 'apple' in list:", 'apple' in a)
print("    'grape' not in list:", 'grape' not in a)

# Concatenation (+) and Repetition (*)
list1 = [1, 2]
list2 = [3, 4]
print("19. concatenation:", list1 + list2)
print("    repetition:", list1 * 3)

#  join() and split() (string-related)
words = ['Python', 'is', 'awesome']
sentence = " ".join(words)
print("20. join:", sentence)

split_words = sentence.split(" ")
print("    split:", split_words)

# End of demo
print("\n All list methods demonstrated successfully!")
