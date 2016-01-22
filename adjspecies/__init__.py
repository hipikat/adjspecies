# coding=utf-8
"""
Print the name of a random adjective/species, more or less…
"""

import argparse
from itertools import chain
from os import path
from random import choice
import sys


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--maxlen', type=int, default=8,
                    help="Maximum length for the name, excluding any separator. (default=8)")
parser.add_argument('--sep', type=str, default='', metavar="SEPARATOR",
                    help="Separator between the adjective and species words. (default='')")
parser.add_argument('--count', type=int, default=1,
                    help="Number of adjective/species combinations to print.")
parser.add_argument('--prevent-stutter', action='store_true',
                    help="Prevent the same letter from appearing on an adjective/species boundary. "
                    "(default=True)")


def get_file_lines(file_name):
    """Return a list of non-empty lines from `file_path`."""
    file_path = path.join(path.dirname(path.abspath(__file__)), file_name)
    with open(file_path) as file_obj:
        return [line for line in file_obj.read().splitlines() if line]


def random_species():
    """Return the name of a species at random."""
    return choice(get_file_lines('species.txt'))


def get_describers():
    """
    Return a describer tuple in the form `(name, position)`,
    where position is either 'prefix' or 'suffix'.
    """
    adjectives = map(lambda x: (x, 'prefix'), get_file_lines('adjectives.txt'))
    animal_nouns = map(lambda x: (x, 'suffix'), get_file_lines('nouns.txt'))
    return list(chain(adjectives, animal_nouns))


def random_describer():
    """Return a 2-tuple, matching a describer to 'prefix' or 'suffix'."""
    return choice(get_describers())


def _random_adjspecies_pair():
    """Return an ordered 2-tuple containing a species and a describer."""
    describer, desc_position = random_describer()
    if desc_position == 'prefix':
        return (describer, random_species())
    elif desc_position == 'suffix':
        return (random_species(), describer)


def random_adjspecies_pair(maxlen=None, prevent_stutter=True):
    """
    Return an ordered 2-tuple containing a species and a describer.
    The letter-count of the pair is guarantee to not exceed `maxlen` if
    it is given. If `prevent_stutter` is True, the last letter of the
    first item of the pair will be different from the first letter of
    the second item.
    """
    while True:
        pair = _random_adjspecies_pair()
        if maxlen and len(''.join(pair)) > maxlen:
            continue
        if prevent_stutter and pair[0][-1] == pair[1][0]:
            continue
        return pair


def random_adjspecies(sep='', maxlen=8, prevent_stutter=True):
    """
    Return a random adjective/species, separated by `sep`. The keyword
    arguments `maxlen` and `prevent_stutter` are the same as for
    `random_adjspecies_pair`, but note that the maximum length argument is
    not affected by the separator.
    """
    pair = random_adjspecies_pair(maxlen, prevent_stutter)
    return pair[0] + sep + pair[1]


def main(*argv):
    args = parser.parse_args()
    for count in range(args.count):
        print(random_adjspecies(args.sep, args.maxlen))


if __name__ == '__main__':
    main(sys.argv)
