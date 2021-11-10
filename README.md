# flyweight
Python metaclass implentation of flyweight pattern

### Examples

Open web page and take a screenshot:
```py
class A(metaclass=Flyweight):
    def __init__(self, a):
        print('init', a)


A(1) 
# init 1
A(1) # no new instance will be created and no call will be made
A(1)
A(2)
# init 2
A(2) # no new instance will be created and no call will be made
A(2)
```
