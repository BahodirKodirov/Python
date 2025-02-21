Homework

Count Vowels in a String

Problem:
Count the number of vowels (a, e, i, o, u) in a given string.
text = "hello world"

count = 0
for char in text:
    if char in "aeuioAEUIO":
        count += 1

print(f'Vowels in {text}: {count}')
Find the Maximum Number in a List

Problem:
Find the maximum number in a list using a loop (without using max()).

ls = [1,6,83,6,2, -100]

max_num = 0
for num in ls:
    if num>max_num:
        max_num = num

print(f'Max number in a list: {max_num}')
