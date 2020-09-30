import re
from collections import Counter
words = re.findall(r'\w+', open('vocabulary.txt').read().lower())
most_common = Counter(words).most_common(2)
print(most_common)
