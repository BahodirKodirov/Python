#1. Create a Dictionary from Two Lists
#Given two lists:
#```python
#keys = ["name", "age", "city"]
#values = ["Alice", 25, "New York"]
#```
#Create a dictionary mapping keys to values using a built-in function.
keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]

My_dic=dict(zip(keys, values))
print(My_dic)

#2. Find the Maximum Value in a Dictionary
#Given the dictionary:
#```python
#scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
#```
#Find the name of the student with the highest score using a single built-in function.
scores = {"Alice": 85, "Bob": 92, "Charlie": 78}
Max_num=max(scores.values())
Max_num

3. Find the Union of Two Sets
Given two sets:
```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
```
Find the union of these sets using a built-in set method.


A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
Union_set=A.union(B)
Union_set

4. Check if a Key Exists in a Dictionary
Given the dictionary:
```python
person = {"name": "John", "age": 30, "city": "London"}
```
Check if `"age"` exists in the dictionary without using a loop.
person = {"name": "John", "age": 30, "city": "London"}
Age_bormi="age" in person
Age_bormi


5. Get Unique Values from a Dictionary
Given the dictionary:
```python
grades = {"Alice": "A", "Bob": "B", "Charlie": "A", "David": "C"}
```
Extract a set of all unique grades using a single line of code.

grades = {"Alice": "A", "Bob": "B", "Charlie": "A", "David": "C"}
Unique_val=set(grades.values())
Unique_val

6. Convert a List of Tuples into a Dictionary
Given a list of tuples:
```python
pairs = [("one", 1), ("two", 2), ("three", 3)]
```
Convert it into a dictionary using a built-in function.
pairs = [("one", 1), ("two", 2), ("three", 3)]
type(pairs)

My_dict=dict(pairs)
My_dict
7. Find the Minimum Value in a Dictionary
Given the dictionary:
```python
temperatures = {"Monday": 20, "Tuesday": 15, "Wednesday": 22}
```
Find the day with the lowest temperature using a single built-in function.
temperatures = {"Monday": 20, "Tuesday": 15, "Wednesday": 22}

Min_val=min(temperatures.values())
Min_val
8. Get the Difference of Two Sets
Given two sets:
```python
X = {10, 20, 30, 40}
Y = {30, 40, 50, 60}
```
Find the elements that are in `X` but not in `Y` using a set method.
X = {10, 20, 30, 40}
Y = {30, 40, 50, 60}

Farq=X.difference(Y)
Farq
