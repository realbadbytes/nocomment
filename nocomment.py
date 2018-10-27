#!/usr/bin/python3
""" Main nocomment script."""


#== TESTING ======================= 
from test_targets import multiproc_queue as target1
#== TESTING =======================

import logging
import time
from collections import OrderedDict
from inspect import isfunction, signature
from docstring_generators.generators import RestviewDocGenerator


logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)


def get_docstrings(target):
    """ Parses docstrings in target module.

    :param target: loaded target python module
    :returns: dict of functions and their docstring
    """
    docstrings = {}
    for funcname, funcptr in target.__dict__.items():
        if isfunction(funcptr):
            logging.info('Found callable: {}'.format(funcname))
            # Use inspect.getdoc() instead?
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


def ingest_docs_from_user(undoc_funcs, target):
    """ Queries the user for documentation on currently undocumented code.

    :param undoc_funcs: list of undocumented functions
    :param target: loaded target python module
    :returns: dict of dicts. undocumented functions with associated raw documentation comments.
    """
    new_docs = OrderedDict()
    # Iterate through undoc_funcs, examine params of each function in target module.

    for func_name in undoc_funcs:
        # Init dict for this function's params
        func_docs = OrderedDict()
        target_func = getattr(target, func_name)
        sig = signature(target_func)
        logging.info('Ingesting doc for {0} with signature {1}'.format(func_name, str(sig)))
        params = sig.parameters

        for p in params:
            p = 'param:'+p
            func_docs[p] = input('Enter type and description for parameter {0} in {1}: '.format(p, func_name))

        # Ingest return value doc
        ret_doc = input('Enter return value description: ')
        func_docs['returns'] = ret_doc

        # Place param comment dict into return new_docs dict
        new_docs[func_name] = func_docs

    return new_docs


def main():
    """ Main nocomment script."""
    logging.info('nocomment starts')

    # Check all functions in target file for valid docstring
    docstrings = get_docstrings(target1)
    logging.info('Processed {0} functions in target module'.format(len(docstrings)))

    # Invalid or non-existent docstring? Prompt for comments
    undoc_funcs = check_docstring_exist(docstrings)
    logging.info('Function(s) without proper documentation: {0}'.format(' '.join(undoc_funcs)))

    # Get new docs for discovered undocumented functions
    new_docs = ingest_docs_from_user(undoc_funcs, target1)

    # Generete rst documentation from user input
    rst_obj = RestviewDocGenerator()
    rst_docstring = rst_obj.generate_docstring(new_docs)
    logging.info('Generated rst-style docstring:\n {0}'.format(rst_docstring))


if __name__ == '__main__':
    main()


































