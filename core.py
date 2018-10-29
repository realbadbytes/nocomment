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

    :param target: Loaded target python module
    :returns: Dict of discovered classes
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
    """ Enumerates functions in target module. Includes both functions outside of classes
    and functions within user-defined classes.

    :param target: Loaded target python module
    :param classes: List of user-defined classes in target module
    :returns: Dict of discovered functions
    """
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

    return functions


def get_docstrings(target, functions):
    """ Proceses functions in target module and prompts user for documentation if none exists.

    :param target: Loaded target python module
    :param functions: List of defined functions in target module
    :returns: Dict containing raw comments entered by user
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


def main():
    """ Main nocomment script."""
    logging.info('nocomment starts')

    # Enumerate classes defined in target
    classes = get_classes(target1)

    # Enumerate functions defined in target
    functions = get_functions(target1, classes)

    # Ingest docstrings
    new_docs = get_docstrings(target1, functions)

    # Generete rst documentation from user input
    rst_obj = RestviewDocGenerator()
    for doc in new_docs.items():
        logging.info('Generating Restview docstring for {0}'.format(doc[0]))
        print(rst_obj.gen_func_docstring(doc))


if __name__ == '__main__':
    main()


































