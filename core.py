#!/usr/bin/python3
""" Main nocomment script."""


#== TESTING ======================= 
from test_targets import test_file_dialog as target1
#== TESTING =======================

import logging
import time
from collections import OrderedDict
from inspect import isfunction, signature, getmembers, isclass
from docstring_generators.generators import RestviewDocGenerator


logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)


def get_classes(target):
    """ Enumerates classes in target module.

    :param target: loaded target python module
    :returns: dict of discovered classes
    """
    classes = []
    for name, obj in getmembers(target):
        # Check if the class is defined inside the module we are analyzing.
        # This avoids a massive list of classes from imported modules.
        if isclass(obj) and obj.__module__ == target.__name__:
            classes.append(obj)
    logging.info('Found classe(s): {0}'.format(classes))
    return classes


def get_functions(target, classes):
    # Each function key:value where key==function name and value==containing class
    # if no class, value="noclass"
    functions = {}
    # Get functions defined outside of classes
    for funcname, funcptr in target.__dict__.items():
        if isfunction(funcptr):
            # Use inspect.getdoc() instead?
            functions[funcname] = 'noclass'

    # Get classes
    # Get functions defined within those classes
    for c in classes:
        for funcname, funcptr in c.__dict__.items():
            if isfunction(funcptr):
                # Use inspect.getdoc() instead?
                functions[funcname] = c

    print(functions)
    return functions



def get_docstrings(target, functions):
    """ Parses docstrings in target module.

    :param target: loaded target python module
    :param classes: list of defined classes in target module
    :returns: dict of functions and their docstring
    """
    new_docs = {}

    for funcname, theclass in functions.items():
        # Init dict for this function's params
        func_docs = OrderedDict()

        if theclass is 'noclass':
            myfunc = getattr(target, funcname)

            if myfunc.__doc__ is None:
                # Init dict for this function's params
                func_docs = OrderedDict()
                myfunc = getattr(target, funcname)
                sig = signature(myfunc)
                logging.info('Ingesting doc for {0} with signature {1}'.format(funcname, str(sig)))
                params = sig.parameters

                for p in params:
                    p = 'param:'+p
                    func_docs[p] = input('Enter type and description for parameter {0} in {1}: '.format(p, funcname))

                # Ingest return value doc
                ret_doc = input('Enter return value description: ')
                func_docs['returns'] = ret_doc

                # Place param comment dict into return new_docs dict
                new_docs[funcname] = func_docs

        else:
            myfunc = getattr(theclass, funcname)

            if myfunc.__doc__ is None:
                sig = signature(myfunc)
                logging.info('Ingesting doc for {0} with signature {1}'.format(funcname, str(sig)))
                params = sig.parameters
                for p in params:
                    p = 'param:'+p
                    func_docs[p] = input('Enter type and description for parameter {0} in {1}: '.format(p, funcname))
                # Ingest return value doc
                ret_doc = input('Enter return value description: ')
                func_docs['returns'] = ret_doc
                # Place param comment dict into return new_docs dict
                new_docs[funcname] = func_docs
        
    return new_docs


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

    # Enumerate classes defined in target
    classes = get_classes(target1)

    # Enumerate functions defined in target
    functions = get_functions(target1, classes)

    # Check all functions in target file for valid docstrings
    new_docs = get_docstrings(target1, functions)
    logging.info('Processed {0} functions in target module'.format(len(new_docs)))

    # Generete rst documentation from user input
    rst_obj = RestviewDocGenerator()
    rst_docstring = rst_obj.gen_func_docstring(new_docs)
    logging.info('Generated rst-style docstring:\n {0}'.format(rst_docstring))


if __name__ == '__main__':
    main()


































