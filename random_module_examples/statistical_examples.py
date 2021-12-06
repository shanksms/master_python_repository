from random import choices
from collections import Counter
from statistics import stdev, mean

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