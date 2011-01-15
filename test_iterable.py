import unittest
import string
from iterable import for_each_in


if __name__ == '__main__':
    def even(x): return x % 2 == 0
    def lowercase(x): return x.lower()

    for_each_in(string.ascii_uppercase).skip(20).take(6).display()\
        .transform(lowercase).display()\
        .transform(ord).display()\
        .select(even).display()\
        .reverse().display()
