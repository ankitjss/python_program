a=int(input('enter number'))
b=int(input('enter number'))
c=int(input('enter number'))
d=int(input('enter number'))

if (a>b):
    h1=a
    print('a is highest')
else:
    h1=b
    print('b is highest')
if(c>d):
    h2=c
    print('c is highest')
else:
    h2=d
    print('d is highest')
if(h1>h2):
    print(str(h1)+'is highest')
else:
    print(str(h2) + 'is highest')
