## Homework 1
#Extract car names from this text.
#txt = 'MsaatmiazD'
txt = 'MsaatmiazD'

car1 = txt[::2]
# car1

car2 = txt[-1::-2]
# car2

print(f'Name of first car is {car1} \n second car name is {car2}')

## Homework 2

txt = "I'm John. I am from London."

#txt[-7:-1]

r = txt.split()[-1]
r
