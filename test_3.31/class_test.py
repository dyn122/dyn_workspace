#Filename:class_test
#coding = utf-8

class robot():
    population=0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        robot.population  += 1

    def sayHi(self):
        print('Hellow master,my name is {0},I am {1} years old,nice to serving you!' .format(self.name,self.age))

    def __del__(self):
        print('{0} has done it\'s work ,bye sir!' .format(self.name))

class babysit_robot(robot):
    def __init__(self,name,age,job):
        robot.__init__(self,name,age)
        self.job = job
        print('I am {0},my job is {1}' .format(self.name,self.job))

dog_1 = babysit_robot('dog_wawa',3,'care')
dog_2 = robot('tim',4)
#robot.population += 20
print(dog_1.age)
print(dog_1.population)
print(robot.population)