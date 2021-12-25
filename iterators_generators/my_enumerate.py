class MyEnumerate:
    def __init__(self, data, start_index=0):
        self.data = data
        self.index = 0
        self.start_index = start_index

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.start_index, self.data[self.index]
        self.index += 1
        self.start_index += 1
        return value


class MyEnumerateWithDelegatedIterator:
    def __init__(self, data, start_index=0):
        self.data = data
        self.index = 0
        self.start_index = start_index

    def __iter__(self):
        return MyIterator(self.data, self.start_index)


class MyIterator:
    def __init__(self, data, start_index=0):
        self.data = data
        self.index = 0
        self.start_index = start_index

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.start_index, self.data[self.index]
        self.index += 1
        self.start_index += 1
        return value


class MyEnumerateGenerator:
    def __init__(self, data, start_index=0):
        self.data = data
        self.index = 0
        self.start_index = start_index

    def __iter__(self):
        while self.index < len(self.data):
            value = self.start_index, self.data[self.index]
            self.index += 1
            self.start_index += 1
            yield value


if __name__ == '__main__':
    for index, letter in MyEnumerate('abc', 1):
        print(f'{index} : {letter}')
    print('#' * 60)
    for index, letter in MyEnumerateWithDelegatedIterator('abc', 2):
        print(f'{index} : {letter}')
    print('#' * 60)
    for index, letter in MyEnumerateGenerator('abc', 2):
        print(f'{index} : {letter}')
