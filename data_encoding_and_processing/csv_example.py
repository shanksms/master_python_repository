import csv
from collections import namedtuple


def as_named_tuple():
    with open('stock.csv') as f:
        f_csv = csv.reader(f)
        headings = next(f_csv)
        Row = namedtuple('Row', headings)
        for r in f_csv:
            row = Row(*r)
            print(f"{row.Symbol},{row.Price}")


def as_dict():
    with open('stock.csv') as f:
        f_csv = csv.DictReader(f)
        for r in f_csv:
            print(f"{r['Symbol']},{r['Price']}")


if __name__ == '__main__':
    #as_named_tuple()
    as_dict()
