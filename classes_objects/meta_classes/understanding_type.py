"""
below code is similar to creating a blank class
e.g.
class Test:
    pass
"""

Test = type('Test', (), {})
print(type(Test))

"""
Lets create a new meta class to control the creation of any class
"""
class Meta(type):
    def __new__(cls, class_name, bases, attrs):
        print(attrs)
        # lets change the attributes name to upperclass
        new_attrs = {}
        for key, val in attrs.items():
            # dont modify dunder methods
            if key.startswith('__'):
                new_attrs[key] = val
            else:
                new_attrs[key.upper()] = val
        print(new_attrs)
        return type(class_name, bases, new_attrs)


class Dog(metaclass=Meta):
    x = 5
    y = 6
    def hello(self):
        print('hi')

Dog().HELLO()
