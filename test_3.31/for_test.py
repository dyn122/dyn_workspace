#Filename:for_test.py
#coding = utf-8
while True:
    s = input('your words :')
    if s == 'exit':
        break;
    elif s == 'pass':
        print('pass now !')
        continue
    elif len(s) < 3 :
        print('too small')
        continue
    print('the length of your words :',len(s))
print('now print s:')
for i in s :
    print (i)
