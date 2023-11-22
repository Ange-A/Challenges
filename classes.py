class MyClass(object):
    pass

this_obj = MyClass() #instance
######################
print(this_obj)

class Joe(object):
    greeting = 'hello, Joe'
    
thisjoe = Joe()

print(thisjoe.greeting)

##############

class Joe(object):
    def callme(self):
        print('calling "callme" method with instance: ')
        
thisjoe = Joe()

thisjoe.callme()

print; print

###############A method on an instance passes instance as the argument to the method(named seld in the method)

import random
class MyClass(object):
    def dothis(self):
        self.rand_val = random.randint(1, 10)
        
myinst = MyClass()
myinst.dothis()
print(myinst.rand_val)


        