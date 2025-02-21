## 1)Given a side of square. Find its perimeter and area.
a= int(input("side of square is: "))
P=4*a
S=pow(a,2)
print("Perimetri: ", P)
print("Yuzi teng: ", S)

## 2)Given diameter of circle. Find its length.
d=float(input("diameter of circle is: "))
r=d/2
L=2*3.14*r
print("Aylananing uzunligi: ", L)

#3)Given two numbers a and b. Find their mean.
a=float(input("First number is: "))
b=float(input("Second number is: "))
m=(a+b)/2
print("Mean equal: ", m)
#4)Given two numbers a and b. Find their sum, product and square of each number.
a=float(input("First number is: "))
b=float(input("Second number is: "))
sum=a+b
product=a*b
S1=pow(a,2)
S2=pow(b,2)
print("Sum of ",a, "and ", b, " is ", sum)
print("Product of ",a, "and ",b, " is ", product)
print ("Square of " , a, " is: ", S1)
print ("Square of ", b, " is: ", S2)

