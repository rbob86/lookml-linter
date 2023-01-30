import os
import lkml
import glob


class LookMlProjectParser:
    root_file_path = "./"

    def __init__(self) -> None:
        '''parse a list of LookML filepaths and then read into dictionary object
        Args:
            infilepath (list): list of input LookML file paths
        Returns:

        '''
        if os.path.isdir(LookMlProjectParser.root_file_path):
            lkml_filepaths = [f for f in glob.glob(
                LookMlProjectParser.root_file_path + "**/*.lkml", recursive=True)]
        else:
            raise IOError("Directory does not exist: %s" %
                          LookMlProjectParser.root_file_path)
        self.unparsable_lookml_files = []
        self.parsed_lookml_files = {}
        for filepath in lkml_filepaths:
            if not os.path.exists(filepath):
                raise IOError("File does not exist: %s" % filepath)
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
