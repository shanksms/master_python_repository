import csv
from collections import namedtuple, defaultdict, Counter
from pprint import pprint
from glob import glob
from modern_python_course_examples.kmeans import k_means, assign_data

Senator = namedtuple('Senator', ['name', 'party', 'state'])
accumulated_record = defaultdict(list)
vote_translator = {'Yea': 1, 'Not Voting': 0, 'Nay': -1}
NUM_SENATORS = 100
for filename in glob('congress_data/*.csv'):
    with open(filename, encoding='utf-8') as f:
        reader = csv.reader(f)
        vote_topic = next(reader)
        headers = next(reader)
        for person, state, district, vote, name, party in reader:
            senator = Senator(name, party, state)
            accumulated_record[senator].append(vote_translator[vote])

#pprint(accumulated_record, width=400)
record = {senator:tuple(votes) for senator, votes in accumulated_record.items()}
#pprint(record, width=500)
centroids = k_means(record.values(), k=3)
clustered_votes = assign_data(centroids, record.values())
#print(clustered_votes)
# Build a reverse mapping of vote history to senators who voted that way
votes_to_senators = defaultdict(list)
for senator, votes_history in record.items():
    votes_to_senators[votes_history].append(senator)
assert sum([len(cluster) for cluster in votes_to_senators.values()]) == NUM_SENATORS

# Display the clusters and voting pattern in each cluster
for i, votes_in_cluster in enumerate(clustered_votes.values(), start=1):
    print(f'############Voting cluster {i}####################')
    party_counter = Counter()
    for votes in set(votes_in_cluster):
        for senator in votes_to_senators[votes]:
            print(senator)
            party_counter[senator.party] += 1
    print(party_counter)