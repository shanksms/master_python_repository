import csv

with open('techcrunch.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    cols = next(reader) # this is done to skip the first line (assuming first line is header)
    company_dicts = (dict(zip(cols, line)) for line in reader)
    funding = (
        int(company_dict['raisedAmt']) for company_dict in company_dicts if company_dict['round'] == 'a'
    )
    print(f'Total round a funding ${sum(funding) :,}')
