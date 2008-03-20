"""
Helper functions to make gof backwards compatible (tested on python 2.4 and 2.5)
"""

import sys
if sys.version_info[:2] < (2,5):
    def all(iterable):
        for element in iterable:
            if not element:
                return False
        return True
    def any(iterable):
        for element in iterable:
            if element:
                return True
        return False
else:
     # Only bother with this else clause and the __all__ line if you are putting
     # this in a separate file.
     import __builtin__
     all = __builtin__.all
     any = __builtin__.any

__all__ = ['all', 'any']
