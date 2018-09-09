import pickle
import pandas
import sklearn
import re
import pprint as pp
pprint = pp.PrettyPrinter().pprint


def parseBalance(balance_spec):
    balance_tokens = balance_spec.split('/')
    if len(balance_tokens) < 3:
        return None
    balance_pt = balance_tokens[1].strip()
    return balance_pt


PARSER_DICT = {
    'Balance': parseBalance
}


def parse(racquet_specs):
    racquet_features = {}
    for name, specs in racquet_specs.items():
        features = []
        for spec_name, parser in PARSER_DICT.items():
            parsed_value = parser(specs[spec_name])
            if(parsed_value):
                features.append(parsed_value)
            else:
                break
        if len(features) < len(PARSER_DICT.keys()):
            print('Racquet has missing features:', name)
            continue
        else:
            racquet_features[name] = features
    return racquet_features


if __name__ == '__main__':
    with open('racquet_specs.pkl', 'rb') as filename:
        racquet_specs = pickle.load(filename)
        parsed_specs = parse(racquet_specs)
        pprint(parsed_specs)
