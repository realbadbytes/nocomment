#!/usr/bin/python3
""" Main nocomment script."""


#== TESTING ======================= 
from test_targets import target1
#== TESTING =======================

import logging
import time


logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)


def get_docstrings(target):
    """ Parses docstrings in target module.

    :param target: loaded python module
    :returns: dict of functions and their docstring
    """
    docstrings = {}
    for funcname, funcptr in target.__dict__.items():
        if callable(funcptr):
            logging.info('Found callable: {}'.format(funcname))
            docstrings[funcname] = funcptr.__doc__
    return docstrings


def check_docstring_exist(func_docstring_dict):
    """ Checks processed functions for docstrings.

    :param func_docstring_dict: dict of functions and their associated docstrings
    :returns: list of undocumented functions
    """
    empty_docstrings = []
    for funcname, docstring in func_docstring_dict.items():
        if docstring is None:
            empty_docstrings.append(funcname)
    return empty_docstrings


def main():
    """ Main nocomment script."""
    logging.info('nocomment starts')
    # Check all functions in target file for valid docstring
    docstrings = get_docstrings(target1)
    logging.info('Processed {0} functions in target module.'.format(len(docstrings)))
    # Invalid or non-existent docstring? Prompt for comments
    undoc_funcs = check_docstring_exist(docstrings)
    logging.info('Function(s) without proper documentation: {0}'.format(' '.join(undoc_funcs)))
    # Build docstring


if __name__ == '__main__':
    main()
