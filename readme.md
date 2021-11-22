# Important python concepts
### resources
[python decorators] (https://www.youtube.com/watch?v=MjHpMCIvwsY)

### Why Python is slow compared to compiled languages?
http://jakevdp.github.io/blog/2014/05/09/why-python-is-slow/

### What is raw string in python
backslash in python is used as a escape character. 
Sometimes, particularly when dealing with strings such as Windows filesystem paths 
or regular expression patterns which use backslashes extensively, 
the requirement to double-up on backslashes can be ugly and error prone. 
Python comes to the rescue with its raw strings. Raw strings don't support any escape sequences and are very much 
what-you-see-is-what-you-get. To create a raw string, precede the opening quote with a lower-case r:
```python
path = r'C:\Users\Merlin\Documents\Spells'
```

### string as collection of unicode points
A string is a sequence of Unicode code-points, and for the most part you can think of code-points 
as being like characters, although they aren't strictly equivalent. The sequence of code-points in a 
Python string is immutable, so once you've constructed a string, you can't modify its contents.
A code point is any one member of the set of of numerical values which make up the code space.
Each character is associated with a single code point, so GREEK CAPITAL LETTER SIGMA is assigned to U+03A3 and N-ARY 
SUMMATION is assigned to U+2211.  As we have done here, code points are often written in U+nnnn form where nnnn is a 
four, five or six digit hexadecimal number. Not all code points have yet been allocated to characters. 
For example, U+0378 is an unassigned code point, and there’s nothing to stop you including this code point in a Python
 str using the \u0378 escape sequence; hence, str really is a sequence of code points and not a sequence of characters

### Converting between bytes and str
To convert between bytes and str we must know the encoding of the byte sequence used to represent the string's 
Unicode code points as bytes. Python supports a wide-variety of so-called codecs such as UTF-8, UTF-16, ASCII, Latin-1,
 Windows-1251, and so on – consult the Python documentation for a current list of codecs

In Python we can encode a Unicode str into a bytes object, and going the other way we can decode a bytes object into
 a Unicode str. In either direction it's up to us to specify the encoding. Python won't — and generally speaking can't 
 do anything to prevent you erroneously decoding UTF-16 data stored in a bytes object using, say, a CP037 codec for 
 handling strings on legacy IBM mainframes.

If you're lucky the decoding will fail with a UnicodeError at runtime; if you're unlucky you'll wind up with a str 
full of garbage that will go undetected by your program.
```python
norsk = "Jeg begynte å fortære en sandwich mens jeg kjørte taxi på vei til quiz"
data = norsk.encode('utf-8')
print(data)
b'Jeg begynte \xc3\xa5 fort\xc3\xa6re en sandwich mens jeg kj\xc3\xb8rte taxi p\xc3\xa5 vei til quiz'
norwegian = data.decode('utf-8')
norwegian == norsk
True
```

### The __name__  type and executing modules from the command line
The Python runtime system defines some special variables and attributes, the names of which are delimited by double 
underscores. One such special variable is called __name__, and it gives us the means for our module to determine whether
 it has been run as a script or, instead, imported into another module or the REPL. To see how, add:
print(__name__)
```python
from urllib.request import urlopen


def fetch_words():
   with urlopen('http://sixty-north.com/c/t.txt') as story:
       story_words = []
       for line in story:
           line_words = line.decode('utf-8').split()
           for word in line_words:
               story_words.append(word)

       for word in story_words:
           print(word)

print(__name__)
```

now lets do import from console. you will notice it prints the name of the module.
```python
from text_encoding import words
text_encoding.words
```
next, run the module directly (in other words run the module as a script)
```shell script
$ python3 words.py
__main__
```
Therefore, we put following check in all the python modules which are supposed to be importable
and cann also run as script
```python
if __name__ == '__main__':
    pass
```
### enum. 
enum is used when you want to limit the value of a constant.

```python
class Condition(Enum):
    NEW = 0
    GOOD = 1
    OK = 2
```

### dunder magic methods
1. functions, methods, modules that start with __ and end with __
2. meant to be called indirectly. e.g. n1.__add__(n2) gets called on n1 + n2
<br>
__str__ is mainly used to provide information to user of the class. __repr__ is used by developers to know how to create an object 

### self parameter
``` python
class Flight:

    def number(self):
        return "SN060"
f = Flight()
Flight.number(f)
```
### instance initializer
If provided, the initializer method is called as part of the process of creating a new object when we call the constructor. The initializer method must be called __init__() delimited by the double underscores used for Python runtime machinery. Like all other instance methods, the first argument to __init__() must be self.
<br>
If you're coming from a Java, C#, or C++ background it's tempting to think of __init__() as being the constructor. This isn't quite accurate; in Python the the purpose of __init__() is to configure an object that already exists by the time __init__() is called. The self argument is, however, analogous to this in Java, C#, or C++. In Python the actual constructor is provided by the Python runtime system and one of the things it does is check for the existence of an instance initializer and call it when present.

### class methods
@classmathod decorator is used to mark a method in a class as a class method. 
This method will have access to all the class level variables. Generally, 
a classmethod is used to define an alternate constructor. Take a look at the below example:
```python
import time
class Date:
    # primary contructor
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)
```

### decorators
lets understand decorators with a simple example. when you see below:
```python
@mydeco
def add(a, b):
    return a + b
```
you should imagine this:
```python
def add(a, b):
    return a + b

add = mydeco(add)
```
this is the definition of my deco
```python
def mydeco(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```
