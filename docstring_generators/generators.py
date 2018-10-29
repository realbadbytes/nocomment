""" Defines the abstract interfact and actual implementation of docstring generator classes."""


from abc import ABC, abstractmethod


class AbstractDocGenerator(ABC):
    """ Provides the API which all *DocGenerator classes must adhere to."""
    def __init__(self):
        pass

    @abstractmethod
    def gen_class_docstring(self):
        pass

    @abstractmethod
    def gen_func_docstring(self):
        pass

    @abstractmethod
    def gen_param_docstring(self):
        pass


class RestviewDocGenerator(AbstractDocGenerator):
    """ Defines the reST-style docstring generator class."""
    def __init__(self):
        super().__init__()
    
    def gen_class_docstring(self):
        pass

    def gen_func_docstring(self, doc_dict):
        """ Returns a well-formed reST-style docstring for inclusion in a Python source file.

        :param doc_dict: dict containing entered comments for function params and return value
        :returns: string of valid reST
        """
        docstring = '\"\"\" '
        for item, contents in doc_dict[1].items():
            if item == 'description':
                docstring += contents + '\n'
            elif item[:5] == 'param':
                docstring += ':param ' + item[6:] + ': ' + contents + '\n'
            # Append return value doc, it'll be last in the OrderedDict
            elif item == 'returns':
                docstring += ':returns: ' + contents
            else:
                print('doc_dict parsing error.')
        docstring += '\n\"\"\"\n\n'
        return docstring


    def gen_param_docstring(self):
        pass


