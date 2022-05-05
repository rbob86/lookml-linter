import os
import lkml
import glob


class LookMlProject:

    root_file_path = "./**/*lkml"

    def __init__(self):
        '''parse a list of LookML filepaths and then read into dictionary object
        Args:
            infilepath (list): list of input LookML file paths
        Returns:
            
        '''
        
        self.lkml_filepaths = [f for f in glob.glob(LookMlProject.root_file_path, recursive=True)]
        self.unparsable_lookML_file = []
        self.lookml_project = {}
        
        for filepath in self.lkml_filepaths:

            if not os.path.exists(filepath):
                raise IOError("Filename does not exist: %s" % filepath)

            with open(filepath, 'r') as file:
                try:
                    self.lookml_project[filepath] = lkml.load(file)
                except SyntaxError:
                    self.unparsable_lookML_file.append(filepath)

        def unparsable_lkml_file(self):
            """get unparsable lkml files (if any)

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
