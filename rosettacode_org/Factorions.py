"""
http://www.rosettacode.org/wiki/Factorions#Python
Factorions

Definition
A factorion is a natural number that equals the sum of the factorials of its digits.


Example
145   is a factorion in base 10 because:

          1! + 4! + 5!   =   1 + 24 + 120   =   145

It can be shown (see the Wikipedia article below) that no factorion in base 10 can exceed   1,499,999.


Task
Write a program in your language to demonstrate, by calculating and printing out the factorions, that:

  There are   3   factorions in base   9
  There are   4   factorions in base 10
  There are   5   factorions in base 11
  There are   2   factorions in base 12     (up to the same upper bound as for base 10)

"""
"""
base_sum = 0
for i in [1, 4, 5]:
    fac = 1
    for a in range(1, i+1):
        fac *= a

    base_sum += fac

print(base_sum)
"""

fact = [1]  # cache factorials from 0 to 11
for n in range(1, 12):
    print(n)
    fact.append(fact[n-1] * n)

print(fact)

for b in range(9, 12 + 1):
    print(f"The factorions for base {b} are:")
    for i in range(1500000):
        fact_sum = 0
        j = i
        while j > 0:
            d = j % b
            fact_sum += fact[d]
            j = j // b
        if fact_sum == i:
            print(i, end=" ")
    print()

