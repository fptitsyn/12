from itertools import *
s = "01"
a = ["".join(x) + "<" for x in product(s, repeat=20)]
a = [x for x in a if "1111" not in x and "0000" not in x]