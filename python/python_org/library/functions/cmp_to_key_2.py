
from functools import cmp_to_key
import locale

print(sorted(["A", "S", "F", "D"], key=cmp_to_key(locale.strcoll)))

# https://riptutorial.com/python/example/20068/cmp-to-key
