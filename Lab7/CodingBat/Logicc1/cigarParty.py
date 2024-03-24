import random
# When squirrels get together for a party,
# they like to have cigars. 
# A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. 
# Unless it is the weekend, in which case there is no upper bound on the number of cigars. 
# Return True if the party with the given values is successful, or False otherwise.

# cigar_party(30, False) → False
# cigar_party(50, False) → True
# cigar_party(70, True) → Tru

def cigar_party(cigars, is_weekend):
    return cigars >= 40 and cigars <= 60 or is_weekend and cigars >= 40


if __name__ == '__main__':
    cigars = random.randint(1, 100)
    is_weekend = random.choice([True, False])
    print(cigar_party(cigars, is_weekend))