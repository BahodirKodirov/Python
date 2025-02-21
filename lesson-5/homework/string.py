Write a program that will check evennes of given number \n

Numb=int(input('ENter any intiger number'))

if Numb%2==0:
    print('Entered number is even number')
else:
    print('Entered number is odd')

From given 3 numbers from input, find the biggest number

a=float(input('Enter first number: '))
b=float(input('Enter second number: '))
c=float(input('Enter thirth number: '))

if a>b and a>c:
    print(f"Max num is {a}")
elif a<b and b>c:
    print(f"max num is {b} ")
else:
    print(f"Max num is {c}")

a=float(input('Enter first number: '))
b=float(input('Enter second number: '))
c=float(input('Enter thirth number: '))
largest=max(a,b,c)
print(f"Max num is:  {largest}")

Write a program that will find if the number is vowel (aeiou) or consonant

letter=input('Enter any letter: ').lower()

if letter in ('aeiou'):
    print(f"your letter '{letter}' is vowel")
else:
    print(f"your letter '{letter}' is constant")

letter=input('Enter any letter: ')
if letter.isalpha():
    if letter in ('aeiou'):
        print(f"your letter '{letter}' is vowel")
    else:
        print(f"your letter '{letter}' is constant")

else:
    raise ValueError(f'{letter} is wrong')
