import argparse
from collections import Counter

parser = argparse.ArgumentParser(description="Discover one-to-one mapping between 2 strings")
parser.add_argument('s1', type=str, help="Enter s1")
parser.add_argument('s2', type=str, help="Enter s2")

args = parser.parse_args()
s1, s2 = args.s1, args.s2

c1 = Counter(s1)
c2 = Counter(s2)
