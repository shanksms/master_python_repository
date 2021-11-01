# Important python concepts
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