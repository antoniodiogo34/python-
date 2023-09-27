a = int(input("digite o primeiro valor inteiro:"))
b = int(input("digite o segundo valor inteiro:"))
c = int(input("digite o terceiro valor inteiro:"))
if a > b and a > c and b > c:
    print(a,b,c)
elif a > b and a > c and c > b:
    print (a, c, b)
elif b > a and b > c and a > c:
    print(b,a,c) 
elif b > a and b > c and c > a:
    print(b,c,a)
elif c > a and c > b and b > a: 
    print(c,b,a) 
else:
    print(c,a,b)