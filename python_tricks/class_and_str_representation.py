class Thing:

    def __str__(self):
        return 'str'

    def __repr__(self):
        '''
        human readble
        :return:
        '''
        return 'repr'


if __name__ == '__main__':
    thing = Thing()
    print(thing) # this will print str
    print(repr(thing))
    print(str(thing))
    print(f"{thing} {thing!r}")

