class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    #The hash function
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    def __setitem__(self, key, value):
        hash = self.get_hash(key)
        found = False
        for index, element in enumerate(self.arr[hash]):
            if len(element) == 2 and element[0] == key:
                self.arr[hash][index] = (key, value)
                found = True
                break
        if not found:
            self.arr[hash].append((key, value))

    def __getitem__(self, key):
        hash = self.get_hash(key)
        for element in self.arr[hash]:
            if len(element) == 2 and element[0] == key:
                return element[1]
        return 'There is no such key-value pair!'
    
    def __delitem__(self, key):
        hash = self.get_hash(key)
        for index, element in enumerate(self.arr[hash]):
            if len(element) == 2 and element[0] == key:
                del self.arr[hash][index]
                return True 
        return 'There is no such key-value pair!'


if __name__ == '__main__':
    samplehashtable = HashTable()

    print(samplehashtable.get_hash('march 6'))
    print(samplehashtable.get_hash('march 17'))

    #__setitem__
    samplehashtable['march 6'] = 310
    samplehashtable['march 6'] = 110
    samplehashtable['march 8'] = 380
    samplehashtable['march 9'] = 302
    samplehashtable['march 17'] = 450

    #__getitem__
    print(samplehashtable['march 79'])
    print(samplehashtable['march 6'])
    print(samplehashtable['march 17'])

    #__delitem__
    #del samplehashtable['march 9']
    #del samplehashtable['march 6']
    print(samplehashtable.arr)
