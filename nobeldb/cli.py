# -*- coding: utf-8 -*-

import csv
import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('needle')
    parser.add_argument('data', nargs='?', default='nobel.csv')
    return parser.parse_args()


def main():
    args = get_args()
    with open(args.data) as fh:
        winners = csv.DictReader(fh)
        for winner in winners:
            name = winner['Name']
            if name.lower().startswith(args.needle.lower()):
                print('%s | %s - %s' % (
                    winner['Year'], winner['Name'],
                    winner['Category']
                ))
                # print(winner['Motivation'])
if __name__ == '__main__':
    main()
