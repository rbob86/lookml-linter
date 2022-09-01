import os
import lkml
import glob


class LookMlProjectParser:


    def __init__(self, lkml_dir: str) -> None:
        '''parse a list of LookML filepaths and then read into dictionary object
        Args:
            infilepath (list): list of input LookML file paths
        Returns:

        '''
        self.lkml_dir = lkml_dir

        if os.path.isdir(self.lkml_dir):
            lkml_filepaths = [f for f in glob.glob(
                self.lkml_dir + "**/*.lkml", recursive=True)]
        else:
            raise IOError("Directory does not exist: %s" %
                          self.lkml_dir)
        self.unparsable_lookml_files = []
        self.parsed_lookml_files = {}

        for filepath in lkml_filepaths:

            if not os.path.exists(filepath):
                raise IOError("Filename does not exist: %s" % filepath)

            with open(filepath, 'r') as file:
                try:
                    self.parsed_lookml_files[filepath] = lkml.load(file)
                except SyntaxError:
                    self.unparsable_lookml_files.append(filepath)

    def get_unparsable_lkml_files(self) -> None:
        """get unparsable lkml files (if any)

        Returns:
        unparsable_lookml_files (list) if any, None otherwise
        """
        if len(self.unparsable_lookml_files) > 0:
            return self.unparsable_lookml_files
        return None

    def get_parsed_lookml_files(self) -> None:
        """get dict of lookml project files and data (if any)
        Returns:
            dictionary: dictionary  if any, None otherwise
        """
        if len(self.parsed_lookml_files) > 0:
            return self.parsed_lookml_files
        return None
