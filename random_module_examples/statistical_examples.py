from random import choices, shuffle
from collections import Counter
from statistics import stdev, mean

# https://learning.oreilly.com/videos/modern-python-livelessons/9780134743400/9780134743400-MOPY_01_02_02/

# what is the probability of getting 5 heads from a 7 spin of a biased coin
trial = lambda : choices(['head', 'tail'], cum_weights=[0.6, 1.0], k=7).count('head') >=5
n = 10000
print(sum(trial() for _ in range(n)) / n)


# Choices with weighting
population = ['red', 'black', 'green']
weights = [18, 18, 2]
number_of_choices = 6
print(Counter(choices(population, weights, k=number_of_choices)))

# confidence interval

timings = [7.18, 8.59, 12.24, 7.39, 8.16, 8.68, 6.98, 8.31, 9.06, 7.06,
           7.67, 7.67, 10.02, 6.87, 9.07]
print('#' * 30)
print(mean(timings))
print(stdev(timings))
# build a 90% confidence interval

def bootstrap(data):
    """
    choose k samples with replacement from the population
    """
    return choices(data, k=len(data))
n = 10000
means = sorted([mean(bootstrap(timings)) for _ in range(n)])
# first twenty
print(means[:20])
print(means[-20:])

# 90% confidence interval is 5% at the each end

print(f'5 % is {round(.05 * n)}')
print(f'the observed mean of {mean(timings)}')
print(f'falls in the confidence interval of {means[500] :.1f} to {means[-500] :.1f}')

# p-value. What is the chance that what you observed is due to chance or due to real effects
print('#' * 30)
drugs = [7.1, 8.5, 6.4, 7.7, 8.2, 7.6, 8.4, 5.1, 8.1, 7.4, 6.9, 8.4]
placebo = [8.2, 6.1, 7.1, 7.1, 4.9, 7.4, 8.1, 7.1, 6.2, 7.0, 6.6, 6.3]
"""
One way to find out is through a type of test called a permutation test.
And we approach the idea of, let's assume the null hypothesis. What does the null hypothesis mean?
It's a technical way of saying, let's presume that the drug did nothing, that there was no difference
between the placebo and the drug. If, in fact, there was no difference between the placebo and the drug,
we should be able to swap participants out of one group and into the other, and get a observed mean that
is as extreme as what we observed here. So, the whole notion of this exact test, and it's called a permutation
test, is we want to take the data and reshuffle it, moving the participants between the two groups, effectively
relabeling them. 
"""
print(mean(drugs))
print(mean(placebo))
obs_diff = mean(drugs) - mean(placebo)
print(obs_diff)
comb = drugs + placebo
nd = len(drugs)
# if we reshuffle (permutate, relabel) the partcipant, is the new mean diff the same or more extreme
# than observed diff

def trial_for_drug_test(comb):
    shuffle(comb)
    diff = mean(comb[:nd]) - mean(comb[nd:])
    return diff >= obs_diff

n = 10000
p_value = sum([trial_for_drug_test(comb) for _ in range(n)])/n
print(f'p value is {p_value}')
# general standard for p-value is 5%, so, in our case null hypothesis is correct
