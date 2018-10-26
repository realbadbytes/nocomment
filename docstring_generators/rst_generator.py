"""This module contains the reST-style docstring generator class."""

__docformat__ = 'reStructuredText'


class RSTGenerator(object):
    """
    This is brief reST-style description.

    :param param1: this is the first param
    :param param2: this is the second param
    :returns: this is a return object description
    :raises keyError: raises an exception
    """
    def __init__(self):
        pass
    def generate_docstring(self):
        """Outputs reST formatted docstring for inclusion in target file."""
        return '\"\"\"Test reST description.\"\"\"'

