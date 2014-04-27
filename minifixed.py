#!/usr/bin/env python
# -*- coding: utf-8 -*-

r"""
Simple fixed-format data reader that guesses offsets.

Does not attempt to do any data transformation other than striping separators
(normally whitespace).

Input can be any iterable of string (str or unicode), including files. The
data is returned as dictionaries of strings. This is not efficient for
large datasets, but is quite convenient for configuration files and small
sets.

For usage examples, first consider some fixed-format data:

>>> data = ["Column1 Column2    Column3\n",
...         "simple1 la lala la 123    \n",
...         "simple2 lalala  la 123*321\n"]
...

Then, it is faily easy to get the data out:

>>> for record in reader(data):
...     print record
...
{'Column1': 'simple1', 'Column3': '123', 'Column2': 'la lala la'}
{'Column1': 'simple2', 'Column3': '123*321', 'Column2': 'lalala  la'}
"""

import re


def reader(list, separator=" "):
        return SimpleReader(list, separator)


class SimpleReader(object):

    def __init__(self, lines, separator=" "):
        self.lines = lines.__iter__()  # iterator (has next() method)
        self.sep = separator
        self.header = None  # a list of tuples (name, start, end)

    def next(self):
        if not self.header:
            self.header = self._parse_header(self.lines.next())
        return self._parse_line(self.lines.next())

    def _parse_header(self, line):
        name = re.compile(r"[^{0}\n]+[{0}]*".format(self.sep))
        return [(col.group().strip(self.sep), col.start(), col.end())
                for col in name.finditer(line)]

    def _parse_line(self, line):
        output = dict()
        for name, start, end in self.header:
            output[name] = line[start:end].strip(self.sep)
        return output

    def __iter__(self):
        return self


if __name__ == "__main__":
    import doctest
    doctest.testmod()
