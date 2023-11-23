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


class MyClass(object):
    def set_val(self, val):
        self.value = val
        
    def get_val(self):
        return self.value   
    
a = MyClass()
b = MyClass()   
a.value = 'hello'

a.set_val(10)
b.set_val(100)


print(a.get_val())
print(b.get_val())

############################

class MyInteger(object):
    def set_val(self, val):
        try:
            val = int(val)
        except ValueError:
            return
        self.val = val
        
    def get_val(self):
        return self.val
    
    def increment_val(self):
        self.val= self.val + 1
        
i = MyInteger()
i.set_val(9)
print(i.get_val())
i.val = 'hi'
print(i.get_val())

#####init_constructor

class MyNum(object):
    def __init__(self, value):
        print ('calling__init__')
        self.val = value
        
    def increment(self):
        self.val = self.val + 1
        
dd = MyNum(5)

dd.increment()
dd.increment()

print (dd.val)

class YourClass(object):
    classy = 'class value!'
    
dd = YourClass()
print(dd.classy)

dd.classy= 'inst value!'
print(dd.classy)

###########@

class InstanceCounter(object):
    count = 0
    
    def __init__(self, val):
        self.val = val
        InstanceCounter, count +=1
        
    def set_val(self, newval):
        self.val = newval
        
    def get_val(self):
        return self.val
    
    def get_count(self):
        return InstanceCounter.count
    
a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter(17)

for obj in (a, b, c):
    print('val of obj: %s' %(obj.get_val()))
    print('val of obj: %s' %(obj.get_count()))
    