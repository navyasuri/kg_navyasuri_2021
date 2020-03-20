import argparse
from collections import Counter

'''
NOTE (s): 
The following code is an O(nlogn) solution. 
ASSUMPTIONS: 
1. Unequal strings always return false
2. The order of characters in the strings does not matter. 
   For example, s1=aab, s2=dcc will print "true"
   
'''

def check_mapping(s1, s2):

    # Unequal lengths will return false
    if (len(s1) != len(s2)): 
        return False

    # Count number of each char into a dictionary
    c1 = Counter(s1)
    c2 = Counter(s2)

    l1, l2 = len(c1.values()), len(c2.values())

    # Make sure s1 has equal or more unique chars than s2
    if l1 < l2:
        return False

    for (_, a), (_, b) in zip(c1.most_common(), c2.most_common()):
        if a < b and l1 <= l2:
            return False

    return True

# Parsing arguments
parser = argparse.ArgumentParser(description="Discover one-to-one mapping between 2 strings")
parser.add_argument('s1', type=str, help="Enter s1")
parser.add_argument('s2', type=str, help="Enter s2")

args = parser.parse_args()
s1, s2 = args.s1, args.s2

print(str(check_mapping(s1, s2)).lower())