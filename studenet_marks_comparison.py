sub1=float(input('enter subject marks\n'))
sub2=float(input('enter subject marks\n'))
sub3=float(input('enter subject marks\n'))

if (sub1<33 or sub2<33 or sub3<33):
    print('student is fail')
elif (((sub1+sub2+sub3)/3)<40):
    print('student is fail')
else:
    print('student is pass')

