#!/usr/bin/python
# input file should contain runes encoded as numbers, separated by whitespace. Encoding starts with 0

# number to alphabet
n2g = { ᚠ: 'F', ᚢ: 'U', ᚦ: 'TH', ᚩ: 'O', ᚱ: 'R', ᚳ: 'C/K', ᚷ: 'G', ᚹ: 'W', ᚻ: 'H', ᚾ: 'N', ᛁ: 'I', ᛂ: 'J', ᛇ: 'EO', ᛈ: 'P', ᛉ: 'X', ᛋ: 'S/Z', ᛏ: 'T', ᛒ: 'B', ᛖ: 'E', ᛗ: 'M', ᛚ: 'L', ᛝ: 'NG/ING', ᛟ: 'OE', ᛞ: 'D', ᚪ: 'A', ᚫ: 'AE', ᚣ: 'Y', ᛡ: 'IA/IO', ᛠ: 'EA', •: ' '}

skip = 56
addition = 1

def main():
    counter = 0
    primes = iter( gen_primes() ) 
    parts = open( '56.runes', 'r' ).read().split()
    for rune in parts:
        if rune.isdigit():
            rune = int(rune)
            if counter == skip:
                print counter, ':', n2g[rune], "  (SKIP DECODE)"
                counter=counter+1
                continue
            prime = primes.next();
            print counter, ':', n2g[(rune-prime+addition) % 29]
            counter=counter+1
        else:
            print ":",rune,":"


# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/
def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    D = {}  
    q = 2  
    while True:
        if q not in D:
            yield q        
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1

# main
main()