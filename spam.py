text=input('enter the words')
# spam = False
if ('make a lot of money'in text):
    spam= True
elif('buy now' in text):
    spam= True
elif ('subscribe this' in text):
    spam= True
elif('click this' in text):
    spam= True
else:
    spam=False

if (spam):
    print('it is spam')
else:
    print("it's not spam")