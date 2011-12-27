'''
This module is aimed at simplifying pretty printing of data in fixed-width
interface, such as a terminal.

@version: 0.1
@author: Tomasz Jaskowski
@contact: http://github.com/tadeck
@license: GNU Lesser General Public License (LGPL)
'''


__author__ = "Tomasz Jaskowski <tadeck@gmail.com>"
__date__ = "27 December 2011"
__version__ = "0.1"
__version_info__ = (0, 1)
__license__ = "GNU Lesser General Public License (LGPL)"


__all__ = [
    'PrettyTable'
]


class PrettyTable():
    """Class for processing data that should be printed as table.

    Example usage:
    >>> data = [['aaa','b'],['ccc','dd']]
    >>> table = PrettyTable(data)
    >>> print table
    +-----+----+
    | aaa | b  |
    +-----+----+
    | ccc | dd |
    +-----+----+
    >>> header = ['Column One', 'Column Two']
    >>> table = PrettyTable(data, header=header)
    >>> print table
    +------------+------------+
    | Column One | Column Two |
    +------------+------------+
    | aaa        | b          |
    +------------+------------+
    | ccc        | dd         |
    +------------+------------+
    """

    def __init__(self, data, header=None):
        """Create a printable table-like structure for outputting in terminal.

        Keyword arguments:
        data      -- actual data to be printed
        header    -- header row with length matching columns number (optional)
        """
        self._data = [header] + data if header else data
        self._refresh_metadata()
        self._build_divider_line()
        self._build_format()

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, repr(self._data))

    def __str__(self):
        lines = []
        for row in self._data:
            lines.append(self._divider_line)
            lines.append(self._format.format(*row))
        lines.append(self._divider_line)
        return '\n'.join(lines)

    def _build_divider_line(self):
        dashes = map(lambda x: '-' * x, self._columns_lengths)
        self._divider_line = '+-{}-+'.format('-+-'.join(dashes))

    def _build_format(self):
        replaces = map(lambda x: '{:<' + str(x) + '}', self._columns_lengths)
        self._format = '| {} |'.format(' | '.join(replaces))

    def _refresh_metadata(self):
        self._columns_number = max(map(len, self._data))
        max_len = lambda x: max(map(len, x))
        self._columns_lengths = map(max_len, zip(*self._data))
