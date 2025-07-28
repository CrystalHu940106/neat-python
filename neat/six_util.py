"""
Compatibility module for Python 2/3 compatibility.
In Python 3, iteritems and iterkeys are just items and keys.
"""

def iteritems(d):
    """Return an iterator over the (key, value) pairs of dictionary d."""
    return d.items()

def iterkeys(d):
    """Return an iterator over the keys of dictionary d."""
    return d.keys() 