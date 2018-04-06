#Filename:use_of_module
#coding = utf-8
import dynmax

cage = []
dic ={}

print(dynmax.dyn_max.__doc__,dynmax.dynprint.__doc__)

while True:
    t_1 = input('the first num:')
    if t_1 == 'end': break
    t_2 = input('the second num:')
    if t_2 == 'end': break
    cage.append(dynmax.dyn_max(int(t_1),int(t_2)))
    dic[str(dynmax.dyn_max(int(t_1),int(t_2)))] = dynmax.dyn_max(int(t_1),int(t_2))

dynmax.dynprint(sorted(cage))
print('\n')
dynmax.dynprint(dic)
print(dic)