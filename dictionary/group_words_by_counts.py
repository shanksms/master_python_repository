from collections import defaultdict


def group_by_count(ls_of_words):
    d = defaultdict(list)
    for word in ls_of_words:
        key = len(word)
        d[key].append(word)
    return d
if __name__ == '__main__':
    print(group_by_count(['a', 'b', 'cc', 'ddd']))
