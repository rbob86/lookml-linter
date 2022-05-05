import os
import lkml


class LookMlProject:

    def __init__(self, infilepaths):
        '''parse a list of LookML filepaths and then read into dictionary object
        Args:
            infilepath (list): list of input LookML file paths
        Returns:
            
        '''
        self.infilepaths = infilepaths
        self.unparsable_lookML_file = []
        self.lookml_project = {}
        for infilepath in self.infilepaths:

            if not os.path.exists(infilepath):
                raise IOError("Filename does not exist: %s" % infilepath)
            
            self.base_filename = os.path.basename(infilepath)

            with open(infilepath, 'r') as file:
                try:
                    self.lookml_project[self.base_filename] = lkml.load(file)
                except SyntaxError:
                    self.unparsable_lookML_file.append(file)

        def unparsable_lkml_file(self):
            """get unparsable lkml file (if any)
            Returns:
            unparsable_lkml_file (list) if any, None otherwise
            """
            if len(self.unparsable_lookML_file) > 0:
                return self.unparsable_lookML_file
            return None
        
        def lookml_project(self):
            """get dict of lookml project files and data (if any)
            Returns:
                dictionary: dictionary  if any, None otherwise
            """
            if len(self.lookml_project) > 0:
                return self.lookml_project
            return None