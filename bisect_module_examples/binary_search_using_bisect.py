import bisect

"""
The bisect_left function tries to find the position at which the number is supposed to be.  
This is actually what bisect.insort does as well; it inserts the number at the correct position by searching for  
the location of the number.
"""

def contains(sorted_list, value):
    insert_location_from_left = bisect.bisect_left(sorted_list, value)
    return insert_location_from_left < len(sorted_list) and value == sorted_list[insert_location_from_left]


if __name__ == '__main__':
    sorted_list = [1, 2, 5]
    print(contains(sorted_list, 2))
    print(contains(sorted_list, -1))