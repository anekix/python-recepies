# List of useful python snippets mostly adopted from itertools module

Check is all elements of an iterable are equal
```python
from itertools import groupby

def all_equal(iterable):
    "Returns True if all the elements are equal to each other"
    g = groupby(iterable)
    return next(g, True) and not next(g, False)
```

Chain multiple iterator together and process results

```python
from itertools import chain

chain('ABC', 'DEF') # --> A B C D E F
```
