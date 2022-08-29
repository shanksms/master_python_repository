import heapq

"""
Since the heappush and heappop functions both have O(log(n)) time complexity, they can be considered really fast.  
Combining those for the n items in the preceding iterable gives us O(n*log(n)) for the heapsort function.  
The heappush method uses list.append() internally and swaps the items in the list to avoid the O(n) time complexity of  
list.insert().
"""

def heap_sort(iterable):
    heap = list(iterable)
    heapq.heapify(heap)

    while heap:
        yield heapq.heappop(heap)


if __name__ == '__main__':
    print(list(heap_sort([1, 3, 5, 2, 4, 1])))



