#Filename:Keyword_only_test.py
#coding = utf-8
def total(initial = 5,*,veg):
    print (initial)
    print (veg)
    #print(num)

total(2,veg=4)