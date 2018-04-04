#Filename:if_test.py
#coding=utf-8
number = 40
running = True
while running :
    guess = int(input("show your integer:"))
    if guess == number:
        print('congratulations,you guess it !')
        print('done!')
        running = False
    elif guess < number:
        print('maybe it is little higher than that !')
        print('done')
    elif guess > number:
        print('maybe it is little lower than that !')
        print('done')
else:
    print('the loop is over !')