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
from typing import Any
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
        InstanceCounter.count += 1
        
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
    print('count: %s' %(obj.get_count()))
    
###########

class MaxSizeList(object):
    def __init__(self, max):
        self.max_size = max
        self.innerList = []
        
    def push(self, obj):
        self.innerList.append(obj)
        if len(self.innerList) > self.max_size:
            self.innerList.pop(0)
    
    def get_list(self):
        return self.innerList
    
a = MaxSizeList(3)
b = MaxSizeList(1)

a.push("hey")
a.push("hi")
a.push("let's")
a.push("go")

b.push("hey")
b.push("hi")
b.push("let's")
b.push("go")

print(a.get_list())
print(b.get_list())
    
######################
class Animal(object):
    def __init__(self, name):
        self.name = name
    
    def eat(self, food):
        print('%s is eating %s!'%(self.name, food))

class Dog(Animal):
    def fetch(self, thing):
        print('%s goes after the %s!' %(self.name, thing))
        
class Cat(Animal):
    def swatstring(self):
        print('%s shreds the string!' %(self.name))
        
    
r = Dog('Rover')
f = Cat('Fluffy')

r.fetch('paper')
f.swatstring()
r.eat('dog food')
r.eat('some food')
        
    #########polymorphism(len)
    
class Animal(object):
    def __init__(self, name):
        self.name = name
        
    def eat(self, food):
        print ('{0} eats {1}'.format(self.name, food))
        
#############
import random

class Animal(object):
    def __init__(self, name):
        self.name = name
        
class Dog(Animal):
    
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.breed = random.choice(['Shit Tzu', 'Beagle', 'Mutt'])
        
    def fetch(self, thing):
        print ('%s goes after the %s!'%(self.name, thing))
        
    ##########
    
    class A(object):
        
        def dothis(self):
            print ('doing this in A')
            
    class B(A):
        pass
    
    class C(A):
        def dothis(self):
            print('do in c')
            
    class D(B,C):
        pass
    
    d_instance = D()
    d_instance.dothis()
    
    print (D.mro())
    

###################@

class InstanceCounter(object):
    count = 0
    
    def __init__(self, val):
        self.val = self.filterint(val)
        InstanceCounter.count += 1
        
    @staticmethod
    def filterint(value):
        if not isinstance(value, int):
            return 0
        else:
            return value
        
a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter('hello')

print(a.val)
print(b.val)
print(c.val)
        
        
##############


        
#########

import abc

class GetSetParent(object):
    __metaclass__ = abc.ABCMeta
    def __init__(self, value):
        self.val = 0
    def set_val(self, value):
        set.val = value
    def get_val(self):
        return set.val
    
class GetSetInt(GetSetParent):
    def set_val(self, value):
        if not isinstance(value, int):
            super(GetSetInt, self).set_val(value)
    def showdoc(self):
        print('GetSeInt object({0}), only accepts integer values'.format(id(self)))
        
        
class GetSetList(GetSetParent):
    def __init__(self, value= 0):
        self.vallist = [value]
    def get_val(self):
        return self.vallist[-1]
    def get_vals(self):
        return self.vallist
    def set_val(self, value):
        self.vallist.append(value)
    def showdoc(self):
        print('getlist object, len{0}, stores, history of values set'.format(len(self.vallist)))
        
###############

import abc
from datetime import datetime

class WriteFile(object):
    
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def write(self):
        return
    
    def __init__(self, filename):
        self.filename = filename
        
    def write_line(self, text):
        fh = open(self.filename, 'a')
        fh.write(text + '\n')
        fh.close()
        
class DelimFile(WriteFile):
    def __init__(self, filename, delim):
        super(DelimFile.self).__init__(filename)
        self.delim = delim
        
    def write(self, this_list):
        line = self.delim.join(this_list)
        self.write_line(line)
        
        
class Logfile(WriteFile):
    def write(self, this_line):
        dt = datetime.now()
        date_str = dt.strftume('%y-%m-%d %H=%M')
        self.write_line('{0} {1}'.format(date_str, this_line))
        
########################
class SumList(object):
    
    def __init__(self, this_list):
        self.mylist = this_list
        
    def __add__(self, other):
        new_list = [ x + y for x, y in zip(self.mylist, other.mylist)]
        
        return SumList(new_list)
    
    def __repr__(self):
        return str(self.mylist)
    
cc = SumList([1, 2, 3, 4])
dd = SumList([1, 2, 3, 4])

ee = cc + dd
        
print(ee) 

####################

class MyDict(dict):
    
    def __setitem__(self, key, val):
        print ("setting a key and a value!")
        dict.__setitem__(self, key, val)
        
dd = MyDict()
dd['a'] = 5
dd['b'] = 6

for key in dd:
    print('{0}={1}'.format(key, dd[key]))
    
print

##############@@

class MyList(list):
    
    def __getitem__(self, index):
        if index == 0: raise IndexError
        if index > 0:  index = index - 1
        return list.__getitem__(self, index)
    
    def __set__item(self, index, value):
        if index == 0: raise IndexError
        if index > 0:  index = index - 1
        return list.__getitem__(self, index, value)

x = MyList(['a', 'b', 'c'])
print(x)

x.append('spam')
    
print(x[1])

############################

class MyClass(object):
    
    def __enter__(self):
        print('we have entered "with"')
        return self
    
    def __exit__(self, type, value, traceback):
        print('we are leaving "with"')
        
   
    def sayhi(self):
        print('hi, instance %s' %(id(self)))
        
cc = MyClass()
with MyClass() as cc:
    cc.sayhi()
    
print('after the "with" block')

#########@

        
        
class MyDict(dict):
    def __item__(self, key, val):
        
        dict.__setitem__(self, key, val)
        
        
        
        




    
    


        
    
        
        

        
    