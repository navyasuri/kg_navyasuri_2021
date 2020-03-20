import argparse
from collections import Counter

def check_mapping(s1, s2):

    if (len(s1) != len(s2)): 
        return False

    # Count number of each char into a dictionary
    c1 = Counter(s1)
    c2 = Counter(s2)

    l1, l2 = len(c1.values()), len(c2.values())

    print(c1, c2)

    # Make sure s1 has more unique chars than s2
    if l1 < l2:
        print('from here')
        return False

    
    for a, b in zip(sorted(c1.values(), reverse=True), sorted(c2.values(), reverse=True)):
        if a < b and l1 <= l2:
            print(a, b)
            return False
    return True


parser = argparse.ArgumentParser(description="Discover one-to-one mapping between 2 strings")
parser.add_argument('s1', type=str, help="Enter s1")
parser.add_argument('s2', type=str, help="Enter s2")

args = parser.parse_args()
s1, s2 = args.s1, args.s2

print(check_mapping(s1, s2))