First try
=========

very naive approach: take the set of characters from string `a` and `b`, and do `(set_a - set_b) + (set_b - set_a)`.

This solves the sample test case, but quickly falls apart when there are repeating characters in `a` and `b`.

Use a dictionary to keep letters and counts
===========================================

The updated algorithm uses a dictionary to keep letters and their counts.
e.g.,

```
    a="reducer",
    dict_a = {
        'r': 2,
        'e': 2,
        'd': 1,
        'u': 1,
        'c': 1,
    }
```

Take the union of `a` and `b`'s keys and for each key, if it exists in both dicts, then add to the accumulator the difference between the values.

If only a has the key then add `dict_a[key]`. If only b has the key then add `dict_b[key]`.

Use abs
=======

The only modification on the third try is to use `abs` so the accumulator (the total number needed) won't be negative.
