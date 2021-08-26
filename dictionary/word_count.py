from collections import Counter


def top_words(words, k):
    counter = Counter(words)
    sorted_word_frequency = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    for i in range(k):
        print(sorted_word_frequency[i][0], sorted_word_frequency[i][1])


if __name__ == '__main__':
    words = ['he', 'she', 'he', 'she', 'he', 'i']
    top_words(words, 2)