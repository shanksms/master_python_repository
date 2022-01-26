"""
Drawing an example from geometry, let’s write a function which can return the area of a two-dimensional rectangle,
the volume of a three-dimensional cuboid, or indeed the hyper-volume of an n-dimensional hyper-cuboid.
Such a function needs to accept an arbitrary number of numeric arguments and multiply them together.
This shows the usage of vargs
"""
def hypervolume(length, *lengths):
      v = length
      for item in lengths:
          v *= item
      return v

def tag(name, **attributes):
    """
    build tags
    """
    result = '<' + name
    for key, value in attributes.items():
        result += ' {k}="{v}"'.format(k=key, v=value)
    result += '>'
    return result

if __name__ == '__main__':
    print(hypervolume(3))
    print(hypervolume(3, 5, 7))
    print(tag('img', src="monet.jpg", alt="Sunrise by Claude Monet", border=1))