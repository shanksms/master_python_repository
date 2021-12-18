import csv
from collections import namedtuple, defaultdict
from pprint import pprint
from glob import glob

Senator = namedtuple('Senator', ['name', 'party', 'state'])
accumulated_record = defaultdict(list)
for filename in glob('congress_data/*.csv'):
    with open(filename, encoding='utf-8') as f:
        reader = csv.reader(f)
        vote_topic = next(reader)
        headers = next(reader)
        for person, state, district, vote, name, party in reader:
            senator = Senator(name, party, state)
            accumulated_record[senator].append(vote)

pprint(accumulated_record, width=400)