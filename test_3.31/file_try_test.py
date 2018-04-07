#!/usr/bin/python3.5
#Filename:file_try_test
#coding = utf-8
import time
print('hellow')
try:
    name = input("File you wanna open:")
    f = open(name,'r')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line,end=' ')
        #time.sleep(2)
except KeyboardInterrupt:
    print('You end it!')
finally:
    f.close()
    print('File is closed!')

with open('dyn.txt') as ff:
    for line in ff:
        print(line)