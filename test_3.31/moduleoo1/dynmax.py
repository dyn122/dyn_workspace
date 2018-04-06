#Filename:dynmax.py
#coding = utf-8

def dyn_max(a,b):
    '''
    It's a module to find max between a and b

    nothing to say,good luck!
    '''
    if int(a) >= int(b):
        return a
    else:
        return b

def dynprint(any):
    '''
    :param any:string or a list
    :return: null
    '''
    for i in any:
        print (i,end='_')



#end of module